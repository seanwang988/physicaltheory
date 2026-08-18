from typing import Literal

from pydantic import BaseModel, Field

ContentStatus = Literal["ready", "planned"]


class SubjectNode(BaseModel):
    id: str
    name: str
    english_name: str
    summary: str
    status: ContentStatus


class Discipline(BaseModel):
    id: str
    name: str
    english_name: str
    color: str
    icon: str
    summary: str
    subjects: list[SubjectNode]


class Formula(BaseModel):
    expression: str
    description: str


class TheorySection(BaseModel):
    title: str
    paragraphs: list[str]


class AnimationSpec(BaseModel):
    kind: Literal["force-motion", "placeholder"]
    title: str
    description: str
    controls: list[str] = Field(default_factory=list)


class SubjectDetail(SubjectNode):
    discipline_id: str
    introduction: str
    sections: list[TheorySection]
    formulas: list[Formula]
    applications: list[str]
    animation: AnimationSpec


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
