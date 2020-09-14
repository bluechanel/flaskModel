# -*- coding:utf-8 -*-
"""
@file: __init__.py.py
@author: wiley
@date: 2020/9/14
@IDE: PyCharm
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from loguru import logger

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    if config_name == "product":
        logger.add(app.config.get("LOG_PATH"), level=app.config.get("LOG_LEVEL"))
        app.config.from_object(config['product'])
    else:
        app.config.from_object(config['development'])

    db.init_app(app)

    from app.views.user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app
