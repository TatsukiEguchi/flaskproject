from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from apps.app import db, login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    username = db.Column(
        db.String(30),
        index=True,
        nullable=False
    )
    email = db.Column(
        db.String,
        index=True,
        unique=True,
        nullable=False
    )
    password_hash = db.Column(
        db.String,
        nullable=False
    )
    create_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

    @property
    def password(self):
        raise AttributeError('password is not a readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)