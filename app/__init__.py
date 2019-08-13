from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()  # 初始化 Flask-Login
login_manager.session_protection = 'strong'     # 初始化 Flask-Login
login_manager.login_view = 'auth.login'  # 初始化 Flask-Login


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    login_manager.init_app(app)   # 初始化 Flask-Login
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # 注册蓝本时使用的 url_prefix 是可选参数。
    # 如果使用了这个参数，注册后蓝本中定义的所有路由都会加上指定的前缀，即这个例子中的 /auth。

    return app
