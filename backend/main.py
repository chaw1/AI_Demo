from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path

from agents.competitor_monitor import CompetitorMonitorAgent
from agents.customer_service import CustomerServiceAgent
from agents.listing_optimizer import ListingOptimizerAgent
from agents.review_analysis import ReviewAnalysisAgent

app = FastAPI(title="Amazon Intelligence Demo")

frontend_path = Path(__file__).resolve().parent.parent / 'frontend'
app.mount('/static', StaticFiles(directory=frontend_path, html=True), name='static')


@app.get('/')
def index():
    return FileResponse(frontend_path / 'index.html')

competitor_agent = CompetitorMonitorAgent()
customer_agent = CustomerServiceAgent()
optimizer_agent = ListingOptimizerAgent()
review_agent = ReviewAnalysisAgent()

class ScrapeResponse(BaseModel):
    title: str | None = None
    bullets: list[str] | None = None
    images: list[str] | None = None
    price: str | None = None
    brand: str | None = None
    description: str | None = None

class ServiceRequest(BaseModel):
    question: str

class ServiceReply(BaseModel):
    answer: str
    sentiment: str | None = None

class OptimizeRequest(BaseModel):
    title: str

class OptimizeResponse(BaseModel):
    improved_title: str
    score: int
    keywords: list[str]

class ReviewRequest(BaseModel):
    reviews: list[str]

class ReviewResponse(BaseModel):
    sentiment: str
    top_words: list[str]

@app.get("/api/scrape", response_model=ScrapeResponse)
def scrape(asin: str = Query(None), url: str = Query(None)):
    if not asin and not url:
        raise HTTPException(status_code=400, detail="ASIN or URL required")
    try:
        data = competitor_agent.fetch_competitor_data(asin or url)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return data


@app.post("/api/customer_service", response_model=ServiceReply)
def customer_service(req: ServiceRequest):
    reply = customer_agent.reply(req.question)
    return reply


@app.post("/api/listing_optimizer", response_model=OptimizeResponse)
def listing_optimizer(req: OptimizeRequest):
    result = optimizer_agent.optimize_listing(req.title)
    return result


@app.post("/api/review_analysis", response_model=ReviewResponse)
def review_analysis(req: ReviewRequest):
    summary = review_agent.summarize(req.reviews)
    return summary
