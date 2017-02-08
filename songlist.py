""" Returns list of songs based on genre """
from app import db, models


def list_to_return(genre):
    """ Returns list of highest scoring songs in the database """
    points_todos = []
    song_id = []
    point = db.session.query(models.songs, models.points).join(models.points).order_by(models.points.Points.desc()).filter(models.points.Genre == genre).all()
    for i in point:
        if i.songs.SongID not in song_id:
            song_id.append(i.songs.SongID)
            points_todos.append((i.songs.Title, i.songs.Artist, i.points.Points, i.songs.SongID))
    return points_todos


POP = list_to_return('pop')
COUNTRY = list_to_return('country')
HOT_100 = list_to_return('hot-100')
ROCK = list_to_return('rock')
RB = list_to_return('r-b-hip-hop')
EDM = list_to_return('dance-electronic')


def songlist(genre):
    """ Call list_to_return based on genre argument """
    if genre == 'pop':
        return POP
    if genre == 'country':
        return COUNTRY
    if genre == 'hot-100':
        return HOT_100
    if genre == 'rock':
        return ROCK
    if genre == 'rb':
        return RB
    if genre == 'edm':
        return EDM

