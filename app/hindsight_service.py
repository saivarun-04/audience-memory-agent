import os

from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_BASE_URL = os.environ["HINDSIGHT_BASE_URL"]
HINDSIGHT_API_KEY = os.environ["HINDSIGHT_API_KEY"]
BANK_ID = "social-audience"

hindsight = Hindsight(
    HINDSIGHT_BASE_URL,
    HINDSIGHT_API_KEY,
)


def retain_audience_experience(content: str, context: str = "Social media performance"):
    return hindsight.retain(
        BANK_ID,
        content,
        context=context,
        metadata={"source": "audience-memory-agent"},
    )


def recall_audience_memory(query: str):
    return hindsight.recall(
        BANK_ID,
        query,
        max_tokens=1000,
        budget="low",
    )