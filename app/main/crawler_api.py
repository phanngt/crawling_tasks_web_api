from flask import request, make_response, jsonify

from app import db
from app.models import new_uuid4
from app.models.crawling_task import CrawlingTask
from app.models.user import User
from . import main

ACTION_ID_USER_CRAWL_VIDEO = '9776C9A529D845CE8DF37447C7DE8A83'


@main.route('/api/add_collection', methods=['POST'])
def crawl_collected_video():
    my_id = None
    if 'my_id' in request.form:
        my_id = request.form['my_id']
    if not my_id:
        return make_response(jsonify({'error': 'My_id required'}), 400)
    user = User.get(my_id)
    if not user:
        return make_response(jsonify({'error': 'Wrong my_id'}), 400)

    crawling_task = CrawlingTask()

    crawling_task.action_id = ACTION_ID_USER_CRAWL_VIDEO
    crawling_task.id = new_uuid4()
    crawling_task.priority = 10

    crawling_task.task_detail = {}

    if 'artist' in request.form:
        crawling_task.task_detail['artist'] = request.form['artist']
    else:
        crawling_task.task_detail['artist'] = ""

    if 'provider' in request.form:
        crawling_task.task_detail['provider'] = request.form['provider']

    crawling_task.task_detail['youtube_id'] = request.form['youtube_id']
    crawling_task.task_detail['song_title'] = request.form['song_title']

    collection_ids = [x.strip() for x in request.form['collection_ids'].split(',')]
    crawling_task.task_detail['collection_ids'] = collection_ids

    db.session.add(crawling_task)
    db.session.commit()

    return 'Add crawling task successfully'
