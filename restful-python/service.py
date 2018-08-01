from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

TODOS = {
        1: {"task": "Sleep"},
        2: {"task": "Eat"},
        3: {"task": "Work"}
}

parser = reqparse.RequestParser()
parser.add_argument("task")

class Todo(Resource):
    def get(self, todo_id):
        return TODOS[int(todo_id)]

    def delete(self, todo_id):
        del TODOS[int(todo_id)]
        return "deleted"

    def put(self, todo_id):
        args = parser.parse_args()
        TODOS[int(todo_id)] = {"task": args['task']}
        return TODOS[int(todo_id)]

class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        new_id = max(TODOS.keys()) + 1
        TODOS[new_id] = {"task": args['task']}
        return TODOS[new_id]

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

app.run(debug=True)
