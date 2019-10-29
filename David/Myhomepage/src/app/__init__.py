from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS

mail = Mail()
cors = CORS()
db = SQLAlchemy()