from flask import Flask, jsonify, request
from flask_cors import CORS
interns = []

class Intern:
    def __init__(self, name, email, start_date, end_date):
        self.name = name
        self.email = email
        self.start_date = start_date
        self.end_date = end_date

app = Flask(__name__)

CORS(app, origins=['http://localhost:3000/','http://localhost:3000'], methods=['GET', 'POST'], allow_headers=['Content-Type'])

@app.route('/interns', methods=['POST'])
def register_intern():
    data = request.get_json()
    # Perform validation on the data
    intern = Intern(data['name'], data['email'], data['start_date'], data['end_date'])
    interns.append(intern)
    return 'Intern registered successfully'



@app.route('/interns', methods=['GET'])
def get_interns():
    return jsonify([vars(intern) for intern in interns])


@app.route('/interns/<int:intern_id>', methods=['PUT', 'PATCH'])
def edit_intern(intern_id):
    intern = interns[intern_id]
    data = request.get_json()
    # Perform validation and update intern fields
    return 'Intern updated successfully'


@app.route('/interns/<int:intern_id>', methods=['DELETE'])
def delete_intern(intern_id):
    interns.pop(intern_id)
    return 'Intern deleted successfully'


if __name__ == '__main__':
    app.run(port=8000)
