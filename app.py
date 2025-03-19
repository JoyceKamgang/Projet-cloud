from flask import flask, jsonify
import json
import yaml

app = Flask(_name_)
def load_data(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        if filename.endswith('.json'):
            return json.load(file)
        elif filename.endswith('.yaml') or filename.endswith('yml'):
            return yaml.safe_load(file)
    return {}

#Endpoints API

@app.route('/api/events', methods=['GET'])
def get_events():
    data = load_data('app/static_data/events.json')
    return jsonify(data)

@app.route('api/news', methods=['GET'])
def get_news():
    data = load_data('app/static/news.yaml')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')