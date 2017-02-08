""" Returns a list of the top scoring songs in the database """
from app import db, models

points_todos = []
SONG_ID = []
POINT = db.session.query(models.songs, models.points).join(models.points).order_by(models.points.Points.desc()).all()
INDEX = 0
for i in POINT:
    if i.songs.SongID not in SONG_ID:
        SONG_ID.append(i.songs.SongID)
        points_todos.append((i.songs.Title, i.songs.Artist, i.points.Points, i.points.Genre, i.songs.SongID))
        INDEX += 1

