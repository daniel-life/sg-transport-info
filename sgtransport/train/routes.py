from flask import Blueprint, render_template

train = Blueprint('train', __name__)

@train.route('/train_system')
def train_system():
     return render_template('train_system.html')

@train.route('/train_guide')
def train_guide():
     return render_template('train_guide.html')

