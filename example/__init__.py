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

@app.route('/counter')
def users():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS counter (id INT NOT NULL PRIMARY KEY, count INT NOT NULL)''')
    cur.execute('''UPDATE counter SET count = count + 1''')
    conn.commit()

    cur.execute('''SELECT count FROM counter''')
    rv = cur.fetchall()
    return str(rv)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
