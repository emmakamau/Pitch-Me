'''
Define and initialize classes for our objects
'''

from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(600),index=True)
    prof_pic = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='user',lazy ='dynamic')
    password_hash = (db.String(30))

    pass_secure=db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('Password attribute is not readable')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __refr__(self):
        return f'User{self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),index=True,unique=True)

    def __refr__(self):
        return f'User{self.name}'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    def __refr__(self):
        return f'User{self.id}'

class Pitch(db.Model):
    #Pitches - id,pitch,upvote,downvote,user,category
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(300))
    upvote = db.Column(db.Integer)
    downote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    category = db.Column(db.Integer,db.ForeignKey('category.id'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.all()
        return pitches

    def __refr__(self):
        return f'User{self.id}'
   
