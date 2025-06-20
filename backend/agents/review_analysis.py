from dataclasses import dataclass
import os

@dataclass
class ReviewSummary:
    sentiment: str
    top_words: list[str]

class ReviewAnalysisAgent:
    """Mock review analysis agent."""

    def __init__(self, openai_key: str | None = None) -> None:
        self.openai_key = openai_key or os.getenv("OPENAI_KEY")

    def summarize(self, reviews: list[str]) -> ReviewSummary:
        # naive summarization
        return ReviewSummary(sentiment="positive", top_words=["good", "quality"])
