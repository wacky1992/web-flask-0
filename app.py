from flask import Flask, request, session, redirect, url_for, flash
# 引入命令行解析器
from flask_script import Manager
# 引入渲染模板
from flask import render_template
# 引入bootstrap客户端框架
from flask_bootstrap import Bootstrap
# 引入浏览器时间和日期渲染拓展
from flask_moment import Moment
from datetime import datetime
# 引用表单相关类
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
# 引入数据库框架
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wacky1992'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
# db 对象是 SQLAlchemy 类的实例，表示程序使用的数据库，同时还获得了 Flask-SQLAlchemy提供的所有功能



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True)
    password = db.Column(db.String(80))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# 定义表单类
class SignForm(FlaskForm):
    name = StringField('用户名：', validators=[DataRequired()])
    # password = PasswordField('密码：')
    submit = SubmitField('登录')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


# 修饰器可以通过引用上下文临时把某些对象变为全局可访问
@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>你的浏览器是：%s</p>' % user_agent


# 修饰器定义路径并设置变量name，返回时根据变量name的值返回数值
@app.route('/user/<name>')
def user(name):
    # render_template()第一个参数时模板的文件名称，随后的参数时键值对
    return render_template('user.html', name=name)


# 定义页面404错误
@app.errorhandler(404)
def page_not_fund(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
