from flask import render_template
from . import main


# 定义页面404错误
@main.errorhandler(404)
def page_not_fund(e):
    return render_template('404.html'), 404


@main.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500
