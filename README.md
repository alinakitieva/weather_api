# Weather API

## Project Overview

Python sample solution for the [Weather API](https://roadmap.sh/projects/weather-api-wrapper-service) challenge from [roadmap.sh](https://roadmap.sh/).

This project is a simple Flask-based Weather API that fetches weather data from a third-party API (Visual Crossing
Weather API) based on a location and optional date range. The API supports caching using Redis to minimize API requests
and improve performance. It also includes rate limiting to prevent abuse.

## Features

- **Fetch Weather Data**: Retrieve weather data by location (city name, ZIP code, or coordinates) with an optional date
  range.
- **Caching**: Uses Redis to cache weather data for 12 hours, reducing external API calls and improving response times.
- **Rate Limiting**: Limits API requests to 100 per hour per client to prevent abuse.
- **Error Handling**: Handles cases such as invalid locations, third-party API failures, and internal server errors.

## Technologies Used

- **Flask**: Python web framework for building the API.
- **Requests**: Python library for making HTTP requests to the third-party weather API.
- **Redis**: In-memory data structure store used for caching.
- **RateLimit**: Library used for rate limiting API requests.
- **Visual Crossing Weather API**: External API used to fetch weather data.

## API Usage

### Base URL

The API is hosted locally at:  
`http://localhost:5000/weather`

### Request Format

#### Example Request

```bash
curl "http://localhost:5000/weather?location=Moscow&date1=2024-10-10"
```

### Query Parameters

- `location` (required): The location for which to retrieve weather data. Can be a city name, ZIP code, or coordinates.
- `date1` (optional): The start date for which to retrieve weather data in `yyyy-MM-dd` format. If omitted, it defaults
  to the current date.
- `date2` (optional): The end date for which to retrieve weather data in `yyyy-MM-dd` format.

### Response

The API returns weather data in JSON format.

#### Example Response:

```json
{
  "address": "Moscow",
  "days": [
    {
      "cloudcover": 85.3,
      "conditions": "Partially cloudy",
      "datetime": "2024-10-11",
      "datetimeEpoch": 1728594000,
      "description": "Partly cloudy throughout the day.",
      "dew": 46.2,
      "feelslike": 46.7,
      "feelslikemax": 54.2,
      "feelslikemin": 41.5,
      "hours": [
        {
          "cloudcover": 100.0,
          "conditions": "Overcast",
          "datetime": "00:00:00",
          "temp": 46.9,
          "winddir": 130.0,
          "windspeed": 10.3,
          "visibility": 5.6
        },
        {
          "cloudcover": 100.0,
          "conditions": "Overcast",
          "datetime": "01:00:00",
          "temp": 46.9,
          "winddir": 140.0,
          "windspeed": 9.7,
          "visibility": 5.7
        }
      ],
      "humidity": 87.4,
      "temp": 49.8,
      "tempmax": 54.2,
      "tempmin": 46.9,
      "windspeed": 16.4,
      "winddir": 136.5
    }
  ],
  "latitude": 55.757,
  "longitude": 37.615,
  "timezone": "Europe/Moscow",
  "tzoffset": 3.0
}

```

## Installation

### Prerequisites

- **Python 3.10+**
- **Redis**: Ensure that Redis is installed and running.
- **Visual Crossing Weather API Key**: Sign up and obtain an API key
  from [Visual Crossing](https://www.visualcrossing.com/).

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/alinakitieva/weather_api.git
   cd weather_api
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   Create a `.env` file and add your Visual Crossing API key:

   ```bash
   WEATHER_API_KEY=your_api_key
   ```

5. **Run Redis**:
   Make sure Redis is running locally. If Redis isn't installed, you can install it on macOS using:

   ```bash
   brew install redis
   ```

   Start Redis:

   ```bash
   redis-server
   ```

6. **Run the Flask App**:

   ```bash
   python app.py
   ```

7. **Test the API**:
   Use `curl` or a browser to access the API:

   ```bash
   curl "http://localhost:5000/weather?location=Moscow&date1=2024-10-10"
   ```

## Rate Limiting

The API limits requests to **100 requests per hour per client**. If this limit is exceeded, the API will return a
`429 Too Many Requests` response.

## Caching

Redis is used to cache weather data for **12 hours**. If a request is made for the same location and date within this
timeframe, the cached data will be returned instead of making a new API call to the external service.

## Error Handling

The API includes error handling for the following scenarios:

- **Invalid Location**: Returns an error if the location cannot be found.
- **Service Unavailable**: Returns an error if the third-party API is down.
- **Rate Limit Exceeded**: Prevents abuse by limiting the number of API requests per hour.
