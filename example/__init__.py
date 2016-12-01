from flask import Flask
from flask_mysqldb import MySQL
from MySQLdb import OperationalError

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
    try: 
        conn = mysql.connection
    except OperationalError, e:
        return "Error connecting to database! {0}".format(e)

    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS counter (id INT NOT NULL PRIMARY KEY, count INT NOT NULL)''')

    cur.execute('''SELECT COUNT(id) from counter''')
    count = cur.fetchone()
    if int(count[0]) == 0:
      cur.execute('''INSERT INTO counter (id,count) VALUES (0,0)''')
      conn.commit()

    cur.execute('''UPDATE counter SET count = count + 1''')
    conn.commit()

    cur.execute('''SELECT count FROM counter''')
    hits = cur.fetchone()
    return "Hits: {0}".format(int(hits[0]))

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
