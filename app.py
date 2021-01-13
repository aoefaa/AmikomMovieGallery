from flask import Flask, render_template, url_for, request, session, make_response
from flask_mysqldb import MySQL
import datetime

#------------------------------MySQLdb------------------------------

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '0411_dbMovies'
mysql = MySQL(app)

#------------------------------Routing------------------------------

@app.route('/')
def home():
    imgMovies = getAllImage()
    movieIndex = len(getAllIndex())
    return render_template('home.html',
                            page='home',
                            title='Home',
                            imgMovies=imgMovies,
                            movieIndex=movieIndex)

@app.route('/movieList')
def movieList():
    movieTitle = getAllTitle()
    movieDesc = getAllDesc()
    movieIndex = len(getAllIndex())
    moviePoster = getAllPoster()
    movieId = getAllId()
    if 'view' in request.args:
        movie_id = request.args['view']

        moviePosterById = getPosterById(movie_id)
        movieTitleById = getTitleById(movie_id)
        # movieRatingById = getRatingbyId(movie_id)
        movieLengthById = getLengthById(movie_id)
        moviePremiereById = getPremiereById(movie_id)
        movieCategoryById = getCategoryById(movie_id)
        movieDirectorsById = getDirectorsById(movie_id)
        movieWritersById = getWritersById(movie_id)
        movieStarsById = getStarsById(movie_id)
        movieDescById = getDescById(movie_id)

        return render_template('movieDetail.html',
                                title='Movie Detail', 
                                movieTitleById=movieTitleById,
                                moviePosterById=moviePosterById,
                                # movieRatingById=movieRatingById,
                                movieLengthById=movieLengthById,
                                moviePremiereById=moviePremiereById,
                                movieCategoryById=movieCategoryById,
                                movieDirectorsById=movieDirectorsById,
                                movieWritersById=movieWritersById,
                                movieStarsById=movieStarsById,
                                movieDescById=movieDescById)

    return render_template('movieList.html',
                            page='movieList',
                            title='Movie List',
                            movieIndex=movieIndex,
                            movieTitle=movieTitle,
                            movieDesc=movieDesc,
                            moviePoster=moviePoster,
                            movieId=movieId)

@app.route('/<filename>')
def getImage(filename):
    if filename is None:
        not_found(404)
    return not_found(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(render_template('error.html', title='Error 404'), 404)

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

def getAllId():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM movies")
    item = cur.fetchall()
    data = []
    for i in item:
        j = str(i).replace(',)', '').replace('(', '')
        data.append(j)
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
            data.append('no-image-big.png')
    item = ['static/image/' + image for image in data]
    return item

#------------------------------Get By Id Function------------------------------

def getPosterById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT poster FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    try:
        data = ''.join(item)
    except:
        data = 'no_image.png'
    poster = 'image/' + data
    return poster

def getTitleById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT title FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    title = ''.join(item)
    return title

def getRatingbyId(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT rating FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    rating = ''.join(item)
    return rating

def getLengthById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT length FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    for i in item:
        length = str(i).replace(',)', '').replace('(', '')
    return length

def getPremiereById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT premiere FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    try:
        premiere = str(datetime.datetime.strptime(
        str(item)
        .replace('(datetime.date(', '')
        .replace('),)', ''), '%Y, %m, %d')
        )[:-9]
    except:
        premiere = '-'
    return premiere

def getCategoryById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT genre FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    category = ''.join(item)
    return category

def getDirectorsById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT directors FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    try :
        directors = ''.join(item)
    except:
        directors = '-'
    return directors

def getWritersById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT writers FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    try :
        writers = ''.join(item)
    except:
        writers = '-'
    return writers

def getStarsById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT stars FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    try :
        stars = ''.join(item)
    except:
        stars = '-'
    return stars

def getDescById(uid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT resume FROM movies WHERE id = '{0}'".format(uid))
    item = cur.fetchone()
    resume = ''.join(item)
    return resume

#------------------------------Main------------------------------

if __name__ == "__main__":
    app.run(debug=True)
    
