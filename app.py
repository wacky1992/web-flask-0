from flask import Flask
from flask import request
# 引入命令行解析器
from flask_script import Manager
# 引入渲染模板
from flask import render_template

app = Flask(__name__)
manager = Manager(app)


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


if __name__ == '__main__':
    manager.run(debug=True)
