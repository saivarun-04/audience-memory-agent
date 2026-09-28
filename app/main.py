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
        "message": "Experience stored in audience memory.",
    }