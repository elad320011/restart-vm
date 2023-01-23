from flask import request,render_template,redirect,Flask
import rebootvm

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'user' and request.form['password'] == 'password'
            resp = redirect('/reboot')
            resp.set_cookie("elko", "cookie")
            return resp

        else:
            error = "invalid credentials"
    return render_template('login.html', error=error)


@app.route('/reboot',methods=['GET', 'POST'])
def home():
    if request.cookies.get("elko") == "cookie":
        reboot_error=None
        if request.method == 'POST':

            success_check = rebootvm.reboot(request.form['id'])
            if success_check == False:
                reboot_error= "Invalid credetials"
            else:
                reboot_error="Success!"
        return render_template('home.html', error=reboot_error)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
