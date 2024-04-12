import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
user = 'root'
password = 'qwer1234....'
database = 'ry'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@139.196.39.139:3306/%s' % (user, password, database)
# 设置sqlalchemy自动更跟踪数据库
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 禁止自动提交数据处理
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
db = SQLAlchemy()
with app.app_context():
    db.init_app(app)


class Student(db.Model):
    # 定义表名
    __tablename__ = 'sys_student'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


if __name__ == '__main__':
    student = Student()
    print(student.query.first())
