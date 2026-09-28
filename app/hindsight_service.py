import os

from dotenv import load_dotenv
from hindsight_client import Hindsight
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.environ["FREELLMAPI_API_KEY"]
OPENAI_BASE_URL = "http://127.0.0.1:31415/v1"

llm = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)

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
    memory_text = "\n".join(f"- {memory}" for memory in memories)

    response = llm.chat.completions.create(
        model="gemini-3.6-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are EchoMind, an AI that helps social teams "
                    "make audience-aware content decisions. "
                    "Use the provided Hindsight memories as evidence. "
                    "Give one concise, practical recommendation. "
                    "Do not invent audience behavior."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Based on these audience memories, what should the team "
                    f"do for its next {platform} post?\n\n"
                    f"{memory_text}"
                ),
            },
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content