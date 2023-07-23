from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/iconix"
mongo = PyMongo(app)

@app.route('/results', methods=['GET'])
def get_results():
    results = mongo.db.results.find()
    response = []
    for result in results:
        result['_id'] = str(result['_id'])
        response.append(result)
    return jsonify(response)

@app.route('/results/<id>', methods=['GET'])
def get_result(id):
    result = mongo.db.results.find_one({'_id': ObjectId(id)})
    if result:
        result['_id'] = str(result['_id'])
        return jsonify(result)
    else:
        return jsonify({"error": "Result not found"}), 404

@app.route('/results/<id>/download', methods=['GET'])
def download_result(id):
    result = mongo.db.results.find_one({'_id': ObjectId(id)})
    if result:
        result['_id'] = str(result['_id'])
        return jsonify(result)
    else:
        return jsonify({"error": "Result not found"}), 404

@app.route('/results/<id>/share', methods=['POST'])
def share_result(id):
    result = mongo.db.results.find_one({'_id': ObjectId(id)})
    if result:
        result['_id'] = str(result['_id'])
        return jsonify(result)
    else:
        return jsonify({"error": "Result not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
