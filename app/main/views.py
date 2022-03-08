from ..models import User
from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required
from .. import db