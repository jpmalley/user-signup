from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

def valid_username(username):
    error = "That's not a valid username"
    if username.count(' ') > 0:
        return error
    elif len(username.strip()) < 3 or len(username.strip()) > 20:
        return error
    else:
        return ''

def valid_password(password):
    error = "That's not a valid password"
    if password.count(' ') > 0:
        return error
    elif len(password.strip()) < 3 or len(password.strip()) > 20:
        return error
    else:
        return ''

def verify_password(password, verify):
    error = "Passwords do not match"
    if password == verify:
        return ''
    else:
        return error

def valid_email(email):
    email = email.strip()
    error = "Thats not a valid email"
    if not email:
        return ''
    else:
        if email.count(' ') > 0:
            return error
        elif email.count('@') == 1 and email.count('.') == 1 and (len(email) > 3 and len(email) < 20):
            return ''
        else:
            return error


@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        user_error = valid_username(username)
        pw_error = valid_password(password)
        verify_error = verify_password(password, verify)
        email_error = valid_email(email)

        if not user_error and not pw_error and not verify_error and not email_error:
            return redirect("/welcome?username=" + username)
        else:
            return render_template('signup.html', username=username, user_error=user_error, password='', pw_error=pw_error, verify='', verify_error=verify_error, email=email, email_error=email_error)
    
    return render_template('signup.html')

@app.route("/welcome")
def welcome():
    username = request.args.get("username")

    return render_template('welcome.html', username=username)

app.run()