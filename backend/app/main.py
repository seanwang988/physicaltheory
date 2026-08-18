from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import Discipline, HealthResponse, SubjectDetail
from app.repository import get_subject, list_disciplines

app = FastAPI(
    title="Physical Theory API",
    version="0.1.0",
    description="Interactive physics learning content API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="physical-theory-api")


@app.get("/api/disciplines", response_model=list[Discipline], tags=["content"])
def disciplines() -> list[Discipline]:
    return list_disciplines()


@app.get("/api/subjects/{subject_id}", response_model=SubjectDetail, tags=["content"])
def subject_detail(subject_id: str) -> SubjectDetail:
    subject = get_subject(subject_id)
    if subject is None:
        raise HTTPException(status_code=404, detail="该学科内容尚未发布")
    return subject
