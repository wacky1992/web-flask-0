import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context()))
manager.add_command('db', MigrateCommand)


# manager.command 修饰器让自定义命令变得简单
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
# 这个脚本先创建程序。如果已经定义了环境变量 FLASK_CONFIG ，则从中读取配置名；否则使用默认配置。
# 然后初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。
