from app.data.catalog import DETAILS, DISCIPLINES
from app.models import Discipline, SubjectDetail


def list_disciplines() -> list[Discipline]:
    return DISCIPLINES


def get_subject(subject_id: str) -> SubjectDetail | None:
    return DETAILS.get(subject_id)
