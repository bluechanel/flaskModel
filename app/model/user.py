# -*- coding:utf-8 -*-
"""
@file: user.py
@author: wiley
@date: 2020/9/14
@IDE: PyCharm
"""
from app import db


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True, index=True)
    first_name = db.Column(db.VARCHAR(24))
    last_name = db.Column(db.VARCHAR(24))
    email = db.Column(db.VARCHAR(16), index=True, unique=True, nullable=False)
    password = db.Column(db.VARCHAR(64), nullable=False)
    is_active = db.Column(db.Boolean(), default=1)
    role = db.Column(db.Boolean(), default=0)
