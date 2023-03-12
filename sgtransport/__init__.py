from flask import Flask

def create_app():
    app = Flask(__name__)

    from sgtransport.main.routes import main
    from sgtransport.bus.routes import bus
    from sgtransport.train.routes import train
    from sgtransport.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(bus)
    app.register_blueprint(train)
    app.register_blueprint(errors)

    return app

   


