# -*- coding: utf-8 -*-
# @Author: zootopia
# @Date:   2020-04-03 14:03:23
# @Last Modified by:   wangqs
# @Last Modified time: 2020-04-03 15:04:44

import os
from whisper import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'zootopia')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)