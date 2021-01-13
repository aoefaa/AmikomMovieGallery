from flask import Flask, render_template, url_for, request, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '0411_dbMovies'
mysql = MySQL(app)

@app.route('/')
def home():
    imgMovies = getAllImage()
    movieIndex = len(getAllIndex())
    return render_template('home.html', page='home', title='Home', imgMovies=imgMovies, movieIndex=movieIndex)

@app.route('/movieList')
def movieList():
    movieTitle = getAllTitle()
    movieDesc = getAllDesc()
    movieIndex = len(getAllIndex())
    moviePoster = getAllPoster()
    movieId = len(getAllIndex())

    if 'view' in request.args:
        movie_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM movies WHERE id=%s", (movie_id,))
        movie = curso.fetchall()
        x = content_based_filtering(movie_id)
        wrappered = wrappers(content_based_filtering, movie_id)
        execution_time = timeit.timeit(wrappered, number=0)
        # print('Execution time: ' + str(execution_time) + ' usec')
        if 'uid' in session:
            uid = session['uid']
            # Create cursor
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM movies WHERE id=%s", (uid))
            result = cur.fetchall()
            print(uid)
        return render_template('movieDetail.html', title='Movie Detail')

    return render_template('movieList.html',page='movieList', title='Movie List', movieIndex=movieIndex, movieTitle=movieTitle, movieDesc=movieDesc, moviePoster=moviePoster, movieId=movieId)

#------------------------------Get All Function------------------------------
    
def getAllDesc():
    cur = mysql.connection.cursor()
    cur.execute("SELECT resume FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(''.join(i))
    return data

def getAllPoster():
    cur = mysql.connection.cursor()
    cur.execute("SELECT poster FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        try:
            data.append(''.join(i))
        except:
            data.append('no_image.png')
    item = ['image/' + poster for poster in data]
    return item

def getAllTitle():
    cur = mysql.connection.cursor()
    cur.execute("SELECT title FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(''.join(i))
    return data

def getAllIndex():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(i)
    return data


def getAllImage():
    cur = mysql.connection.cursor()
    cur.execute("SELECT image FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        try:
            data.append(''.join(i))
        except:
            data.append('no_image.png')
    item = ['image/' + image for image in data]
    return item

#------------------------------Get By Id Function------------------------------

def getTitleById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT title FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchall()
    data = []
    for i in item:
        data.append(i)
	return item

if __name__ == "__main__":
    app.run(debug=True)
    
