# -*- coding:utf-8 -*-
"""
@file: user.py
@author: wiley
@date: 2020/9/14
@IDE: PyCharm
"""
from flask import Blueprint, request
from app.model.user import User
from app import db, logger

user = Blueprint('user', __name__)


@user.route('/', methods=['POST', 'GET'])
def register():
    data = request.get_json()
    logger.info(data)
    if data is None:
        return "please data"
    users = User(first_name=data["first_name"],
                 last_name=data["last_name"],
                 email=data["email"],
                 password=data["password"],
                 is_active=0,
                 role=1)
    db.session.add(users)
    db.session.commit()
    return "ok"
