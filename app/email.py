# 引用邮件相关库
from flask_mail import Mail, Message
# 引入异步发送邮件
from threading import Thread
from flask import current_app, render_template
from . import mail


# Flask-Mail 中的 send() 函数使用 current_app ，因此必须激活程序上下文。
# 不过，在不同线程中执行 mail.send() 函数时，程序上下文要使用 app.app_context() 人工创建。
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    mail.send(msg)
