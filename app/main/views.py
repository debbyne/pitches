
from flask import render_template,redirect,url_for

from app.main.forms import PitchForm
from . import main
from flask_login import current_user, login_required
from .. import  photos, db
from sqlalchemy import desc
from ..models import User,Category,Pitch

@main.route('/',methods = ['GET', 'POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.get_pitches()
    form = PitchForm()
    title = 'Home | Pitcher'
    form.category.query = Category.query
    if form.validate_on_submit():
        selected_category = form.category.data
        pitch = form.pitch.data
        new_pitch = Pitch(pitch = pitch, user = current_user, category=selected_category)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    

    return render_template('pitches.html', title = title, form=form, pitches = pitches)