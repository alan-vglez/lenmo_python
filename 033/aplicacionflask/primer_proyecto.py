import pymysql
from app import app
from dbconfiguration import mysql
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    conn = None
    cursor = None
    try:
        id = request.form['UsuarioID']
        primer_nombre = request.form['PrimerNombre']
        segundo_nombre = request.form['SegundoNombre']
        nacimiento = request.form['Nacimiento']
        edad = request.form['Edad']
        genero = request.form['Genero']
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (UsuarioID, PrimerNombre, SegundoNombre, Nacimiento, Edad, Genero) VALUES (%s, %s, %s, %s, %s, %s)',
                       (id, primer_nombre, segundo_nombre, nacimiento, edad, genero))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return redirect(url_for('show'))
    
@app.route('/show')
def show():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return render_template('usuarios.html', usuarios = usuarios)
        
if __name__ == '__main__':
    app.run()
