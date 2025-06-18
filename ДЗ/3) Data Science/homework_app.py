import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
from random import choice

app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False
with open("questions.json", encoding="utf-8") as f:
    questions = json.load(f)
    print(questions)


class Question(Resource):
    def get(self, id=0):
        if id == 0:
            return choice(questions), 200
        for question in questions:
            if question['id'] == id:
                return question, 200
        return 'Not found this question.', 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('answer')
        params = parser.parse_args(strict=True)


api.add_resource(Question, "/questions", "/questions/", "/questions/<int:id>")
app.run(debug=True)
