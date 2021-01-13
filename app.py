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
    cur = mysql.connection.cursor()
    cur.execute("SELECT image FROM movies")
    imgList = cur.fetchall()
    image = []
    for i in imgList:
        try:
            image.append(''.join(i))
        except:
            image.append('NULL DATA')
    imgMovies = ['static/image/' + image for image in image]
    return render_template('home.html', page='home', title='Home', imgMovies=imgMovies)

def getDesc():
    cur = mysql.connection.cursor()
    cur.execute("SELECT resume FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(''.join(i))
    return data

def getPoster():
    cur = mysql.connection.cursor()
    cur.execute("SELECT poster FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        try:
            data.append(''.join(i))
        except:
            data.append('NULL DATA')
    item = ['static/image/' + poster for poster in data]
    return item

def getTitle():
    cur = mysql.connection.cursor()
    cur.execute("SELECT title FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(''.join(i))
    return data

def getIndex():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(i)
    return data

@app.route('/movieList')
def movieList():
    movieTitle = getTitle()
    movieDesc = getDesc()
    movieIndex = len(getIndex())
    moviePoster = getPoster()
    return render_template('movieList.html', page='movieList', title='Movie List', movieIndex=movieIndex, movieTitle=movieTitle, movieDesc=movieDesc, moviePoster=moviePoster)

@app.route('/<filename>')
def getImage(filename):
    fullpath = "/static/image/" + filename
    resp = open(fullpath).read()
    return resp

if __name__ == "__main__":
    app.run(debug=True)