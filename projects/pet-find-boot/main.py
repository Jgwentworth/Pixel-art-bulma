from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://pet-find-boot:fhyBwcgZHHGiMj53@localhost:8889/pet-find-boot"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sign-up")
def display_index():
    return render_template("sign-up.html")

def is_blank(resp):
    if len(resp) == 0:
        return True
    else:
        return False

def is_valid(resp):
    if " " in resp:
        return False
    elif (len(resp) < 3) or (len(resp) > 20):
        return False
    else:
        return True

def valid_email(resp):
    if ("@" and "." in resp) and (len(resp) > 3) and (len(resp) < 20):
        return True
    elif resp == "":
        return True    
    else:
        return False

def sign_up():
    return render_template("sign-up.html")

@app.route("/sign-up", methods=["POST"])
def validate_response():

    name = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    not_valid ="Not valid (Between 3-20 characters and no whitespace)" 
    
    name_error = ''
    pass_error = ''
    pass_error2 = ''
    email_error = ''

    if is_blank(name):
        name_error = "Empty field"
    else:    
        if not is_valid(name):
            name_error = not_valid
            name = ""
    if is_blank(password):
        pass_error = "Empty field"
    else:
        if not is_valid(password):
            pass_error = not_valid
            password =""
    if is_blank(password2):
        pass_error2 ="Empty field"
    else:
        if not is_valid(password2):
            pass_error2 = not_valid
            password2 = ""      
        elif password != password2:
            pass_error2 = "Not matching"
            password2 = ""
    if not valid_email(email):
            email_error = "Not valid email"
            email = ""        
    if not name_error and not pass_error and not pass_error2 and not email_error:
        user_id = User(name, email, password)
        db.session.add(user_id)
        db.session.commit()
        session['username'] = name
        return redirect("/")
    else:
        return render_template("sign-up.html",
            username = name,
            password = password,
            password2 = password2,
            email = email,
            name_error = name_error,
            pass_error = pass_error,
            pass_error2 = pass_error2,
            email_error = email_error
    )  
@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")    

@app.route("/search")
def search_page():
    return render_template("search.html")

@app.route("/post")
def post_page():
    return render_template("post.html")    

if __name__ == "__main__" :
    app.run()    