from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config.update(
    MYSQL_HOST='mysql',
    MYSQL_USER='user',
    MYSQL_PASSWORD='password',
    MYSQL_DB='database'
)

mysql = MySQL(app)

@app.route('/read_db_users')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
