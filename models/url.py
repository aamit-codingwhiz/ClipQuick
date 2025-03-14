from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import string, random
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class ShortURL(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True
    )
    original_url = db.Column(
        db.String(500),
        nullable=False
    )
    short_code = db.Column(
        db.String(6),
        unique=True,
        nullable=False
    )
    password_hash = db.Column(
        db.String(200), 
        nullable=True
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)

    @staticmethod
    def generate_short_code():
        return "".join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6
            )
        )
    
    @staticmethod
    def set_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")
    
    @staticmethod
    def check_password(url, password):
        return bcrypt.check_password_hash(
            pw_hash=url.password_hash, 
            password=password
        )