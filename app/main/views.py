'''
We define views that will be rendered on our pages
'''
from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from flask_login import *
from . import main
from .forms import *
from ..models import *
from .. import db, photos

# Views

# Homepage/Landing page
@main.route('/')
def index(): 
   return render_template('index.html')

# View user profile
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

# Update user profile
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
   user = User.query.filter_by(username = uname).first()
   if user is None:
      abort(404)

   form_update_prof = UpdateProfile()

   if form_update_prof.validate_on_submit():
      user.bio = form_update_prof.bio.data

      db.session.add(user)
      db.session.commit()

      return redirect(url_for('.profile',uname=user.username))
   return render_template('profile/update-profile.html',form_update_prof=form_update_prof)

# Update user profile picture
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.prof_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# Pitch form
@main.route('/<userid>/<uname>/create-pitch', methods=['GET','POST'])
@login_required
def create_pitch(userid,uname):
   user = User.query.filter_by(id=userid).first()
   user_name = User.query.filter_by(username=uname).first()
   print(user)
   create_pitch_form = PitchForm()
   if create_pitch_form.validate_on_submit():
      pitch = create_pitch_form.pitch.data
      category = create_pitch_form.category.data
      new_pitch = Pitch(pitch=pitch,category=category,user_id=userid)
      new_pitch.save_pitch()
      
      return redirect(url_for('.profile',userid=user.id,uname=user_name.username))
   return render_template('create-pitch.html',create_pitch_form=create_pitch_form)
