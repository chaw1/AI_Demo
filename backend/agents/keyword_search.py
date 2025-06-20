from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import List, Dict, Any


@dataclass
class SearchResult:
    asin: str
    title: str | None = None
    price: float | None = None
    rating: float | None = None
    reviews: int | None = None
    brand: str | None = None
    image: str | None = None
    is_prime: bool | None = None
    position: int | None = None


class AmazonScraper:
    """Fetch Amazon search results. Uses a local JSON sample for the demo."""

    sample_file = Path(__file__).resolve().parent / "sample_search.json"

    def search_products(self, keyword: str, marketplace: str = "amazon.de") -> List[SearchResult]:
        """Return a list of SearchResult objects."""
        try:
            data = json.loads(self.sample_file.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return []

        products: List[SearchResult] = []
        for item in data.get("organic_results", []):
            result = SearchResult(
                asin=item.get("asin", ""),
                title=item.get("title"),
                price=item.get("price", {}).get("value"),
                rating=item.get("rating"),
                reviews=item.get("reviews"),
                brand=item.get("brand"),
                image=item.get("thumbnail"),
                is_prime=item.get("is_prime"),
                position=item.get("position"),
            )
            products.append(result)
        return products

    def get_product_details(self, asin: str) -> Dict[str, Any]:
        """Return extra details for a product. For the demo it returns an empty dict."""
        return {}


class AIAnalyzer:
    """Mock analyzer that aggregates basic statistics from search results."""

    def analyze_listings(self, products: List[SearchResult]) -> Dict[str, Any]:
        if not products:
            return {}

        prices = [p.price for p in products if p.price is not None]
        avg_price = round(mean(prices), 2) if prices else None

        brand_count: Dict[str, int] = {}
        for p in products:
            if p.brand:
                brand_count[p.brand] = brand_count.get(p.brand, 0) + 1

        top_brand = None
        if brand_count:
            top_brand = max(brand_count.items(), key=lambda x: x[1])[0]

        return {
            "total_products": len(products),
            "average_price": avg_price,
            "top_brand": top_brand,
        }
