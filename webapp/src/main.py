import os
from flask import Flask, jsonify
import web_detect

app = Flask(__name__)

@app.route('/image/info/<path:path>', methods=['GET'])
def get_image_info(path):
    annotations = web_detect.annotate(path)
    entities = []
    for entity in annotations.web_entities:
        entities.append({
                    'Score': entity.score,
                    'Description': entity.description
                })
    return jsonify(entities)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
