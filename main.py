from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_args = reqparse.RequestParser()
video_args.add_argument('name', type=str, help='Enter Name of Video', required=True)
video_args.add_argument('views', type=int, help='Enter No. of views', required=True)
video_args.add_argument('likes', type=int, help='Enter No. of likes', required=True)

videos = {}


def abort_video_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video ID not Valid")


def abort_video_exist(video_id):
    if video_id in videos:
        abort(409, message="Video Already Exists with given ID")


class Video(Resource):
    def get(self, video_id):
        abort_video_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_video_exist(video_id)
        args = video_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_video_not_exist(video_id)
        return '', 204


api.add_resource(Video, "/channel/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)