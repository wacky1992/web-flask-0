# 引用表单相关类
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


# 定义表单类
class SignForm(FlaskForm):
    name = StringField('用户名：', validators=[DataRequired()])
    password = PasswordField('密码：')
    submit = SubmitField('登录')
