from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
# need to import this 
## each game is a resource, a thing that our api can return

app = Flask(__name__)
app.config["MONGO_STUDENTSDB"] = "student_db"
mongo = PyMongo(app, config_prefix='MONGO')
APP_URL = "http://127.0.0.1:5000"

class Classroom(Resource):
### MESSED AROUND WITH MY DOMAIN MODEL A FEW TIMES SO
#A LOT OF THESE TITLES AND NAMES i HAVEN'T GOTTEN AROUND TO CHANGING 

    def getData(self, student_id=None ):
        data = []

        if class_id:
            class_info = mongo.db.student.find_one({"student_id": student_id}, {"_id": 0})
            if studnet_info:
                return jsonify({"status": "ok", "data": student_info})
            else:
                return {"response": "no student found for {}".format(student_id)}

        elif name:
            cursor = mongo.db.student.find({"name": name},
            for student in cursor:
                student['url'] = APP_URL + url_for('students') + "/" + student.get('student_id')
                data.append(student)

            return jsonify({"name": name, "response": data})

        else:
            cursor = mongo.db.student.find({}, {"_id": 0, "update_time": 0}).limit(10)

            for student in cursor:
                print student
                student['url'] = APP_URL + url_for('students') + "/" + student.get('student_id')
                data.append(student)

            return jsonify({"response": data})

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            student_id = data.get('student_id')
            if student_id:
                if mongo.db.student.find_one({"student_id": student_id}):
                    return {"response": "student already exists."}
                else:
                    mongo.db.student.insert(data)
            else:
                return {"response": "student_id number missing"}

        return redirect(url_for("students"))

    def put(self, student_id):
        data = request.get_json()
        mongo.db.student.update({'student_id': student_id}, {'$set': data})
        return redirect(url_for("students"))

    def delete(self, student_id):
        mongo.db.student.remove({'student_id': student_id})
        return redirect(url_for("students"))


class Index(Resource):
    def get(self):
        return redirect(url_for("students"))


api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Student, "/api", endpoint="students")
api.add_resource(Student, "/api/<string:student_id>", endpoint="student_id")
api.add_resource(Student, "/api/name/<string:name>", endpoint="name")

if __name__ == "__main__":
    app.run(debug=True)
