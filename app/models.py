from . import db
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import desc
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    pitches = db.relationship("Pitch", backref="user", lazy="dynamic")
    comment = db.relationship("Comment", backref="user", lazy="dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    liked = db.relationship('PitchLike', foreign_keys='PitchLike.user_id', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'
        
    def like_pitch(self, pitch):
        if not self.has_liked_pitch(pitch):
            like = PitchLike(user_id=self.id, pitch_id=pitch.id)
            db.session.add(like)

    def unlike_pitch(self, pitch):
        if self.has_liked_pitch(pitch):
            PitchLike.query.filter_by(user_id = self.id, pitch_id = pitch.id).delete()

    def has_liked_pitch(self, pitch):
        return PitchLike.query.filter(PitchLike.user_id == self.id, PitchLike.pitch_id == pitch.id).count() > 0 

# class Category(db.Model):
#     __tablename__ = "categories"

#     id = db.Column(db.Integer, primary_key=True)
#     category = db.Column(db.String(255))
#     name = db.Column(db.String(255))

#     pitches = db.relationship('Pitch', backref='category', lazy='dynamic')

#     def __repr__(self):
#         return self.id

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    pitch = db.Column(db.String) 
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    pitch_category = db.Column(db.String)
    comments = db.relationship('Comment', backref='pitch', lazy="dynamic")
    likes = db.relationship('PitchLike', backref='pitch', lazy='dynamic')
     
   
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, pitch_category):
        pitches = Pitch.query.filter_by(pitch_category=pitch_category).all()
        return pitches
    @classmethod
    def getPitchId(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch
    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    @classmethod
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id)
        return comments
        
class PitchLike(db.Model):
    __tablename__ = 'pitch_likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
