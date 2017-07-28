from flask import Flask, request, redirect, render_template, session
from model import User, Post
from hashutils import check_pw_hash
from app import app, db
import cgi
import string
app.secret_key = "acubycoarvpv"

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
    if ("@" and "." in resp) and (len(resp) > 3):
        return True
    elif resp == "":
        return True    
    else:
        return False

def strip_str(str):
    new_str = "".join([i for i in str if not i.isdigit()])
    return new_str

@app.before_request
def require_login():
    allowed_routes = ['home_page', 'sign_in', 'search_page', "sign_up"]
    if request.endpoint not in allowed_routes and "username" not in session:
        return redirect("/sign-up")


@app.route("/logout")
def logout():
    del session['username']
    return redirect('/')

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sign-up", methods=["POST","GET"])
def sign_up():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        email = request.form["email"]
        number = request.form['number']
        number = ''.join(n for n in number if n.isdigit())

        not_valid ="Not valid (Between 3-20 characters and no whitespace)" 

        existing_user = User.query.filter_by(username=username).count()
        existing_email = User.query.filter_by(email=email).count()
        
        name_error = ''
        pass_error = ''
        pass_error2 = ''
        email_error = ''
        num_error = ''

        if is_blank(username):
            name_error = "Empty field"
        else:
            if existing_user > 0:
                name_error = "Username already in use."
                username = ""
            elif not is_valid(username):
                name_error = not_valid
                username = ""
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
        if is_blank(email):
            email_error = "Empty Field"
        else:
            if existing_email > 0:
                email_error = "Email already in use."
                email = ""
            elif not valid_email(email):
                email_error = "Not valid email"
                email = ""
        if is_blank(number):
            num_error = "Empty Field"                
        if not name_error and not pass_error and not pass_error2 and not email_error and not num_error:
            user_id = User(username, password, email, number)
            db.session.add(user_id)
            db.session.commit()
            session['username'] = username
            return redirect("/")
        else:
            return render_template("sign-up.html",
                                   username = username,
                                   password=password,
                                   password2=password2,
                                   email=email,
                                   name_error=name_error,
                                   pass_error=pass_error,
                                   pass_error2=pass_error2,
                                   email_error=email_error,
                                   number=number,
                                   num_error=num_error
        ) 
    return render_template("sign-up.html")

@app.route("/sign-in", methods=["POST","GET"])
def sign_in():
    if request.method == "GET":
        return render_template("sign-in.html")    
    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        name_error = ""
        pass_error = ""

        if not user:
            name_error = "Incorrect Username"
            username = ''
        if user and check_pw_hash(password, user.pw_hash):
            session["username"] = username
            return redirect('/')
        else:
            pass_error = "Incorrect Password"
            password = ""
            return render_template("sign-in.html",
                                   name_error=name_error,
                                   pass_error=pass_error,
                                   username=username,
                                   password=password
                                  )

@app.route("/search", methods=["POST","GET"])
def search_page():
    if request.method == "POST":

        #TODO fix the repeats. possible function called clean_form
        species = request.form["species"]
        breed = request.form["breed"]
        color = request.form["color"]
        size = request.form["size"]
        name = request.form["name"]
        city = request.form["city"]
        state = request.form["state"]
        
        species = strip_str(species)
        species = species.upper()

        breed = strip_str(breed)
        breed = breed.upper()

        color = strip_str(color)
        color = color.upper()

        name = strip_str(name)
        name = name.upper()

        city = strip_str(city)
        city = city.upper()

        matches = Post.query.filter_by(state=state).filter_by(species=species).all()

        return render_template("matches.html", matches=matches)


    return render_template("search.html")

@app.route("/post", methods=["POST", "GET"])
def post_page():
    if request.method == "POST":

        owner = User.query.filter_by(username=session['username']).first()

        species = request.form["species"]
        breed = request.form["breed"]
        color = request.form["color"]
        size = request.form["size"]
        name = request.form["name"]
        city = request.form["city"]
        state = request.form["state"]
        
        species = strip_str(species)
        species = species.upper()

        breed = strip_str(breed)
        breed = breed.upper()

        color = strip_str(color)
        color = color.upper()

        name = strip_str(name)
        name = name.upper()

        city = strip_str(city)
        city = city.upper()

        post_id = Post(species, breed ,color, size, name, city, state, owner)
        db.session.add(post_id)
        db.session.commit()

        return redirect("/")

    return render_template("post.html")    

if __name__ == "__main__" :
    app.run()    