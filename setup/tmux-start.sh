#!/usr/bin/env bash
tmux new-session -d -s "services"
tmux new-window -c "/home/ec2-user/Developer/github.com/Glue-th/web-api" -n "caching" '. env/bin/activate && FLASK_APP=manage flask clean_cache && FLASK_APP=manage flask maintain'
tmux new-window -c "/home/ec2-user/Developer/github.com/Glue-th/web-api" -n "web-api" '. env/bin/activate && honcho start'
tmux new-window -c "/home/ec2-user/Developer/github.com/Glue-th/web-api" -n "uri-mapping" '. env/bin/activate && FLASK_APP=manage flask uri_mapping'
