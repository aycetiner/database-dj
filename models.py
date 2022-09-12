"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                         primary_key=True, 
                         autoincrement=True)

    name = db.Column(db.String(30), 
                         nullable=False)
    
    description = db.Column(db.String(50), 
                         nullable=False)


    songs = db.relationship('Song', backref='playlists', secondary='playlistsongs')
    playlistsongs = db.relationship('PlaylistSong', backref='playlists', cascade="all, delete-orphan")


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                         primary_key=True, 
                         autoincrement=True)

    title = db.Column(db.String(50), 
                         nullable=False)
    
    artist = db.Column(db.String(50), 
                         nullable=False)

    playlistsong = db.relationship('PlaylistSong', backref='songs', cascade="all, delete-orphan")


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlistsongs"

    id = db.Column(db.Integer,
                         primary_key=True, 
                         autoincrement=True)

    playlist_id = db.Column(db.Integer,
                                db.ForeignKey("playlists.id", ondelete="CASCADE"))
    
    song_id = db.Column(db.Integer,
                                db.ForeignKey("songs.id", ondelete="CASCADE"))
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
