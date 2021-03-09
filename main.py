from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __refr__(self):
        return f"Video(Name={name}, Views={views}, Likes={likes})"


video_args = reqparse.RequestParser()
video_args.add_argument('name', type=str, help='Enter Name of Video', required=True)
video_args.add_argument('views', type=int, help='Enter No. of views', required=True)
video_args.add_argument('likes', type=int, help='Enter No. of likes', required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument('name', type=str, help='Enter Name of Video')
video_update_args.add_argument('views', type=int, help='Enter No. of views')
video_update_args.add_argument('likes', type=int, help='Enter No. of likes')


resources_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resources_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find with given ID')
        return result

    @marshal_with(resources_fields)
    def put(self, video_id):
        args = video_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message= 'Video ID already in use')

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resources_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

api.add_resource(Video, "/channel/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)