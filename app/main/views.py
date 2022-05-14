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
   title = 'Pitch Me'
   return render_template('index.html',title=title)

# View user profile
@main.route('/user/<userid>/<uname>')
def profile(userid,uname):
   user = User.query.filter_by(username = uname).first()
   title='User Profile'
   pitches = Pitch.get_all_pitches_user(userid)
   if user is None:
      abort(404)
   return render_template("profile/profile.html", title = title, pitches=pitches,user=user)

# Update user profile
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
   title='Update Profile'
   user = User.query.filter_by(username = uname).first()
   if user is None:
      abort(404)

   form_update_prof = UpdateProfile()

   if form_update_prof.validate_on_submit():
      user.bio = form_update_prof.bio.data

      db.session.add(user)
      db.session.commit()

      return redirect(url_for('.profile',uname=user.username))
   return render_template('profile/update-profile.html',form_update_prof=form_update_prof,title=title)

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
   title='New Pitch'
   user = User.query.filter_by(id=userid).first()
   user_name = User.query.filter_by(username=uname).first()
   create_pitch_form = PitchForm()
   if create_pitch_form.validate_on_submit():
      pitch = create_pitch_form.pitch.data
      category = create_pitch_form.category.data
      new_pitch = Pitch(pitch=pitch,category=category,user_id=userid)
      new_pitch.save_pitch()
      
      return redirect(url_for('.profile',userid=user.id,uname=user_name.username))
   return render_template('create-pitch.html',create_pitch_form=create_pitch_form,title=title)

# Upvote
@main.route('/upvotes/<int:id>', methods=['GET', 'POST'])
@login_required
def upvote(id):
   pitch = Pitch.query.get(id)
   new_vote = Upvote(pitch = pitch, upvote = 1, user_id = current_user.id)
   new_vote.save_upvote()
   return redirect('/pitch/comments/{pitch_id}'.format(pitch_id=id))

# Downvote
@main.route('/downvotes/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
   pitch = Pitch.query.get(id)
   new_downvote = Downvote(pitch = pitch,downvote = 1, user_id=current_user.id)
   new_downvote.save_downvote()
   return redirect('/pitch/comments/{pitch_id}'.format(pitch_id=id))

# Add Comment for particular pitch
@main.route('/add/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def add_comment(id):
   title='Add Comment'
   comment_form = CommentForm()
   pitch = Pitch.query.get(id)
   user = User.query.get(id)
   
   if comment_form.validate_on_submit():
      new_comment = Comment(comment=comment_form.comment.data, pitch_id=id, user_id=current_user.id)
      new_comment.save_comment()
      return redirect('/pitch/comments/{pitch_id}'.format(pitch_id=id))
   return render_template('add-comment.html', comment_form=comment_form, pitch=pitch, user=user,title=title)

# Display comments for a pitch
@main.route('/pitch/comments/<int:id>')
def display_comments(id):
   title='Comments'
   pitch = Pitch.query.get(id)
   comments = Comment.get_comment(id)
   return render_template('display-comments.html',pitch=pitch,comments=comments,title=title)


# Display pitches of Tech category
@main.route('/category/<category>')
def tech_pitches(category):
   tech_pitches= Pitch.get_all_pitches_category(category)
   title='Category'
   return render_template('category/tech-pitch.html',tech_pitches=tech_pitches,title=title)

# Display pitches of Sales category
@main.route('/category/<category>')
def sales_pitches(category):
   sales_pitches= Pitch.get_all_pitches_category(category)
   title='Category'
   return render_template('category/sales-pitch.html',sales_pitches=sales_pitches,title=title)

# Display pitches of Marketing category
@main.route('/category/<category>')
def marketing_pitches(category):
   marketing_pitches= Pitch.get_all_pitches_category(category)
   title='Category'
   return render_template('category/marketing-pitch.html',marketing_pitches=marketing_pitches,title=title)