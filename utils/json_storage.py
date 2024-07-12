import json
import os

DATA_DIR = "./data"


def put_data_storage(user_id, data):
    file_path_temp = os.path.join(DATA_DIR, f'{user_id}_temp.json')
    file_path = os.path.join(DATA_DIR, f'{user_id}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []
    if os.path.exists(file_path_temp):
        with open(file_path_temp, 'r') as file:
            existing_data_temp = json.load(file)
    else:
        existing_data_temp = []

    existing_data.append(data)
    existing_data_temp.append(data)
    with open(file_path, 'w') as file:
        json.dump(existing_data, file)
    with open(file_path_temp, 'w') as file:
        json.dump(existing_data_temp, file)
    print(user_id, data, file_path)


def get_data_count(user_id):
    file_path_temp = os.path.join(DATA_DIR, f'{user_id}_temp.json')
    file_path = os.path.join(DATA_DIR, f'{user_id}.json')
    if os.path.exists(file_path_temp):
        with open(file_path_temp, 'r') as file:
            data = json.load(file)
        return len(data)
    if not os.path.exists(file_path_temp):
        if os.path.exists(file_path):
            return 167.00
    return 0
