from sched import scheduler

from flask import Flask
from sqlalchemy.exc import SQLAlchemyError


class SimpleService:
    def __init__(self, f_app, ss_scheduler, main_task, refresh_interval=30.0, priority=5):
        """
        :type f_app: Flask
        :type ss_scheduler: scheduler
        :param main_task: A function.
        :param refresh_interval: Refresh interval in seconds.
        :type refresh_interval: float
        :param priority: A lower number represents a higher priority.
        """
        self.f_app = f_app
        self.ss_scheduler = ss_scheduler
        self.main_task = main_task
        self.refresh_interval = refresh_interval
        self.priority = priority

        self.ss_scheduler.enter(0, self.priority, self.serve)

    def exec_main_task(self):
        with self.f_app.app_context():
            try:
                self.main_task()
            except SQLAlchemyError as exc:
                from app import db
                db.session.rollback()
                print('SQLAlchemy error:', exc)
            except Exception as ex:
                print('Error: {}'.format(ex))

    def serve(self):
        self.exec_main_task()
        self.ss_scheduler.enter(self.refresh_interval, self.priority, self.serve)
