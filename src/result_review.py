from src.shared_dependencies import app, mongo
from flask import jsonify

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