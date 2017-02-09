from flask import Flask, render_template, request
from app import db, models
import top20list
from songpoints import songpoints
from totalpoints import totalpoints
from youtube import youtube_search
import songlist
from artistpoints import artistpoints
from sqlalchemy import func
import plotly.tools as tls
#import dbupdate
#import top5artist_graph
from mylog import log
app = Flask(__name__)

@app.route("/artist", methods=['GET'])
@log("log.txt")
def hello_artist():
    """ Home Page Server Side Artist Search """
    t = db.session.query(models.graphs).filter(models.graphs.SongID == -5).first()
    A = db.session.query(models.artist_points).filter(models.artist_points.Artist != "YG" and models.artist_points.Artist != "CL").order_by(models.artist_points.Points.desc()).limit(5).all()
    return render_template('artist.html',
                           artist_1=A[0].Artist,
                           artist_2=A[1].Artist,
                           artist_3=A[2].Artist,
                           artist_4=A[3].Artist,
                           artist_5=A[4].Artist,
                           list1=top20list.points_todos,
                           t5=tls.get_embed(t.URL)
                          )

@app.route('/artist', methods=['POST'])
@log("log.txt")
def hello_post():
    """ Home Page Server Side Artist Search """
    if request.form['input_artist']:
        Asearch = request.form['input_artist']
        return render_template(
            'artistselected.html',
            B=Asearch,
            list_d1=artistpoints(Asearch),
            points=totalpoints(Asearch)
            )

@app.route("/")
@log("log.txt")
def home_page():
    """ Home Page Song Search """
    t = db.session.query(models.graphs).filter(models.graphs.SongID == -4).first()
    A = db.session.query(models.artist_points).filter(models.artist_points.Artist != "YG" and models.artist_points.Artist != "CL").order_by(models.artist_points.Points.desc()).limit(5).all()
    return render_template(
        'index.html',
        artist_1=A[0].Artist,
        artist_2=A[1].Artist,
        artist_3=A[2].Artist,
        artist_4=A[3].Artist,
        artist_5=A[4].Artist,
        list1=top20list.points_todos,
        t4=tls.get_embed(t.URL)
        )

@app.route("/", methods=['GET', 'POST'])
@log("log.txt")
def hello_home():
    """ Home Page Song Search """
    if request.form['inputName']:
        search = request.form['inputName']
        return render_template(
            'results.html',
            index=0,
            user_query=songpoints(search),
            song=search
            )

@app.route('/', methods=['POST'])
@log("log.txt")
def hello_post2():
    """ Render search results """
    if request.form['inputName']:
        search = request.form['inputName']
        return render_template(
            'results.html',
            index=0,
            user_query=songpoints(search)
            )

@app.route('/list/<Page>')
@log("log.txt")
def list_all(Page):
    """ List top songs """
    max_l = 133*50
    return render_template(
        'list.html',
        p_list=top20list.points_todos,
        lower=int((float(Page)-1)*50),
        upper=int(float(Page)*50),
        Page=int(float(Page)),
        Length=len(top20list.points_todos),
        MaxP=max_l/50+1
        )

@app.route('/list_a/<Page>')
@log("log.txt")
def list_all_artist(Page):
    """ List top artist """
    max_l = 65 * 50 
    return render_template(
        'list_a.html',
        index=0,
        p_list_a=db.session.query(models.artist_points).order_by(models.artist_points.Points.desc()).all(),
        lower=int((float(Page)-1)*50),
        upper=int(float(Page)*50),
        Page=int(float(Page)),
        Length=len(db.session.query(models.artist_points).order_by(models.artist_points.Points.desc()).all()),
        MaxP=max_l/50+1
        )


@app.route('/<Genre>/<Page>')
@log("log.txt")
def list_genre(Genre, Page):
    """ List top songs by genre """
    max_l = len(songlist.songlist(Genre))
    return render_template(
        'genre.html',
        Genre=Genre,
        Page=int(Page),
        lower=(int(Page)-1)*50,
        upper=(int(Page)*50),
        p_list_genre=songlist.songlist(Genre),
        Length=len(songlist.songlist(Genre)),
        MaxP=max_l/50+1
        )


@app.route('/electronic/<Page>')
@log("log.txt")
def list_electronic(Page):
    return render_template(
        'genre.html',
        p_list_genre=songlist.edm,
        Page=int(Page)
        )


@app.route('/SongGraph/<Song>')
@log("log.txt")
def graph_song_selected(Song):
    """ Song page with youtube video and graphs """
    A = db.session.query(models.graphs).filter(models.graphs.SongID == Song).all()
    Title = db.session.query(models.songs).filter(models.songs.SongID == Song).first()
    Artist = Title.Artist
    Title = Title.Title
    D = []
    for song in A:
        D.append(tls.get_embed(song.URL))
    return render_template(
        'song_graph.html',
        B=D,
        Title=Title,
        Artist=Artist,
        URL=youtube_search(Title + Artist),
        )


@app.route('/artistSelected/<Artist>')
@log("log.txt")
def list_artist_selected(Artist):
    """ Artist Page list all songs by artist """
    return render_template(
        'artistselected.html',
        B=Artist,
        list_d1=artistpoints(Artist),
        points=totalpoints(Artist),
        )

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
