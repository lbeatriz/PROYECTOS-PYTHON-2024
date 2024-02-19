from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludo/<name>')
def saludo(name):
    return render_template('saludo.html',nombre=name)

@app.route('/saludo1/<name1>/<edad>')
def saludo1(name1,edad):
    return render_template('saludo1.html',nombre=name1,edad=edad)
   
    

app.run(debug=True)