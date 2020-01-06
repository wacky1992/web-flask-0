import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 从环境导入或者使用默认配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'liuhengjian'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_MAIL_SENDER = 'Admin<18912965231@189.cn>'
    FLASKY_MAIL_SUBJECT_PREFIX = '[刘恒健]'
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 50

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
    MAIL_USERNAME = '18912965231@189.cn'
    MAIL_PASSWORD = 'qq625327691'
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+pymysql://root:root@localhost/flask_test_0'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql+pymysql://'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
