import pymysql
import pymysql.cursors
from app import app
from dbconfiguration import mysql
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    conn = None
    cursor = None
    try:
        id_usuario = request.form['UsuarioID']
        primer_nombre = request.form['PrimerNombre']
        segundo_nombre = request.form['SegundoNombre']
        nacimiento = request.form['Nacimiento']
        edad = request.form['Edad']
        genero = request.form['Genero']
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (UsuarioID, PrimerNombre, SegundoNombre, Nacimiento, Edad, Genero) VALUES (%s, %s, %s, %s, %s, %s)',
                      (id_usuario, primer_nombre, segundo_nombre, nacimiento, edad, genero))
        conn.commit()       
        flash("Usuario agregado correctamente!")
    except Exception as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        return redirect(url_for('show'))
    
@app.route('/show')
def show():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        return render_template('usuarios.html', usuarios = usuarios)
    except Exception as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
@app.route('/eliminar')
def eliminar():
    return render_template('eliminar.html')
        
@app.route('/delete', methods = ['POST'])
def delete():
    conn = None
    cursor = None
    try:
        id_usuario = request.form['UsuarioID']
        
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('DELETE FROM usuarios WHERE UsuarioID = %s', (id_usuario))
        conn.commit()
        
        eliminacion = cursor.rowcount()
        if eliminacion == 0: flash("No existe el usuario!")
        else: flash("Usuario eliminado!")
    except Exception as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        print("Eliminado exitosamente!")
        return redirect(url_for('show'))

    
@app.route('/actualizar')
def actualizar():
    return render_template('actualizar.html')

@app.route('/update', methods = ['POST'])
def update():
    conn = None
    cursor = None
    try:
        id_usuario = request.form['UsuarioID']
        primer_nombre = request.form['PrimerNombre']
        segundo_nombre = request.form['SegundoNombre']
        nacimiento = request.form['Nacimiento']
        edad = request.form['Edad']
        genero = request.form['Genero']
        
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('UPDATE usuarios SET PrimerNombre = %s, SegundoNombre = %s, Nacimiento = %s, Edad = %s, Genero = %s WHERE UsuarioID = %s',
                      (primer_nombre, segundo_nombre, nacimiento, edad, genero, id_usuario))
        conn.commit()
        
        actualizacion = cursor.rowcount()
        if actualizacion == 0: flash("No existe el usuario!")
        else: flash("Usuario actualizado!")
    except Exception as e:
        print(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        print("Actualizado correctamente!")
        return redirect(url_for('show'))
            
if __name__ == '__main__':
    app.debug = True
    app.run()
