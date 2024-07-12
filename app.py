from flask import Flask, request, jsonify
import asyncio
from utils import config
from services.weather_data_collect import capture_data_async, get_progress

app = Flask(__name__)
data_dict = []
config.run_config(app)


@app.route('/capture_data', methods=['POST'])
def capture_data():
    data = request.form
    user_id = data.get('userid', '')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    asyncio.run(capture_data_async(user_id))
    return jsonify({"status": "Data collection initiated"}), 200


@app.route('/get_progress', methods=['GET'])
def return_progress():
    user_id = request.args.get('userid', '')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    progress_percentage = get_progress(user_id)
    return jsonify({"userid": user_id, "progress": progress_percentage}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
