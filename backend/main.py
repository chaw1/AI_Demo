from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path

from agents.competitor_monitor import CompetitorMonitorAgent

app = FastAPI(title="Amazon Intelligence Demo")

frontend_path = Path(__file__).resolve().parent.parent / 'frontend'
app.mount('/static', StaticFiles(directory=frontend_path, html=True), name='static')


@app.get('/')
def index():
    return FileResponse(frontend_path / 'index.html')

agent = CompetitorMonitorAgent()

class ScrapeResponse(BaseModel):
    title: str | None = None
    bullets: list[str] | None = None
    images: list[str] | None = None
    price: str | None = None
    brand: str | None = None
    description: str | None = None

@app.get("/api/scrape", response_model=ScrapeResponse)
def scrape(asin: str = Query(None), url: str = Query(None)):
    if not asin and not url:
        raise HTTPException(status_code=400, detail="ASIN or URL required")
    try:
        data = agent.fetch_competitor_data(asin or url)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return data
