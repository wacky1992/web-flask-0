from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 32), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('记住')
    submit = SubmitField('登录')
