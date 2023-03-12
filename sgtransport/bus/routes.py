from flask import Blueprint, render_template

bus = Blueprint('bus', __name__)

@bus.route('/bus_services')
def bus_services():
     return render_template('bus_services.html')

@bus.route('/bus_guide')
def bus_guide():
     return render_template('bus_guide.html')

