# Weather API Wrapper Service

A Flask-based Weather API Wrapper that fetches weather data from the Visual Crossing Weather API and caches responses using Redis.

## Features

- Flask REST API
- Visual Crossing Weather API Integration
- Redis Caching
- Cache Expiration (TTL)
- Rate Limiting with Flask-Limiter
- Environment Variables
- Docker Redis Support

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
WEATHER_API_KEY=your_api_key
REDIS_URL=redis://localhost:6379
CACHE_EXPIRY=43200
```

## Run

```bash
python app.py
```

## Endpoint

```http
GET /weather/<city>
```

Example:

```http
GET /weather/london
```

## Tech Stack

- Python
- Flask
- Redis
- Docker
- Visual Crossing Weather API
