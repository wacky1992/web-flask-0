from datetime import datetime
from flask import render_template, redirect, session, url_for, current_app

from . import main
from .form import SignForm
from .. import db
from ..models import User
from ..email import send_mail


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SignForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_mail(main.config['FLASKY_ADMIN'], '新用户',
                          'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
