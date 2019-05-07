import codecs
import os

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import config

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, static_folder='static/static', static_url_path='/static')
    app.config.from_object(config[config_name])
    # Don't use SQLAlchemy event system
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config[config_name].init_app(app)

    # Setup extensions
    db.init_app(app)
    codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
    CORS(app, resources={r"/api/*": {"origins": "*"}}, max_age=600)

    # Create app blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.errorhandler(404)
    def resp_not_found(e):
        return jsonify({"error": e.description}), 404

    # noinspection PyUnusedLocal
    @app.errorhandler(500)
    def resp_not_found(e):
        return jsonify({"error": 'Internal Server Error'}), 500

    return app

