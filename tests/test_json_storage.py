import os
import json
import pytest
from utils.json_storage import put_data_storage, get_data_count

DATA_DIR = "./data"


def test_put_data_storage():
    user_id = 9999999
    data = {"userid": "9999999", "userid_datetime": "2024-07-12T17:48:27.150817", "city_id": 3439525, "city_temp": 5.21,
            "humidity": 64}

    put_data_storage(user_id, data)

    file_path = os.path.join(DATA_DIR, f'{user_id}.json')
    assert os.path.exists(file_path)

    with open(file_path, 'r') as file:
        existing_data = json.load(file)
        assert existing_data == [data]


def test_get_data_count_with_file():
    user_id = '9999999'
    file_path = os.path.join(DATA_DIR, f'{user_id}.json')
    file_path_temp = os.path.join(DATA_DIR, f'{user_id}_temp.json')
    data = {"userid": "9999999", "userid_datetime": "2024-07-12T17:48:27.150817", "city_id": 3439525, "city_temp": 5.21,
            "humidity": 64}
    count = get_data_count(user_id)
    os.remove(file_path)
    os.remove(file_path_temp)
    assert count == len([data])
