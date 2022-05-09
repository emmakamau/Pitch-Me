'''
We define views that will be rendered on our pages

from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review


# Views
@main.route('/')  #route decorator
def index(): #view function

   return render_template('index.html')
'''