from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Create the SQLAlchemy db instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    with app.app_context():
        # Import models
        # from models import User

        # Create the database tables
        db.create_all()

    return app

# Define routes
app = create_app()


# signup routes
@app.route("/signup")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
	app.run(debug= True)
