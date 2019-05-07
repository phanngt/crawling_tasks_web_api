from sqlalchemy import func

from app import db


class CrawlingTask(db.Model):
    __tablename__ = 'CrawlingTasks'
    id = db.Column('Id', db.String(32), primary_key=True)
    created_at = db.Column('CreatedAt', db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column('UpdatedAt', db.DateTime, onupdate=func.now())
    action_id = db.Column('ActionId', db.String(32), db.ForeignKey('CrawlingTaskActionMaster.ActionId'), nullable=False)
    track_id = db.Column('TrackId', db.String(32))
    object_id = db.Column('ObjectId', db.String(32))
    priority = db.Column('Priority', db.SmallInteger)
    task_detail = db.Column('TaskDetail', db.JSON)
    batch_id = db.Column('BatchID', db.String(32))
    status = db.Column('Status', db.String(32))
    status_updated_at = db.Column('StatusUpdatedAt', db.DateTime)
    ext = db.Column('Ext', db.JSON)
