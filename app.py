from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db
from route import create_routes
# Initialize Flask app
app = Flask(__name__)

# Configure the app with SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'  # or your chosen DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration support
db.init_app(app)

migrate = Migrate(app, db)

create_routes(app)



if __name__ == '__main__':
    app.run( debug=True)
