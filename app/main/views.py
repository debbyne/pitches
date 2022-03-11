
from unicodedata import category
from flask import render_template,redirect,url_for,abort

from app.main.forms import CommentForm, PitchForm,UpdateProfile
from . import main
from flask_login import current_user, login_required
from .. import  photos, db
from sqlalchemy import desc
from ..models import Comment, User,Pitch



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pick_up_lines = Pitch.query.filter_by(pitch_category = 'Pick Up line').all()
    interview_pitch = Pitch.query.filter_by(pitch_category = 'Interview Pitch').all()
    product_pitch = Pitch.query.filter_by(pitch_category = 'Product Pitch').all()
    pitches = Pitch.query.all()
    
    return render_template('index.html', pick_up_lines = pick_up_lines, interview_pitch = interview_pitch ,  product_pitch =   product_pitch )

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/pitch/new',methods = ['GET', 'POST'])
def newpitch():

    '''
    View root page function that returns the index page and its data
    '''
    form = PitchForm()
    if form.validate_on_submit():
        selected_category = form.category.data
        pitch = form.pitch.data
        title = form.title.data
        new_pitch = Pitch(pitch = pitch, title = title, user = current_user, pitch_category=selected_category)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
        
    return render_template('pitches.html', form=form)

@main.route('/allpitches/', methods = ['GET' ,'POST'])
def allpitches():
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(id = Pitch.id).first()
    user = User.query.filter_by(id = Pitch.user_id).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment= comment , user = current_user, pitch_id = pitch.id)
        new_comment.save_comment()

    return render_template('allpitches.html' , pitches = pitches , CommentForm = form)


