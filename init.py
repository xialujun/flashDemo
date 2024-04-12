from flask import Flask
from db import db
from models import *

import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__) # 新建app对象

app.config.from_object('config') # 加载配置信息，其中有数据库的配置信息，包含在SQLALCHEMY_DATABASE_URI中

# 初始化db,并创建models中定义的表格
with app.app_context(): # 添加这一句，否则会报数据库找不到application和context错误
    db.init_app(app) # 初始化db
    db.create_all() # 创建所有未创建的table

if __name__ == '__main__':
    student = Student()
    student.name = 'xlj222'
    db.session.add(student)