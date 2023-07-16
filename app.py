from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from cassandra.cluster import Cluster
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.policies import DCAwareRoundRobinPolicy, TokenAwarePolicy
from flask_cqlalchemy import CQLAlchemy
from cassandra.cqlengine import columns
from datetime import datetime
from cassandra.cqlengine.models import Model

import uuid
interns = []


PATH_TO_BUNDLE_YAML = './connect-bundle-CODEPALY UG.yaml'


def get_cluster():
    profile = ExecutionProfile(
        load_balancing_policy=TokenAwarePolicy(
            DCAwareRoundRobinPolicy(local_dc='us-east-1')
        )
    )

    return Cluster(
        execution_profiles={EXEC_PROFILE_DEFAULT: profile},
        scylla_cloud=PATH_TO_BUNDLE_YAML,
        )
create_table_query = """
    CREATE TABLE IF NOT EXISTS interns (
        name TEXT,
        email TEXT,
        start_date DATE,
        end_date DATE ,
        PRIMARY KEY (email)
    )
    """
cluster = get_cluster()
session = cluster.connect() 
session.set_keyspace('your_keyspace')
   
class Intern:
    def __init__(self, name, email, start_date, end_date):
        self.name = name
        self.email = email
        self.start_date = start_date
        self.end_date = end_date
        

app = Flask(__name__)
if __name__ == '__main__':
    app.run()




CORS(app, origins=['*'], methods=['GET', 'POST'], allow_headers=['Content-Type'])


@app.route('/')
def index():
    return 'CodePlay API!'

@app.route('/interns', methods=['POST'])
def register_intern():
    data = request.get_json()
   
    enter_data = "INSERT INTO interns (name, email, start_date, end_date) VALUES (%s, %s, %s, %s)"
   
    f = session.execute(enter_data, (data["name"], data["email"], data["start_date"], data["end_date"]))
    print(f)
    return 'Intern registered successfully'



@app.route('/interns', methods=['GET'])
def get_interns():
   
    select_query = "SELECT name, email, start_date, end_date  FROM interns"
    result = session.execute(select_query)
    data = []
    for row in result:
        data.append({'name': row.name, 'email': row.email,
        'start_date': str(row.start_date),
            'end_date': str(row.end_date)})
    return jsonify(data)  


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
