
from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required
from .. import  photos, db
from sqlalchemy import desc
from ..models import User

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''