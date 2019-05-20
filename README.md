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

3、条件判断
Jinja2 中的条件语句格式为 {% if condition %}...{% else %}...{% endif %} 。
如果条件的计算结果为 True ，那么渲染 if 和 else 指令之间的值


WTFform支持的HTML标准字段
StringField         文本字段
TextAreaField       多行文本字段
PasswordField       密码文本字段
HiddenField         隐藏文本字段
DateField           文本字段，值为 datetime.date 格式
DateTimeField       文本字段，值为 datetime.datetime 格式
IntegerField        文本字段，值为整数
DecimalField        文本字段，值为 decimal.Decimal
FloatField          文本字段，值为浮点数
BooleanField        复选框，值为 True 和 False
RadioField          一组单选框
SelectField         下拉列表
SelectMultipleField 下拉列表，可选择多个值
FileField           文件上传字段
SubmitField         表单提交按钮
FormField           把表单作为字段嵌入另一个表单
FieldList           一组指定类型的字段


WTForms 内建的验证函数
Email           验证电子邮件地址
EqualTo         比较两个字段的值；常用于要求输入两次密码进行确认的情况
IPAddress       验证 IPv4 网络地址
Length          验证输入字符串的长度
NumberRange     验证输入的值在数字范围内
Optional        无输入值时跳过其他验证函数
Required        确保字段中有数据
Regexp          使用正则表达式验证输入值
URL             验证 URL
AnyOf           确保输入值在可选值列表中
NoneOf          确保输入值不在可选值列表中


不同数据库地址的引用方式
MySQL mysql+pymysql://username:password@hostname/database
Postgres postgresql://username:password@hostname/database
SQLite（Unix） sqlite:////absolute/path/to/database
SQLite（Windows） sqlite:///c:/absolute/path/to/database



SQLAlchemy关系选项
backref         在关系的另一个模型中添加反向引用
primaryjoin     明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
uselist         如果设为 Fales ，不使用列表，而使用标量值
order_by        指定关系中记录的排序方式
secondary       指定多对多关系中关系表的名字
secondaryjoin   SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件
lazy            指定如何加载相关记录。可选值有 select（首次访问时按需加载）、 immediate（源对象加载后就加载）、
                joined（加载记录，但使用联结）、subquery（立即加载，但使用子查询），
                noload（永不加载）和dynamic（不加载记录，但提供加载记录的查询）


SQLAlchemy的列选项名说明
primary_key 如果设为 True ，这列就是表的主键
unique 如果设为 True ，这列不允许出现重复的值
index 如果设为 True ，为这列创建索引，提升查询效率
nullable 如果设为 True ，这列允许使用空值；如果设为 False ，这列不允许使用空值
default 为这列定义默认值


SQLAlchemy查询过滤器
filter()        把过滤器添加到原查询上，返回一个新查询
filter_by()     把等值过滤器添加到原查询上，返回一个新查询
limit()         使用指定的值限制原查询返回的结果数量，返回一个新查询
offset()        偏移原查询返回的结果，返回一个新查询
order_by()      根据指定条件对原查询结果进行排序，返回一个新查询
group_by()      根据指定条件对原查询结果进行分组，返回一个新查询


SQLAlchemy查询执行函数
all()           以列表形式返回查询的所有结果
first()         返回查询的第一个结果，如果没有结果，则返回 None
first_or_404()  返回查询的第一个结果，如果没有结果，则终止请求，返回 404 错误响应
get()           返回指定主键对应的行，如果没有对应的行，则返回 None
get_or_404()    返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回 404 错误响应
count()         返回查询结果的数量
paginate()      返回一个 Paginate 对象，它包含指定范围内的结果


创建数据迁移仓库命令
python hello.py db init

创建迁移脚本命令
python hello.py db migrate -m "initial migration"

更新数据库
python hello.py db upgrade



Flask-Mail SMTP服务器的配置
MAIL_SERVER     localhost 电子邮件服务器的主机名或 IP 地址
MAIL_PORT       25        电子邮件服务器的端口
MAIL_USE_TLS    False     启用传输层安全（Transport Layer Security，TLS）协议
MAIL_USE_SSL    False     启用安全套接层（Secure Sockets Layer，SSL）协议
MAIL_USERNAME   None      邮件账户的用户名
MAIL_PASSWORD   None      邮件账户的密码

保存电子邮件服务器用户名和密码的两个环境变量要在环境中定义。
如果你在 Linux 或Mac OS X 中使用 bash，那么可以按照下面的方式设定这两个变量：
(venv) $ export MAIL_USERNAME=<Gmail username>
(venv) $ export MAIL_PASSWORD=<Gmail password>

微软 Windows 用户可按照下面的方式设定环境变量：
(venv) $ set MAIL_USERNAME=<Gmail username>
(venv) $ set MAIL_PASSWORD=<Gmail password>