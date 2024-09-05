from app import app
from flask import MySQL

#Configuracion de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AstreqasRibiag_27.'
app.config['MYSQL_DB'] = 'usuario'

mysql = MySQL()
mysql.innit_app(app)
