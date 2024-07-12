import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_capture_data_success(client, mocker):
    form_data = {
        'userid': '9999999'
    }
    mock_data = [
        {"userid": "9999999", "userid_datetime": "2024-07-12T17:48:27.150817", "city_id": 3439525, "city_temp": 5.21,
         "humidity": 64}
    ]
    mocker.patch('services.weather_data_collect.capture_data_async', return_value=mock_data)

    rv = client.post('/capture_data', data=form_data)
    assert rv.status_code == 200
    assert b'Data collection initiated' in rv.data


async def test_get_progress_success(client):
    rv = await client.get('/get_progress?userid=9999999')
    assert rv.status_code == 200
    assert b'"progress":' in rv.data


def test_capture_data_missing_userid(client):
    rv = client.post('/capture_data')
    assert rv.status_code == 400
    assert b'user_id is required' in rv.data


def test_get_progress_missing_userid(client):
    rv = client.get('/get_progress')
    assert rv.status_code == 400
