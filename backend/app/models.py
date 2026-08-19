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


class TheoryNode(BaseModel):
    id: str
    subject_id: str
    name: str
    english_name: str
    summary: str
    order: int
    experiment_kind: str


class ExperimentSpec(BaseModel):
    kind: Literal["force-table", "free-body", "lever", "stability", "friction", "truss"]
    title: str
    description: str
    principle: str
    observation: str
    controls: list[str] = Field(default_factory=list)


class ApplicationCase(BaseModel):
    title: str
    description: str


class ScientistProfile(BaseModel):
    name: str
    original_name: str
    period: str
    field: str
    contribution: str
    introduction: str


class TheoryDetail(TheoryNode):
    tagline: str
    introduction: str
    sections: list[TheorySection]
    formulas: list[Formula]
    experiment: ExperimentSpec
    applications: list[ApplicationCase]
    scientists: list[ScientistProfile]
    related_theory_ids: list[str] = Field(default_factory=list)


class SubjectDetail(SubjectNode):
    discipline_id: str
    introduction: str
    sections: list[TheorySection]
    formulas: list[Formula]
    applications: list[str]
    animation: AnimationSpec
    theories: list[TheoryNode] = Field(default_factory=list)


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
