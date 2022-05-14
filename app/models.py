'''
Define and initialize classes for our objects
'''

from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(600),index=True)
    prof_pic = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='user',lazy ='dynamic')
    comments = db.relationship('Comment',backref='user',lazy ='dynamic')
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
        return f'User{self.comment}'

class Pitch(db.Model):
    #Pitches - id,pitch,upvote,downvote,user,category
    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.String(300))
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    upvotes = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    comment_id =  db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.all()
        return pitches

    @classmethod
    def get_all_pitches_user(cls,id):
        pitches = Pitch.query.filter_by(user_id=id)
        return pitches

    @classmethod
    def get_all_pitches_category(cls,category):
        pitches = Pitch.query.filter_by(category=category)
        return pitches

    def __refr__(self):
        return f'User{self.id}'
   
class Upvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()
        
    def upvote(self, id):
        upvote_pitch = Upvote(user=current_user, pitch_id=id)
        upvote_pitch.save_upvote()
        
    @classmethod
    def get_upvote(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote
    
    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

class Downvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    downvotes = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    def save_downvote(self):
        db.session.add(self)
        db.session.commit()
    
    def downvote(self, id):
        downvote_pitch = Downvote(user=current_user, pitch_id=id)
        downvote_pitch.save_downvote()
        
    @classmethod
    def get_downvote(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote
    
    @classmethod
    def all_downvotes(cls):
        downvotes = Downvote.query.order_by('id').all()
        return downvotes


