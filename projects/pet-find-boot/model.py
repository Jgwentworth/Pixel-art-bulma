from app import db
from hashutils import make_pw_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    pw_hash = db.Column(db.String(255))
    posts = db.relationship("Post", backref="owner")
    

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.pw_hash = make_pw_hash(password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(120))
    breed = db.Column(db.String(120))
    color = db.Column(db.String(120))
    size = db.Column(db.String(120))
    name = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))        

    def __init__(self, species, breed, color, size, name, owner ):
        self.species = species
        self.breed = breed
        self.color = color
        self.size = size
        self.name = name
        self.owner = owner
