from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    correo = request.form['email']
    password = request.form['password']
    return render_template('index.html',correo=correo,password=password)

@app.route('/saludo/<name>')
def saludo(name):
    return render_template('saludo.html',nombre=name)

@app.route('/saludo1/<name1>/<edad>')
def saludo1(name1,edad):
    return render_template('saludo1.html',nombre=name1,edad=edad)

@app.route('/login')
def login():
    
    return render_template('login.html')
   
    

app.run(debug=True)