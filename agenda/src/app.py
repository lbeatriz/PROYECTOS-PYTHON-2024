from flask import Flask,render_template,request,redirect,url_for,session
import config
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_USER"]= config.MYSQL_USER
app.config["MYSQL_DB"]= config.MYSQL_DB
app.config["MYSQL_PASSWORD"]= config.MYSQL_PASSWORD
app.config['SECRET_KEY'] = config.HEX_SEC_KEY

mysql= MySQL(app)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods= ["POST"])
def login():
    email= request.form["email"]
    password= request.form["password"]
    cur=mysql.connection.cursor()
    cur.execute("select * from users where email= %s and password=%s", (email,password))
    user=cur.fetchone()
    cur.close()
    if user is not None:
        session['email'] = email
        session['name'] = user[1]
        session['surnames'] = user[2]

        return redirect(url_for('tasks'))
    else:
        return render_template('login.html', message="Email o contraseña incorrectos")

@app.route("/tasks")
def tasks ():
    return render_template('tasks.html')

if __name__ =='__main__':
    app.run(debug=True)

