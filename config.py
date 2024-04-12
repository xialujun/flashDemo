# 配置 sqlalchemy  "数据库+数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码"

user = 'root'
password = 'qwer1234....'
database = 'ry'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@139.196.39.139:3306/%s' % (user, password, database)
