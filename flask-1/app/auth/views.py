from flask import render_template, redirect, url_for, session, current_app, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..model import User
from ..email import send_mail
from .forms import SignUpForm, LoginForm, ChangePassword, PasswordResetRequestForm, PasswordResetForm


# 处理程序中过滤未确认的账户
@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        # 更新已登录用户的访问时间
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


# 登录页面
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(password=form.password.data):
            login_user(user, form.remember_me.data)
            # 用户访问未授权的URL时会显示登录表单，Flask - Login会把原地址保存在查询字符串的next参数中，这个参数可从request.args字典中读取。
            # 如果查询字符串中没有next参数，则重定向到首页
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('无效的电子邮件或密码。')
    return render_template('auth/login.html', form=form)


# 退出登录
@auth.route('/logout')
# 如果未认证的用户访问这个路由，Flask-Login 会拦截请求，把用户发往登录页面。
@login_required
def logout():
    logout_user()
    flash('你已经退出登录')
    return redirect(url_for('main.index'))


@auth.route('/signup',  methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data,
                    role_id=2)
        db.session.add(user)
        db.session.commit()
        token = user.create_confirmation_token()
        send_mail(user.email, '确认你的账户', 'auth/email/confirm', user=user, token=token)
        flash('已发送一封确认邮件')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)


# 确认用户账户
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


# 重新发送账户确认邮件
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.create_confirmation_token()
    send_mail(current_user.email, 'Confirm Your Account',
              'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


# 修改用户密码
@auth.route('/changepassword', methods=['GET', 'POST'])
@login_required
def changepassword():
    form = ChangePassword()
    if form.validate_on_submit():
        if current_user.verify_password(password=form.old_password.data):
            current_user.password = form.new_password.data
            db.session.add(current_user)
            db.session.commit()
            flash('你的密码已更新')
            return redirect(url_for('main.index'))
        else:
            flash('密码无效')
    return render_template('auth/changepassword.html', form=form)


@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            token = user.generate_reset_token()
            send_mail(user.email, 'Reset Your Password',
                       'auth/email/reset_password',
                       user=user, token=token)
            flash('An email with instructions to reset your password has been '
                  'sent to you.')
            return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        if User.reset_password(token, form.password.data):
            db.session.commit()
            flash('Your password has been updated.')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)
