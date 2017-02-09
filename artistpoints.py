from app import db, models
from sqlalchemy import func
import mylog


@mylog.log("log.txt")
def artistpoints(artist):
    artistIDs = []
    user_query = db.session.query(models.songs).filter(func.lower(models.songs.Artist).contains(func.lower(artist))).all()
    for i in user_query:
        points = db.session.query(models.songs, models.points).join(models.points).filter(models.points.SongID == i.SongID).order_by(models.points.Points.desc()).first()
        artistIDs.append(points)
    artistIDs = sorted(artistIDs, key = lambda x: x.points.Points, reverse = True)
    return artistIDs
#hello
