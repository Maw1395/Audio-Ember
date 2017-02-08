""" Finds a song in the database """
from app import db, models


def song_search(song_id):
    """ Song search function """
    point = db.session.query(models.songs, models.points).join(models.points).order_by(models.points.points.desc())
    list1 = []
    for i in point:
        if i.songs.SongID == song_id:
            list1.append((i.songs.Title, i.songs.Artist, i.points.points))
            return list1

