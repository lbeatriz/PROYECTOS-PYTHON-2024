from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludo/<name>')
def saludo(name):
    return '<h2>hola '+name+'</h2>'

@app.route('/saludo1/<name1>/<edad>')
def saludo1(name1,edad):
    return '<h2>Hola '+name1+' tienes '+edad+' años</h2>'
    

app.run(debug=True)