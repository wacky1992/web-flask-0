from flask import Flask
from flask import request
# 引入命令行解析器
from flask_script import Manager
# 引入渲染模板
from flask import render_template
# 引入bootstrap客户端框架
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


# 修饰器定义路径，并确认返回值
@app.route('/')
def index():
    # 返回渲染模板的内容
    return render_template('index.html')


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
