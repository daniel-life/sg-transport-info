from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('home.html')

@app.route('/contacts')
def contacts():
     return render_template('contacts.html')

@app.route('/train_system')
def train_system():
     return render_template('train_system.html')

@app.route('/train_guide')
def train_guide():
     return render_template('train_guide.html')

@app.route('/bus_services')
def bus_services():
     return render_template('bus_services.html')

@app.route('/bus_guide')
def bus_guide():
     return render_template('bus_guide.html')

if __name__ == '__main__':
    app.run()
