from flask import Flask
from flask_restful import Resource, Api

app2 = Flask(__name__)
api = Api(app2)

class Student(Resource):
    def get(self,name):
        return {'student': name }
    
api.add_resource(Student, '/student/<string:name>') # http//localhost:5001/student/Rolf
    
app2.run(port=5001)
