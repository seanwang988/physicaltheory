<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

import { api } from './api'
import DisciplineMap from './components/DisciplineMap.vue'
import SubjectPanel from './components/SubjectPanel.vue'
import type { Discipline, SubjectDetail, SubjectNode } from './types'

const disciplines = ref<Discipline[]>([])
const selectedDiscipline = ref<Discipline | null>(null)
const selectedSubject = ref<SubjectNode | null>(null)
const detail = ref<SubjectDetail | null>(null)
const isLoading = ref(true)
const error = ref('')

const selectedSubjectId = computed(() => selectedSubject.value?.id ?? null)

async function loadCatalog() {
  isLoading.value = true
  error.value = ''
  try {
    disciplines.value = await api.listDisciplines()
    const mechanics = disciplines.value.find((item) => item.id === 'mechanics')
    const dynamics = mechanics?.subjects.find((item) => item.id === 'dynamics')
    if (mechanics && dynamics) await selectSubject(mechanics, dynamics)
  } catch {
    error.value = '无法连接内容服务。请确认 Python API 已在 8000 端口启动。'
  } finally {
    isLoading.value = false
  }
}

async function selectSubject(discipline: Discipline, subject: SubjectNode) {
  selectedDiscipline.value = discipline
  selectedSubject.value = subject
  detail.value = null
  error.value = ''

  if (subject.status === 'planned') {
    window.scrollTo({ top: 0, behavior: 'smooth' })
    return
  }

  try {
    detail.value = await api.getSubject(subject.id)
  } catch {
    error.value = '内容读取失败，请稍后重试。'
  }
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(loadCatalog)
</script>

<template>
  <div class="app-shell">
    <header class="site-header">
      <a class="brand" href="#top" aria-label="返回首页">
        <span class="brand__mark"><i /><i /><i /></span>
        <span><strong>物理原场</strong><small>PHYSICAL THEORY</small></span>
      </a>
      <div class="site-header__meta">
        <span>交互式物理图谱</span>
        <i />
        <span>V0.1</span>
      </div>
    </header>

    <main id="top">
      <section class="catalog-hero">
        <div class="catalog-hero__copy">
          <p class="eyebrow"><span>EXPLORE THE LAWS</span><i /><span>理解世界的运行方式</span></p>
          <h1>从一个节点<br />进入<span>物理世界</span></h1>
          <p>选择学科，阅读核心理论，通过可控动画观察规律，并发现物理学如何改变现实生活。</p>
        </div>
        <div class="catalog-hero__orbit" aria-hidden="true">
          <span class="orbit orbit--one"><i /></span>
          <span class="orbit orbit--two"><i /></span>
          <b>φ</b>
        </div>
      </section>

      <div v-if="isLoading" class="state-card">正在建立物理图谱…</div>
      <div v-else-if="error && disciplines.length === 0" class="state-card state-card--error">
        <p>{{ error }}</p>
        <button class="button button--primary" type="button" @click="loadCatalog">重新连接</button>
      </div>
      <DisciplineMap
        v-else
        :disciplines
        :selected-subject-id
        @select="selectSubject"
      />

      <div v-if="error && disciplines.length" class="state-card state-card--error">{{ error }}</div>
      <SubjectPanel
        v-else-if="detail && selectedDiscipline"
        :key="detail.id"
        :discipline="selectedDiscipline"
        :detail
      />
      <section v-else-if="selectedSubject" class="coming-soon">
        <span>CONTENT IN PROGRESS</span>
        <h2>{{ selectedSubject.name }}</h2>
        <p>{{ selectedSubject.summary }}</p>
        <div>该节点的理论文章、动画与应用案例将在后续迭代中加入。</div>
      </section>
    </main>

    <footer>
      <span>PHYSICAL THEORY · OPEN LEARNING PROJECT</span>
      <span>用图像、运动与实验理解公式</span>
    </footer>
  </div>
</template>
