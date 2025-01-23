from flask import Flask,session
# from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_frozen import Freezer
import os

load_dotenv()
HOST=os.getenv("host")
PORT=os.getenv("port")
DATABASE=os.getenv("database")
USER=os.getenv("user")
SECRET_KEY=os.getenv("secret_key")
POOL_MODE=os.getenv("pool_mode")
PASSWORD=os.getenv("password")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
log_manage = LoginManager(app)
freezer = Freezer(app)

from routes import *

if __name__ == '__main__':
    app.run()