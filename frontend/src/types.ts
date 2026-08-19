export type ContentStatus = 'ready' | 'planned'

export interface SubjectNode {
  id: string
  name: string
  english_name: string
  summary: string
  status: ContentStatus
}

export interface Discipline {
  id: string
  name: string
  english_name: string
  color: string
  icon: string
  summary: string
  subjects: SubjectNode[]
}

export interface Formula {
  expression: string
  description: string
}

export interface TheorySection {
  title: string
  paragraphs: string[]
}

export interface AnimationSpec {
  kind: 'force-motion' | 'placeholder'
  title: string
  description: string
  controls: string[]
}

export type StaticsExperimentKind =
  | 'force-table'
  | 'free-body'
  | 'lever'
  | 'stability'
  | 'friction'
  | 'truss'

export interface TheoryNode {
  id: string
  subject_id: string
  name: string
  english_name: string
  summary: string
  order: number
  experiment_kind: StaticsExperimentKind
}

export interface ExperimentSpec {
  kind: StaticsExperimentKind
  title: string
  description: string
  principle: string
  observation: string
  controls: string[]
}

export interface ApplicationCase {
  title: string
  description: string
}

export interface ScientistProfile {
  name: string
  original_name: string
  period: string
  field: string
  contribution: string
  introduction: string
}

export interface TheoryDetail extends TheoryNode {
  tagline: string
  introduction: string
  sections: TheorySection[]
  formulas: Formula[]
  experiment: ExperimentSpec
  applications: ApplicationCase[]
  scientists: ScientistProfile[]
  related_theory_ids: string[]
}

export interface SubjectDetail extends SubjectNode {
  discipline_id: string
  introduction: string
  sections: TheorySection[]
  formulas: Formula[]
  applications: string[]
  animation: AnimationSpec
  theories: TheoryNode[]
}
