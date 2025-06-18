from dataclasses import dataclass

@dataclass
class Reply:
    answer: str
    sentiment: str | None = None

class CustomerServiceAgent:
    """Mock customer service agent."""

    def reply(self, question: str) -> Reply:
        # trivial mock: echo question
        return Reply(answer=f"Thanks for asking about '{question}'. We will get back to you soon.", sentiment="neutral")
