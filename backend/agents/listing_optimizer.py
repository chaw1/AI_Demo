from dataclasses import dataclass

@dataclass
class OptimizationResult:
    improved_title: str
    score: int
    keywords: list[str]

class ListingOptimizerAgent:
    """Mock listing optimizer."""

    def optimize_listing(self, title: str) -> OptimizationResult:
        improved = title + " (Optimized)"
        return OptimizationResult(improved_title=improved, score=80, keywords=["sample", "keyword"])
