from dataclasses import dataclass

@dataclass
class ReviewSummary:
    sentiment: str
    top_words: list[str]

class ReviewAnalysisAgent:
    """Mock review analysis agent."""

    def summarize(self, reviews: list[str]) -> ReviewSummary:
        # naive summarization
        return ReviewSummary(sentiment="positive", top_words=["good", "quality"])
