import type { Discipline, SubjectDetail } from './types'

class ApiError extends Error {
  constructor(
    message: string,
    readonly status: number,
  ) {
    super(message)
  }
}

async function request<T>(path: string): Promise<T> {
  const response = await fetch(path)
  if (!response.ok) {
    const body = (await response.json().catch(() => null)) as { detail?: string } | null
    throw new ApiError(body?.detail ?? '请求失败，请稍后重试', response.status)
  }
  return response.json() as Promise<T>
}

export const api = {
  listDisciplines: () => request<Discipline[]>('/api/disciplines'),
  getSubject: (subjectId: string) => request<SubjectDetail>(`/api/subjects/${subjectId}`),
}
