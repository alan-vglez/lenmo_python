from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

#Configuracion de MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'AstreqasRibiag_27.'
app.config['MYSQL_DATABASE_DB'] = 'usuario'

mysql.init_app(app)
