from datetime import datetime
from flask import render_template, redirect, session, url_for

from . import main
from . import SignForm
from .. import db
from ..models import User

@main.route('/', methods = ['GET', 'POST'])
def index():
    from =