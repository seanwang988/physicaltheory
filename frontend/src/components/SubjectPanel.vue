<script setup lang="ts">
import type { Discipline, SubjectDetail } from '../types'
import ForceMotionLab from './ForceMotionLab.vue'

defineProps<{
  discipline: Discipline
  detail: SubjectDetail
}>()
</script>

<template>
  <article class="subject-panel" :style="{ '--accent': discipline.color }">
    <header class="subject-hero">
      <div class="eyebrow">
        <span>{{ discipline.name }}</span>
        <i />
        <span>{{ detail.english_name }}</span>
      </div>
      <h1>{{ detail.name }}</h1>
      <p>{{ detail.introduction }}</p>
    </header>

    <section class="content-block">
      <div class="section-heading">
        <span>01</span>
        <div><p>THEORY</p><h2>理论原理</h2></div>
      </div>
      <div class="theory-grid">
        <div class="theory-copy">
          <section v-for="section in detail.sections" :key="section.title">
            <h3>{{ section.title }}</h3>
            <p v-for="paragraph in section.paragraphs" :key="paragraph">{{ paragraph }}</p>
          </section>
        </div>
        <aside class="formula-board">
          <p class="formula-board__label">核心公式 / EQUATIONS</p>
          <div v-for="formula in detail.formulas" :key="formula.expression" class="formula">
            <strong>{{ formula.expression }}</strong>
            <span>{{ formula.description }}</span>
          </div>
        </aside>
      </div>
    </section>

    <section class="content-block">
      <div class="section-heading">
        <span>02</span>
        <div><p>INTERACTIVE LAB</p><h2>{{ detail.animation.title }}</h2></div>
      </div>
      <p class="section-intro">{{ detail.animation.description }}</p>
      <ForceMotionLab v-if="detail.animation.kind === 'force-motion'" />
    </section>

    <section class="content-block">
      <div class="section-heading">
        <span>03</span>
        <div><p>APPLICATIONS</p><h2>实际应用</h2></div>
      </div>
      <div class="applications">
        <div v-for="(application, index) in detail.applications" :key="application">
          <span>0{{ index + 1 }}</span>
          <p>{{ application }}</p>
        </div>
      </div>
    </section>
  </article>
</template>
