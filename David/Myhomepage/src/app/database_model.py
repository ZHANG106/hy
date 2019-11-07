from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#  用户数据模型
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), index=True, comment='用户真实姓名')
    email = db.Column(db.String(64), unique=True, index=True)
    phone_number = db.Column(db.String(11), unique=True, index=True)
    info = db.Column(db.String(2048), index=True)
    add_time = db.Column(
        db.DateTime(), index=True, default=datetime.now)  # 注册时间
