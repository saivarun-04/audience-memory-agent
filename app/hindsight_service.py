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


def retain_audience_experience(
    content: str,
    context: str = "Social media performance",
):
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
        max_tokens=700,
        budget="low",
    )


def generate_recommendation(
    memories: list[str],
    platform: str = "LinkedIn",
) -> str:
    response = hindsight.reflect(
        BANK_ID,
        f"""What should this team do for its next {platform} post?

Use the audience's previous experiences and preferences stored in memory.
Give one concise, practical recommendation.
Do not invent audience behavior.
Explain briefly why the recommendation follows from the remembered audience behavior.""",
        budget="low",
    )

    return response.text