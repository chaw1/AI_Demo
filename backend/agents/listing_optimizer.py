from dataclasses import dataclass
import os

@dataclass
class OptimizationResult:
    improved_title: str
    score: int
    keywords: list[str]

class ListingOptimizerAgent:
    """Mock listing optimizer."""

    def __init__(self, openai_key: str | None = None) -> None:
        self.openai_key = openai_key or os.getenv("OPENAI_KEY")

    def optimize_listing(self, title: str) -> OptimizationResult:
        improved = title + " (Optimized)"
        return OptimizationResult(improved_title=improved, score=80, keywords=["sample", "keyword"])
