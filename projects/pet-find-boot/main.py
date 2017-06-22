from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sign-in")
def display_index():
    return render_template("sign-in.html")

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

def sign_in():
    return render_template("sign-in.html")

@app.route("/sign-in", methods=["POST"])
def validate_response():

    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    not_valid ="Not valid (Between 3-20 characters and no whitespace)" 
    
    name_error = ''
    pass_error = ''
    pass_error2 = ''
    email_error = ''

    if is_blank(username):
        name_error = "Empty field"
    else:    
        if not is_valid(username):
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
        name = username
        return render_template("welcome.html",
            name = name
        )
    else:
        return render_template("sign-in.html",
            username = username,
            password = password,
            password2 = password2,
            email = email,
            name_error = name_error,
            pass_error = pass_error,
            pass_error2 = pass_error2,
            email_error = email_error
    )             

app.run()    