import os
import pytest
from unittest.mock import MagicMock
from app import capture_data_async, get_progress

DATA_DIR = "./data"


if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


class MockClientSession:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def get(self, url, ssl):
        mock_response = MagicMock()
        file_path = os.path.join(DATA_DIR, f'{9999999}.json')
        if url.endswith(str(6)):
            mock_response.status = 200

            async def json():
                return {
                    "id": 9999999,
                    "main": {
                        "temp": 25,
                        "humidity": 70
                    }
                }

            mock_response.json = json

            open(file_path, 'w').close()
            with open(file_path, 'w') as file:
                json.dump(mock_response.json(), file)
        else:
            mock_response.status = 404

        return mock_response


@pytest.fixture
def mock_session():
    return MockClientSession()


@pytest.mark.asyncio
async def test_capture_data_async(mock_session):
    file_path = os.path.join(DATA_DIR, f'{9999999}.json')
    user_id = 9999999
    result = await capture_data_async(user_id)
    assert isinstance(result, list)
    assert len(result) > 0
    os.remove(file_path)


@pytest.mark.asyncio
async def test_get_progress():
    user_id = 9999999
    progress = get_progress(user_id)
    assert progress == 0.0
