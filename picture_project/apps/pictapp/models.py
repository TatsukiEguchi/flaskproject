from datetime import datetime
from apps.app import db

class UserPicture(db.Model):
    __tablename__ = "pictures"

    id = db.Column(
		db.Integer,         
        primary_key=True,   
        autoincrement=True) 
    
    user_id = db.Column(
        db.String,          
        db.ForeignKey('users.id'))
    
    username = db.Column(
        db.String,         
        index=True)        

    title = db.Column(
        db.String)         
    
    contents = db.Column(
        db.Text)            

    image_path = db.Column(
        db.String)         

    create_at = db.Column(
        db.DateTime,          
        default=datetime.now) 
    
