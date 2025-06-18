# AI Demo Project

This repository contains a minimal demonstration of an Amazon intelligence toolkit. It exposes four mock services representing the project agents:
CustomerServiceAgent, ListingOptimizerAgent, ReviewAnalysisAgent and CompetitorMonitorAgent. The Competitor Monitor feature accepts an ASIN or URL and returns structured listing information.

## Backend
- Python `FastAPI` server located in `backend/`
- Endpoint `GET /api/scrape` returns mock listing data
- Endpoint `POST /api/customer_service` returns a simple reply
- Endpoint `POST /api/listing_optimizer` returns optimized title data
- Endpoint `POST /api/review_analysis` returns a review summary


### Running
```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```
The backend also serves the Vue3 frontend.

## Frontend
- Vue3 app (`frontend/index.html`) provides four tabs matching the agents
- Basic styling is provided using the Bootstrap 5 CDN
- Each tab sends a request to the corresponding API and shows the JSON reply


Open `http://127.0.0.1:8000` after starting the backend to use the demo.

*Note*: Due to environment restrictions, the demo uses a static sample HTML file instead of live Amazon requests.
