from __future__ import annotations
from bs4 import BeautifulSoup
from dataclasses import dataclass
import os
import re
from pathlib import Path

@dataclass
class ListingData:
    title: str | None = None
    bullets: list[str] | None = None
    images: list[str] | None = None
    price: str | None = None
    brand: str | None = None
    description: str | None = None

class CompetitorMonitorAgent:
    """Mock agent to fetch Amazon listing information."""

    sample_file = Path(__file__).resolve().parent / "sample_listing.html"

    def __init__(self, serpapi_key: str | None = None) -> None:
        self.serpapi_key = serpapi_key or os.getenv("SERPAPI_KEY")

    def fetch_competitor_data(self, asin_or_url: str) -> ListingData:
        """Fetch listing data. Currently reads from a sample HTML file."""
        # In real use, you'd fetch from Amazon. For demo we read a local file.
        html = self.sample_file.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, 'html.parser')
        data = ListingData()
        title_el = soup.select_one('#productTitle')
        if title_el:
            data.title = title_el.get_text(strip=True)
        bullet_els = soup.select('#feature-bullets ul li')
        if bullet_els:
            data.bullets = [b.get_text(strip=True) for b in bullet_els]
        img_els = soup.select('#altImages img')
        if img_els:
            data.images = [img.get('alt', '') for img in img_els]
        price_el = soup.select_one('#priceblock_ourprice') or soup.select_one('#priceblock_dealprice')
        if price_el:
            data.price = price_el.get_text(strip=True)
        brand_el = soup.select_one('#bylineInfo')
        if brand_el:
            data.brand = brand_el.get_text(strip=True)
        desc_el = soup.select_one('#productDescription')
        if desc_el:
            data.description = desc_el.get_text(strip=True)
        return data
