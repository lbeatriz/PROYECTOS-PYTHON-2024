from flask import Flask, render_template #Es para importar flask

app = Flask(__name__) #creamos una instancia de flask en una variable llamada app(se puede llamar como sea)

@app.route('/')#usamos un decorador(@) para crear una respuesta a la ruta / que es el index o página principal
def Hola(): #creamos la función que va a responder al llamado a  la ruta /
    return '<h1>Hola mundo</h1>' #es lo que devuelve la función es este caso solo un texto (hola mundo)
@app.route('/plantilla')
def plantilla():
    data={
        'titulo':'Página plantilla',
        'mensaje':'Hola'
    } #Declaración de diccionario
    return render_template('pagina1.html',data=data) #render_template es para renderizar la plantilla
app.run(debug=True) #es para correr la aplicación o sea nuestro sitio web en el servidor virtual
    
    
    #recuerda que para verlo solo debemos entrar a la dirección 127.0.0.1:5000 en cualquier navegador
    #es importante crear la carpeta templates porque ahi va flask a intentar buscar el archivo de la plantilla.