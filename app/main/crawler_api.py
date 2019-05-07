from flask import request

from app import db
from app.models import new_uuid4
from app.models.crawling_task import CrawlingTask
from . import main

ACTION_ID_USER_CRAWL_VIDEO = '9776C9A529D845CE8DF37447C7DE8A83'


@main.route('/api/v6/crawler/crawlYoutubeVideo', methods=['POST'])
def crawl_collected_video():
    json = request.json

    crawling_task = CrawlingTask()

    crawling_task.action_id = ACTION_ID_USER_CRAWL_VIDEO
    crawling_task.id = new_uuid4()
    crawling_task.priority = 10

    crawling_task.task_detail = {}

    if 'artist' in json:
        crawling_task.task_detail['artist'] = json['artist']

    crawling_task.task_detail['youtube_id'] = json['youtube_id']
    crawling_task.task_detail['song_title'] = json['song_title']
    crawling_task.task_detail['collection_ids'] = json['collection_ids']

    db.session.add(crawling_task)
    db.session.commit()

    return 'Add crawling task successfully'
