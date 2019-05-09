Flask的上下文全局变量类型：
current_app 程序上下文   当前激活程序的程序实例
g           程序上下文   处理请求时用作临时存储的对象。每次请求都会重设这个变量
request     请求上下文   请求对象，封装了客户端发出的 HTTP 请求中的内容
session     请求上下文   用户会话，用于存储请求之间需要“记住”的值的词典

Flask的请求钩子：
before_first_request：   注册一个函数，在处理第一个请求之前运行。
fore_request：           注册一个函数，在每次请求之前运行。
after_request：          注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
teardown_request：       注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。

jinja2变量过滤器
safe             渲染值时不转义
capitalize       把值的首字母转换成大写，其他字母转换成小写
lower            把值转换成小写形式
upper            把值转换成大写形式
title            把值中每个单词的首字母都转换成大写
trim             把值的首尾空格去掉
striptags        渲染之前把值中所有的 HTML 标签都删掉

jinjia2的控制结构
1、判断结构
{% if user %}
Hello, {{ user }}!
{% else %}
Hello, Stranger!
{% endif %}

2、for循环结构
{% for comment in comments %}
<li>{{ comment }}</li>
{% endfor %}