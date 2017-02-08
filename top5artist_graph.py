""" Creates a bar graph of the current top 5 artist and songs
    in the database and saves the urls """
import plotly.plotly as py
import plotly.graph_objs as go
from app import db, models
import Config

py.sign_in(Config.user, Config.api_key)
A = db.session.query(models.artist_points).filter(models.artist_points.Artist!="YG" and models.artist_points.Artist!="CL").order_by(models.artist_points.Points.desc()).limit(5).all()
DATA = [go.Bar(
    x=[A[0].Artist, A[1].Artist, A[2].Artist, A[3].Artist, A[4].Artist],
    y=[A[0].Points, A[1].Points, A[2].Points, A[3].Points, A[4].Points],
    )]
"""
link = py.plot(DATA, filename='top5artist', auto_open=False)
u = models.graphs(SongID=-5, URL=link)
db.session.add(u)
db.session.commit()
"""
points_todos = []
SONG_ID = []
POINT = db.session.query(models.songs, models.points).join(models.points).order_by(models.points.Points.desc()).all()
INDEX = 0
for i in POINT:
    if INDEX < 5:
        if i.songs.SongID not in SONG_ID:
            SONG_ID.append(i.songs.SongID)
            points_todos.append((i.songs.Title,i.songs.Artist, i.points.Points, i.points.Genre, i.songs.SongID))
            INDEX += 1
DATA = [go.Bar(
    x=[points_todos[0][0],points_todos[1][0],points_todos[2][0],points_todos[3][0],points_todos[4][0]],
    y=[points_todos[0][2],points_todos[1][2],points_todos[2][2],points_todos[3][2],points_todos[4][2]],
    )]
"""
link = py.plot(DATA, filename='top5songs', auto_open=False)
u = models.graphs(SongID=-4, URL=link)
db.session.add(u)
db.session.commit()
"""

