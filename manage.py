#!/usr/bin/env python
import os

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command('custom_task')
def custom_task():
    print('Finish custom task.')
