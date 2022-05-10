'''
We define views that will be rendered on our pages
'''

from flask import render_template,request,redirect,url_for
from . import main
from .forms import *
from ..models import *


# Views
@main.route('/')
def index(): 
   return render_template('index.html')
