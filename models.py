from db import db


class Student(db.Model):
    # 定义表名
    __tablename__ = 'sys_student'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)