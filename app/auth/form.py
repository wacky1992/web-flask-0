from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 32), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住')
    submit = SubmitField('登录')


class SignupForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 32), Email()])
    username = StringField('用户名', validators=[DataRequired(), Length(1, 32),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                     'Usernames must have only letters, numbers, dots or '
                                                     'underscores')])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower().first()):
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    passwrod = PasswordField('新密码', validators=[DataRequired(),
                                                EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('确认新密码', validators=[DataRequired()])
    submit = SubmitField('更新密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 32), Email()])
    submit = SubmitField('修改密码')


class PasswordResetForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    passwrod = PasswordField('新密码', validators=[DataRequired(),
                                                EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('确认新密码', validators=[DataRequired()])
    submit = SubmitField('更新密码')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')