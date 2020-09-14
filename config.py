# -*- coding:utf-8 -*-
"""
@file: config.py
@author: wiley
@date: 2020/9/14
@IDE: PyCharm
"""
import os


# 共有配置
class BaseConfig(object):
    AUTHOR = "Wiley"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/blog"
    SERVER_PORT = "5000"
    SERVER_URL = "127.0.0.1"
    DEBUG = True


class ProductConfig(BaseConfig):
    LOG_PATH = "./logs/file_{time}.log"
    LOG_LEVEL = "INFO"
    SQLALCHEMY_DATABASE_URI = "*"
    SERVER_PORT = "80"
    SERVER_URL = "0.0.0.0"
    DEBUG = False


config = {
    "development": DevConfig,
    "product": ProductConfig,
    "default": DevConfig
}
