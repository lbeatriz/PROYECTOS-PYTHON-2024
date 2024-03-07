from flask import Flask,render_template,request,redirect,url_for
import config
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_USER"]= config.MYSQL_USER
app.config["MYSQL_DB"]= config.MYSQL_DB
app.config["MYSQL_PASSWORD"]= config.MYSQL_PASSWORD

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
        return redirect(url_for("tasks"))
    return render_template('login.html')

@app.route("/tasks")
def tasks ():
    return "Usuario Valido"

if __name__ =='__main__':
    app.run(debug=True)

