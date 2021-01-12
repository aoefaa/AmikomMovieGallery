from flask import Flask, render_template, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '0411_dbMovies'
mysql = MySQL(app)

@app.route('/')
def home():
    print(request.args)
    cur = mysql.connection.cursor()
    cur.execute("SELECT image FROM movies where id = 1")
    imgMovie = cur.fetchall()
    cur.close()
    print(imgMovie)
    return render_template('home.html', page='home', title='Home', imgMovie='img_movie')

@app.route('/movieList')
def movieList():
    cur = mysql.connection.cursor()
    cur.execute("SELECT image FROM movies WHERE")
    image = cur.fetchall()
    cur.close()
    print(request.args)
    return render_template('movieList.html', page='movieList', title='Movie List', txName='tx_name')

if __name__ == "__main__":
    app.run(debug=True)