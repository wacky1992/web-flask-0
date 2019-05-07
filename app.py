from flask import Flask
app = Flask(__name__)


# 修饰器定义路径，并确认返回值
@app.route('/')
def index():
    return 'hello world'


# 修饰器定义路径并设置变量name，返回时根据变量name的值返回数值
@app.route('/user/<name>')
def user(name):
    return 'hello world,%s!' % name


if __name__ == '__main__':
    app.run(debug=True)
