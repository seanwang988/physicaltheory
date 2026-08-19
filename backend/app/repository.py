from app.data.catalog import DETAILS, DISCIPLINES
from app.data.statics_theories import STATICS_THEORIES, STATICS_THEORY_NODES
from app.models import Discipline, SubjectDetail, TheoryDetail, TheoryNode


def list_disciplines() -> list[Discipline]:
    return DISCIPLINES


def get_subject(subject_id: str) -> SubjectDetail | None:
    return DETAILS.get(subject_id)


def list_subject_theories(subject_id: str) -> list[TheoryNode] | None:
    if subject_id == "statics":
        return STATICS_THEORY_NODES
    if subject_id not in DETAILS:
        return None
    return []


def get_theory(theory_id: str) -> TheoryDetail | None:
    return STATICS_THEORIES.get(theory_id)
