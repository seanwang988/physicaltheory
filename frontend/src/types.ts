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

export interface SubjectDetail extends SubjectNode {
  discipline_id: string
  introduction: string
  sections: TheorySection[]
  formulas: Formula[]
  applications: string[]
  animation: AnimationSpec
}
