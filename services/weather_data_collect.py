import os
import aiohttp
import asyncio
import datetime
from utils import config, json_storage
from utils.json_storage import get_data_count
from utils.config import CITIES, REQUEST_LIMIT, TIME_WINDOW

data_dict = []


async def make_api_request(session, url, retry_attempts=3):
    for attempt in range(retry_attempts):
        try:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 429:
                    retry_after = int(response.headers.get('Retry-After', 5))
                    print(f"Rate limit exceeded. Retrying after {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                else:
                    print(f"Request error: {response.status}")
                    return None
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error: {e}")
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            print(f"Unknown error: {e}")
            return None

    return None


async def capture_data_for_city(user_id, session, city_id):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={config.OPEN_WEATHER_API_KEY}&units=metric"
    print(url)
    weather_data = await make_api_request(session, url)
    if weather_data:
        data_temp = {"userid": user_id,
                     "userid_datetime": datetime.datetime.now().isoformat(),
                     "city_id": weather_data.get("id"),
                     "city_temp": weather_data["main"].get("temp"),
                     "humidity": weather_data["main"].get("humidity")}
        print(data_dict)
        data_dict.append(data_temp)
        json_storage.put_data_storage(data_temp["userid"], data_temp)
    else:
        print(f"Failed to fetch data for city ID {city_id}")


async def capture_data_async(user_id):
    async with aiohttp.ClientSession() as session:
        tasks = []
        request_counter = {'count': 0}
        for city_id in config.CITIES:
            if request_counter["count"] >= REQUEST_LIMIT:
                print("Request limit per minute reached. Waiting...")
                await asyncio.sleep(TIME_WINDOW)
                request_counter["count"] = 0  # Resets counter after wait
            task = asyncio.create_task(capture_data_for_city(user_id, session, city_id))
            tasks.append(task)
            request_counter["count"] += 1
        await asyncio.gather(*tasks)
    print(len(data_dict))
    os.remove(os.path.join("./data", f'{user_id}_temp.json'))
    return data_dict


def get_progress(user_id):
    total_cities = len(CITIES)
    completed_cities = get_data_count(user_id)
    return (completed_cities / total_cities) * 100
