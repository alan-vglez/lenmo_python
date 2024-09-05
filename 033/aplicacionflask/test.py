import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='AstreqasRibiag_27.',
        database='usuario'
    )
    print("Conneccion exitosa.")
except Exception as e:
    print(f"Error: {e}")
