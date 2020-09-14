# -*- coding:utf-8 -*-
"""
@file: run.py
@author: wiley
@date: 2020/9/14
@IDE: PyCharm
"""
import os
from app import create_app

if __name__ == '__main__':
    app = create_app(os.getenv('ENV') or 'default')
    app.run(app.config.get("SERVER_URL"), app.config.get("PORT"), app.config.get("DEBUG"))
