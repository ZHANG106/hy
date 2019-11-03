# coding=utf-8

"""
@author: David
@time: 2019/05/24
"""
# from src.app import db
from app.database_model import User
from flask import Flask, render_template, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)
mail = Mail()
mail.init_app(app)

# 这些最好放在一个config文件里面，用户名密码需要加密
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_SUBJECT_PREFIX'] = 'Hello'
app.config['MAIL_SENDER'] = 'David <18817870180@163.com>'
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://shimian:shimian@182.254.166.148/david"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def hello():
    return render_template('main.html')


@app.route('/register', methods=['GET'])
def loin():
    return render_template('rest.html')


@app.route('/register/in', methods=['POST'])
def register():
    user = User(
        username=request.form.get('username'),
        email=request.values.get('email'),
        phone_number=request.values.get('phone_number'),
        info=request.form.get('info'),
    )
    db.session.add(user)
    db.session.commit()
    # send_content = {
    #     '问候语': '您好！\n',
    #     '发送方': '感谢您的来信\n',
    #     '主体内容': '很高兴认识您，您的信息我已经收到了，很快会给您回复\n',
    #     '注脚': 'David'
    # }
    # send_email(user.email, '验证帐号', send_content)
    return 'Well done', 200


def send_email(to, subject, content):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    body_content = "".join(c for _, c in content.items())
    msg.body = body_content
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
