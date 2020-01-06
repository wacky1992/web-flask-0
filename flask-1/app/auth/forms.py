from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms import ValidationError
from ..model import User


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          '用户名必须只有字母、数字、点或下划线')])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('check_password', message='密码不一致')])
    check_password = PasswordField('检查密码', validators=[DataRequired()])
    submit = SubmitField('提交')

    # 校验邮箱唯一性
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册')

    # 校验用户名唯一性
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经被注册')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('提交')


class ChangePassword(FlaskForm):
    old_password = PasswordField('密码', validators=[DataRequired()])
    new_password = PasswordField('密码', validators=[DataRequired(), EqualTo('check_password', message='密码不一致')])
    check_password = PasswordField('检查密码', validators=[DataRequired()])
    submit = SubmitField('提交')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

