from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import Discipline, HealthResponse, SubjectDetail, TheoryDetail, TheoryNode
from app.repository import get_subject, get_theory, list_disciplines, list_subject_theories

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


@app.get("/api/subjects/{subject_id}/theories", response_model=list[TheoryNode], tags=["content"])
def subject_theories(subject_id: str) -> list[TheoryNode]:
    theories = list_subject_theories(subject_id)
    if theories is None:
        raise HTTPException(status_code=404, detail="该学科内容尚未发布")
    return theories


@app.get("/api/theories/{theory_id}", response_model=TheoryDetail, tags=["content"])
def theory_detail(theory_id: str) -> TheoryDetail:
    theory = get_theory(theory_id)
    if theory is None:
        raise HTTPException(status_code=404, detail="该理论内容不存在")
    return theory
