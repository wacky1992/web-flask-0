from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager   # 加载用户的回调函数


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True)
    password_hash = db.Column(db.String(80))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(30), unique=True, index=True)

    @property
    def password(self):
        raise AttributeError('password不是可读属性')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    # generate_password_hash(password, method= •  pbkdf2:sha1, salt_length=8) ：这个函数将
    # 原始密码作为输入，以字符串形式输出密码的散列值，输出的值可保存在用户数据库中。
    # method 和 salt_length 的默认值就能满足大多数需求。

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    # check_password_hash(hash, password) •  ：这个函数的参数是从数据库中取回的密码散列
    # 值和用户输入的密码。返回值为 True 表明密码正确。

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
