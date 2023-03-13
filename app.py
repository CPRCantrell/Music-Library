from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load, fields, ValidationError
from flask_migrate import Migrate
from flask_restful import Api, Resource
from dotenv import load_dotenv
from os import environ

load_dotenv()

# Create App instance
app = Flask(__name__)

# Add DB URI from .env
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

# Registering App w/ Services
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app)
Migrate(app, db)

# Models
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    album = db.Column(db.String(255), nullable=False)
    relase_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f'{self.id} {self.title} {self.artist} {self.album} {self.relase_date} {self.genre}'

# Schemas
class SongSchema(ma.Schema):
    id = fields.Interger(Primary_key=True)
    title = fields.String(rquired=True)
    artist = fields.String(rquired=True)
    album = fields.String(rquired=True)
    relase_date = fields.Date(rquired=True)
    genre = fields.String(rquired=True)

    class Meta:
        fields = ('id','title','artist','album','relase_date','genre')

    @post_load
    def create_song(self, data, **kwargs):
        return Song(**data)

song_schema = SongSchema()
songs_schema = SongSchema(many=True)

# Resources
class SongListResource(Resource):
    def get(self):
        return songs_schema.dump(Song.query.all()), 200

    def post(self):
        try:
            add_song = songs_schema.load(request.get_json())
            db.session.add(add_song)
            db.session.commit()
            return songs_schema.dump(add_song), 201
        except ValidationError as error:
            return error.messages, 400

class SongResource(Resource):
    def get(self, song_id):
        return song_schema.dump(Song.query.get_or_404(song_id)), 200

    def put(self, song_id):
        song_from_db = Song.query.get_or_404(song_id)
        if 'title' in request.json:
            song_from_db.title = request.json['title']
        if 'artist' in request.json:
            song_from_db.artist = request.json['artist']
        if 'album' in request.json:
            song_from_db.album = request.json['album']
        if 'relase_date' in request.json:
            song_from_db.relase_date = request.json['relase_date']
        if 'genre' in request.json:
            song_from_db.genre = request.json['genre']
        db.session.commit()
        return song_schema.dump(song_from_db), 200

    def delete(self, song_id):
        song_from_db = Song.query.get_or_404(song_id)
        db.session.delete(song_from_db)
        db.session.commit()
        return '', 204

# Routes
api.add_resource(SongListResource, '/api/songs')
api.add_resource(SongResource, '/api/songs/<int:song_id>')