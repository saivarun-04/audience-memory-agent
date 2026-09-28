from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.hindsight_service import (
    recall_audience_memory,
    retain_audience_experience,
)

app = FastAPI(title="Audience Memory Agent")


class Experience(BaseModel):
    content: str
    context: str = "Social media performance"


@app.get("/", response_class=FileResponse)
def root():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/memory")
def memory():
    result = recall_audience_memory(
        "What type of content did the audience respond positively to?"
    )

    return {
        "query": "What type of content did the audience respond positively to?",
        "memories": [item.text for item in result.results],
    }


@app.post("/learn")
def learn(experience: Experience):
    result = retain_audience_experience(
        experience.content,
        experience.context,
    )

    return {
        "success": result.success,
        "message": "Experience stored in Hindsight memory.",
    }


@app.get("/recommendation")
def recommendation():
    result = recall_audience_memory(
        "What type of content did the audience respond positively to?"
    )

    memories = [item.text for item in result.results]

    combined_memory = " ".join(memories).lower()

    if "concise code" in combined_memory or "practical" in combined_memory:
        recommendation_text = (
            "Create a practical professional post with concise, "
            "specific code examples. Avoid generic motivational content."
        )
        reasoning = (
            "Hindsight recalled that this audience responded strongly "
            "to practical content and concise code examples."
        )
    else:
        recommendation_text = (
            "Use specific, audience-focused content based on previously "
            "observed engagement patterns."
        )
        reasoning = (
            "The recommendation was generated from the audience memories "
            "returned by Hindsight."
        )

    return {
        "recommendation": recommendation_text,
        "reasoning": reasoning,
        "based_on_memory": memories,
    }