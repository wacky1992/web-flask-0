from flask_script import Manager, Shell
from app import create_app, db
from app.model import User, Role, Follow, Permission, Post
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post)


manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
