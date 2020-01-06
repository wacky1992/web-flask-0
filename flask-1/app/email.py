from threading import Thread
from flask_mail import Message
from flask import current_app, render_template
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    # 不使用current_app的原因：
    # 使用Thread新开了一个线程，如果你不穿真实对象过去，那么你在线程里面使用 current_app 将获取不到对象，因为他没有 flask 上下文。这又是一个 Flask 的重要概念，太多得说
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr