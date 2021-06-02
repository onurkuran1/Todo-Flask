from flask import Flask, jsonify, make_response
import todosDao
from flask import Flask, redirect, url_for, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def main():
    test=todosDao.todosDao()
    results=test.getAll()
    return jsonify(results)

@app.route("/add", methods=['POST','GET'])
def add():
    data=request.get_json()
    test = todosDao.todosDao()
    result=test.save(data)
    return jsonify(result)


@app.route("/delete/<string:id>",methods=['POST','GET','DELETE'])
def delete(id):
    test = todosDao.todosDao()
    result=test.delete(id)
    return jsonify(result)

@app.route("/update",methods=['POST','GET','PUT'])
def update():
    data=request.get_json()
    test = todosDao.todosDao()
    result=test.update(data)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
