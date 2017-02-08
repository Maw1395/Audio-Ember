from app import db

class songs (db.Model):
        SongID = db.Column(db.Integer,primary_key=True, autoincrement=False)
        Artist = db.Column(db.String(120), primary_key=True)
        Title = db.Column(db.String(120), primary_key = True)
        def __repr__(self):
                return "%s, %s, %d\n" %(self.Artist, self.Title, self.SongID)

class points(db.Model):
        SongID = db.Column(db.Integer, db.ForeignKey("songs.SongID"), nullable= False, primary_key=True)
        Genre = db.Column(db.String(25), primary_key=True)
        Points = db.Column(db.Integer)
        Date = db.Column(db.Date, primary_key=True)
        Rank = db.Column(db.Integer)
        def __repr__self(self):
                return "%d, %s, %d\n" %(self.SongID, self.Genre, self.Points)
class artist_points(db.Model):
        Artist = db.Column(db.String(120), primary_key=True)
        Points = db.Column(db.Integer)
        def __repr__self(self):
            return "%s, %d\n" %(self.Artist, self.Points)

class graphs(db.Model):
        SongID = db.Column(db.String(120), db.ForeignKey("songs.SongID"), nullable = False, primary_key = True)
        URL = db.Column(db.String(120), primary_key=True)
        def __repr__self(self):
            return "%s, %s\n" %(self.SongID, self.URL)
class song_points(db.Model):
        SongID = db.Column(db.Integer,db.ForeignKey("songs.SongID"), nullable = False, primary_key = True)
        Genre = db.Column(db.String(25), db.ForeignKey("points.Genre"), nullable = False, primary_key = True)
        Points = db.Column(db.Integer)
