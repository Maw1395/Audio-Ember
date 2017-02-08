""" Calculate artist points """
from app import db, models
from sqlalchemy import func
import re


def totalpoints(artist):
    regex = r'(?i)\b' + re.escape(artist) + r'\b'
    tpoints = 0
    user_query = db.session.query(models.songs).filter(func.lower(models.songs.Artist).contains(func.lower(artist))).all()
    for i in user_query:
        st = i.Artist
        if re.search(regex, st):
            points = db.session.query(models.songs, models.points).join(models.points).filter(models.points.SongID == i.SongID).order_by(models.points.Points.desc()).first()
            tpoints = tpoints + points.points.Points
    return tpoints

