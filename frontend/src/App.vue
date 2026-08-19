<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'

import { api } from './api'
import DisciplineMap from './components/DisciplineMap.vue'
import StaticsTheoryPage from './components/StaticsTheoryPage.vue'
import SubjectPanel from './components/SubjectPanel.vue'
import type { Discipline, SubjectDetail, SubjectNode, TheoryDetail, TheoryNode } from './types'

const disciplines = ref<Discipline[]>([])
const selectedDiscipline = ref<Discipline | null>(null)
const selectedSubject = ref<SubjectNode | null>(null)
const detail = ref<SubjectDetail | null>(null)
const theoryDetail = ref<TheoryDetail | null>(null)
const isLoading = ref(true)
const error = ref('')

const selectedSubjectId = computed(() => selectedSubject.value?.id ?? null)
const staticsTheoryIndex = computed(() =>
  detail.value?.id === 'statics' ? detail.value.theories : [],
)

function theoryIdFromPath() {
  return window.location.pathname.match(/^\/theories\/([a-z0-9-]+)\/?$/)?.[1] ?? null
}

async function loadCatalog() {
  isLoading.value = true
  error.value = ''
  try {
    disciplines.value = await api.listDisciplines()
    const mechanics = disciplines.value.find((item) => item.id === 'mechanics')
    const statics = mechanics?.subjects.find((item) => item.id === 'statics')
    const dynamics = mechanics?.subjects.find((item) => item.id === 'dynamics')
    const routeTheoryId = theoryIdFromPath()

    if (routeTheoryId && mechanics && statics) {
      await selectSubject(mechanics, statics, false)
      await openTheoryById(routeTheoryId, false)
    } else if (mechanics && dynamics) {
      await selectSubject(mechanics, dynamics, false)
    }
  } catch {
    error.value = '无法连接内容服务。请确认 Python API 已在 8000 端口启动。'
  } finally {
    isLoading.value = false
  }
}

async function selectSubject(discipline: Discipline, subject: SubjectNode, updateHistory = true) {
  selectedDiscipline.value = discipline
  selectedSubject.value = subject
  detail.value = null
  theoryDetail.value = null
  error.value = ''

  if (updateHistory && window.location.pathname !== '/') {
    window.history.pushState({}, '', '/')
  }

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

async function openTheoryById(theoryId: string, updateHistory = true) {
  error.value = ''
  try {
    theoryDetail.value = await api.getTheory(theoryId)
    if (updateHistory && window.location.pathname !== `/theories/${theoryId}`) {
      window.history.pushState({}, '', `/theories/${theoryId}`)
    }
    window.scrollTo({ top: 0, behavior: 'smooth' })
  } catch {
    theoryDetail.value = null
    error.value = '理论页面读取失败，请确认链接是否正确。'
  }
}

function openTheory(theory: TheoryNode) {
  void openTheoryById(theory.id)
}

async function backToStatics() {
  const mechanics = disciplines.value.find((item) => item.id === 'mechanics')
  const statics = mechanics?.subjects.find((item) => item.id === 'statics')
  if (!mechanics || !statics) return

  await selectSubject(mechanics, statics)
  requestAnimationFrame(() => {
    document.querySelector('.statics-catalog')?.scrollIntoView({ behavior: 'smooth' })
  })
}

function goHome() {
  theoryDetail.value = null
  if (window.location.pathname !== '/') window.history.pushState({}, '', '/')
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handlePopState() {
  const theoryId = theoryIdFromPath()
  if (theoryId) void openTheoryById(theoryId, false)
  else theoryDetail.value = null
}

onMounted(() => {
  window.addEventListener('popstate', handlePopState)
  void loadCatalog()
})

onBeforeUnmount(() => window.removeEventListener('popstate', handlePopState))
</script>

<template>
  <div class="app-shell">
    <header class="site-header">
      <a class="brand" href="/" aria-label="返回首页" @click.prevent="goHome">
        <span class="brand__mark"><i /><i /><i /></span>
        <span><strong>物理原场</strong><small>PHYSICAL THEORY</small></span>
      </a>
      <div class="site-header__meta">
        <span>{{ theoryDetail ? '静力学理论专题' : '交互式物理图谱' }}</span>
        <i />
        <span>V0.1</span>
      </div>
    </header>

    <main id="top">
      <StaticsTheoryPage
        v-if="theoryDetail"
        :key="theoryDetail.id"
        :theory="theoryDetail"
        :theory-index="staticsTheoryIndex"
        @back="backToStatics"
        @open-theory="openTheory"
      />

      <template v-else>
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
        @open-theory="openTheory"
      />
      <section v-else-if="selectedSubject" class="coming-soon">
        <span>CONTENT IN PROGRESS</span>
        <h2>{{ selectedSubject.name }}</h2>
        <p>{{ selectedSubject.summary }}</p>
        <div>该节点的理论文章、动画与应用案例将在后续迭代中加入。</div>
      </section>
      </template>
    </main>

    <footer>
      <span>PHYSICAL THEORY · OPEN LEARNING PROJECT</span>
      <span>用图像、运动与实验理解公式</span>
    </footer>
  </div>
</template>
