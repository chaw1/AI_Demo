from dataclasses import dataclass
import os

@dataclass
class Reply:
    answer: str
    sentiment: str | None = None

class CustomerServiceAgent:
    """Mock customer service agent."""

    def __init__(self, openai_key: str | None = None) -> None:
        self.openai_key = openai_key or os.getenv("OPENAI_KEY")

    def reply(self, question: str) -> Reply:
        # trivial mock: echo question
        return Reply(answer=f"Thanks for asking about '{question}'. We will get back to you soon.", sentiment="neutral")
