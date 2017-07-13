from flask import Flask, request, redirect, render_template, session
from model import User, Post
from hashutils import check_pw_hash
from app import app, db
import cgi
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

        not_valid ="Not valid (Between 3-20 characters and no whitespace)" 

        existing_user = User.query.filter_by(username=username).first()

        name_error = ''
        pass_error = ''
        pass_error2 = ''
        email_error = ''

        if is_blank(username):
            name_error = "Empty field"
        else:
            if username == existing_user:
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
        if not valid_email(email):
                email_error = "Not valid email"
                email = ""        
        if not name_error and not pass_error and not pass_error2 and not email_error:
            user_id = User(username, email, password)
            db.session.add(user_id)
            db.session.commit()
            session['username'] = username
            return redirect("/")
        else:
            return render_template("sign-up.html",
                username = username,
                password = password,
                password2 = password2,
                email = email,
                name_error = name_error,
                pass_error = pass_error,
                pass_error2 = pass_error2,
                email_error = email_error
        ) 
    return render_template("sign-up.html")

@app.route("/sign-in")
def sign_in():
    if request.method == "GET":
        return render_template("sign-in.html")    
    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_pw_hash(password, user.pw_hash):
            session["username"] = username
            return redirect('/')
        else:
            # TODO - Need to fix error checks so that they are individual
            name_error = "Incorrect username or password"
            pass_error = "Incorrect username or password"
            username = ""
            password = ''
            return render_template("sign-in.html",
                            name_error = name-error,
                            pass_error = pass_error,
                            username = username,
                            password = password
        )


@app.route("/search")
def search_page():
    return render_template("search.html")

@app.route("/post")
def post_page():
    return render_template("post.html")    

if __name__ == "__main__" :
    app.run()    