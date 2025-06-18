import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
from random import choice

app = Flask(__name__)
api = Api(app)
with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)


class Question(Resource):
    def get(self, id=0):
        if id == 0:
            return choice(questions), 200
        for question in questions:
            if question['id'] == id:
                return question, 200
        return 'Not found this question.', 404

class Answer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, location='json')
        parser.add_argument('answer', required=True, location='json')
        args = parser.parse_args(strict=True)
        for question in questions:
            if question['id'] == args['id']:
                if question['correct_answer'].lower().strip() == args['answer'].lower().strip():
                    return 'Correct!', 200
                else:
                    return 'Wrong answer!', 200
        return 'This question does not exist.', 404


api.add_resource(Question, "/questions", "/questions/", "/questions/<int:id>")
api.add_resource(Answer, "/answers", "/answers/")
app.run(debug=True)
