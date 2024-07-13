## Documentation

### Docker Installation

To run this application using Docker, follow these steps:

1. **Install Docker**: Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/get-started).

2. **Clone the Repository**: Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ````
3. **Build the Docker Image**: Build the Docker image using the provided Dockerfile. Replace nome_da_imagem with your desired image name:
    ```bash
   docker build -t iamge_name .
   ````
4. **How to Run**: To run the application using Docker with your OpenWeather API key, execute the following command:
    ```bash
    docker run -p 5000:5000 -e OPEN_WEATHER_API_KEY=YOUR_API_KEY image_name
   ````
    Replace YOUR_API_KEY with your actual OpenWeather API key and image_name with the name of the Docker image you built.
6. **How to Test**: To test the application, ensure you have Python and pytest installed. Run the tests using the following command:
    ```bash
    pytest
   ````
## How to Use the Routes
### Endpoint `/capture_data` (POST)

- **Description**: Initiates weather data collection for a specific user.
- **Parameters**: Send a POST request to `/capture_data` with a `userid` parameter defined.
- **Example Usage**: Using Postman or curl, send a POST request to `http://localhost:5000/capture_data` with `userid` defined in the request body.
- **Example CURL**:
  ```bash
  curl -X POST -d "userid=your_userid_here" http://127.0.0.1:5000/capture_data
  ```
### Endpoint /get_progress (GET)
- **Description**: Retrieves the progress of data collection for a specific user. 
- **Parameters**: Send a GET request to /get_progress with a userid parameter defined.
- **Example Usage**: Using Postman or your web browser, make a GET request to http://localhost:5000/get_progress?userid=your_userid_here.
- **Example CURL**:
  ```bash
  curl http://127.0.0.1:5000/get_progress?userid=your_userid_here
  ```
### Libs

**Flask**: Used to build the service API due to its simplicity, flexibility, and suitability for building web APIs in Python.

**requests**: Utilized for making HTTP requests to the Open Weather API to fetch weather data asynchronously.

**python-dotenv**: Used to load environment variables from a .env file, ensuring secure handling of sensitive information like API keys.

**aiohttp**: Chosen for its asynchronous capabilities, facilitating concurrent HTTP requests to handle multiple city IDs within the Open Weather API rate limits.

**pytest**: Employed for testing the application, ensuring functionality and reliability through automated tests.

**pytest-mock**: Used to mock dependencies during testing, enabling isolated unit testing of functions and API interactions.

**pytest-asyncio**: Utilized to test asynchronous code in conjunction with pytest, ensuring that async functions behave correctly under various conditions.

