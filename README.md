# AI Demo Project

This repository contains a minimal demonstration of an Amazon intelligence toolkit. The main feature allows entering an Amazon ASIN or product URL and quickly returning structured listing information.

## Backend
- Python `FastAPI` server located in `backend/`
- Endpoint `GET /api/scrape` accepts `asin` or `url` query parameters
- A mock `CompetitorMonitorAgent` parses a sample HTML file and returns listing data

### Running
```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```
The backend also serves the Vue3 frontend.

## Frontend
- Minimal Vue3 app (`frontend/index.html`)
- Allows input of ASIN or URL and displays JSON response

Open `http://127.0.0.1:8000` after starting the backend to use the demo.

*Note*: Due to environment restrictions, the demo uses a static sample HTML file instead of live Amazon requests.
