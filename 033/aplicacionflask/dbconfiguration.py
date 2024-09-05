from app import app
from flaskext.mysql import MySQL

#Configuracion de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AstreqasRibiag_27.'
app.config['MYSQL_DB'] = 'usuario'

mysql = MySQL()
mysql.init_app(app)
