""" Returns the points for a certain song  """
from app import db, models
from sqlalchemy import func


def songpoints(song):
    """ song point function """
    song_ids = []
    user_query = db.session.query(models.songs).filter((func.lower(models.songs.Title).contains(func.lower(song)))).all()
    for i in user_query:
        points = db.session.query(models.songs, models.points).join(models.points).filter(models.points.SongID == i.SongID).order_by(models.points.Points.desc()).first()
        song_ids.append(points)
    song_ids = sorted(song_ids, key=lambda x: x.points.Points, reverse=True)
    return song_ids

