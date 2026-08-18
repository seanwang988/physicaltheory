<script setup lang="ts">
import type { Discipline, SubjectNode } from '../types'

const { disciplines, selectedSubjectId } = defineProps<{
  disciplines: Discipline[]
  selectedSubjectId: string | null
}>()

const emit = defineEmits<{
  select: [discipline: Discipline, subject: SubjectNode]
}>()
</script>

<template>
  <nav class="discipline-map" aria-label="物理学科目录">
    <article
      v-for="(discipline, index) in disciplines"
      :key="discipline.id"
      class="discipline-card"
      :style="{ '--accent': discipline.color, '--delay': `${index * 80}ms` }"
    >
      <header class="discipline-card__header">
        <span class="discipline-card__index">0{{ index + 1 }}</span>
        <div>
          <p>{{ discipline.english_name }}</p>
          <h2>{{ discipline.name }}</h2>
        </div>
        <span class="discipline-card__glyph" aria-hidden="true">{{ discipline.icon }}</span>
      </header>

      <p class="discipline-card__summary">{{ discipline.summary }}</p>

      <div class="subject-list">
        <button
          v-for="subject in discipline.subjects"
          :key="subject.id"
          class="subject-node"
          :class="{ 'subject-node--active': subject.id === selectedSubjectId }"
          type="button"
          @click="emit('select', discipline, subject)"
        >
          <span class="subject-node__dot" />
          <span>
            <strong>{{ subject.name }}</strong>
            <small>{{ subject.english_name }}</small>
          </span>
          <span v-if="subject.status === 'planned'" class="subject-node__status">待扩展</span>
          <svg viewBox="0 0 20 20" aria-hidden="true">
            <path d="m7 4 6 6-6 6" />
          </svg>
        </button>
      </div>
    </article>
  </nav>
</template>
