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
# 不同数据库地址的引用方式
# MySQL mysql+pymysql://username:password@hostname/database
# Postgres postgresql://username:password@hostname/database
# SQLite（Unix） sqlite:////absolute/path/to/database
# SQLite（Windows） sqlite:///c:/absolute/path/to/database
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
# db 对象是 SQLAlchemy 类的实例，表示程序使用的数据库，同时还获得了 Flask-SQLAlchemy提供的所有功能


# SQLAlchemy的列选项名说明
# primary_key 如果设为 True ，这列就是表的主键
# unique 如果设为 True ，这列不允许出现重复的值
# index 如果设为 True ，为这列创建索引，提升查询效率
# nullable 如果设为 True ，这列允许使用空值；如果设为 False ，这列不允许使用空值
# default 为这列定义默认值
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


# SQLAlchemy关系选项
# backref         在关系的另一个模型中添加反向引用
# primaryjoin     明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
# uselist         如果设为 Fales ，不使用列表，而使用标量值
# order_by        指定关系中记录的排序方式
# secondary       指定多对多关系中关系表的名字
# secondaryjoin   SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件
# lazy            指定如何加载相关记录。可选值有 select（首次访问时按需加载）、 immediate（源对象加载后就加载）、
#                 joined（加载记录，但使用联结）、subquery（立即加载，但使用子查询），
#                 noload（永不加载）和dynamic（不加载记录，但提供加载记录的查询）
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


# 修饰器定义路径，并确认返回值
# @app.route('/', methods=['GET', 'POST'])
# def index():
    # name = None
    # form = SignForm()
    # if form.validate_on_submit():
        # 使用重定向和用户会话
        # session['name'] = form.name.data
        # render是渲染变量到模板中，而redirect是HTTP中1个跳转的函数，一般会生成302状态码。
        # return redirect(url_for('index'))
        # name = form.name.data
        # form.name.data = ''
    # 返回渲染模板的内容
    # return render_template('index.html',
    #                        form=form,
    #                        name=session.get('name'),
    #                        current_time=datetime.utcnow())


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('用户登录异常，请检查')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
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
    manager.run(debug=True)
