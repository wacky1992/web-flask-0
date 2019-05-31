import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY =  os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
# 配置类可以定义init_app()类方法，其参数是程序实例。
# 在这个方法中，可以执行对当前环境的配置初始化。
# 现在，基类Config中的init_app()方法为空。
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.189.cn'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+pymysql://root:123@localhost/flask'


# 在 3 个子类中， SQLALCHEMY_DATABASE_URI 变量都被指定了不同的值。
# 这样程序就可在不同的配置环境中运行，每个环境都使用不同的数据库
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql+pymysql://'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql+pymysql://'


class ProductionConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}