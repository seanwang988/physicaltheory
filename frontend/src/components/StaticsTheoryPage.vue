<script setup lang="ts">
import { computed } from 'vue'

import type { ScientistProfile, TheoryDetail, TheoryNode } from '../types'
import StaticsExperimentLab from './StaticsExperimentLab.vue'

const { theory, theoryIndex } = defineProps<{
  theory: TheoryDetail
  theoryIndex: TheoryNode[]
}>()

const emit = defineEmits<{
  back: []
  openTheory: [theory: TheoryNode]
}>()

const relatedTheories = computed(() =>
  theory.related_theory_ids
    .map((id) => theoryIndex.find((item) => item.id === id))
    .filter((item): item is TheoryNode => Boolean(item)),
)

function initials(scientist: ScientistProfile) {
  return scientist.original_name
    .split(' ')
    .map((part) => part[0])
    .join('')
    .slice(0, 2)
}
</script>

<template>
  <article class="theory-page">
    <nav class="theory-breadcrumb" aria-label="页面路径">
      <button type="button" @click="emit('back')">物理学</button>
      <span>/</span>
      <button type="button" @click="emit('back')">静力学</button>
      <span>/</span>
      <strong>{{ theory.name }}</strong>
    </nav>

    <header class="theory-hero">
      <div class="theory-hero__meta">
        <span>STATICS · THEORY 0{{ theory.order }}</span>
        <i />
        <span>{{ theory.english_name }}</span>
      </div>
      <p class="theory-hero__tagline">{{ theory.tagline }}</p>
      <h1>{{ theory.name }}</h1>
      <p class="theory-hero__intro">{{ theory.introduction }}</p>
      <div class="theory-hero__scroll"><span />向下探索理论与实验</div>
    </header>

    <section class="theory-section theory-section--concept">
      <div class="theory-section__heading">
        <span>01</span>
        <div><small>CORE THEORY</small><h2>理论原理</h2></div>
      </div>
      <div class="concept-layout">
        <div class="concept-copy">
          <section v-for="section in theory.sections" :key="section.title">
            <h3>{{ section.title }}</h3>
            <p v-for="paragraph in section.paragraphs" :key="paragraph">{{ paragraph }}</p>
          </section>
        </div>
        <aside class="equation-panel">
          <p>MECHANICAL FORMULAS</p>
          <div v-for="formula in theory.formulas" :key="formula.expression">
            <strong>{{ formula.expression }}</strong>
            <span>{{ formula.description }}</span>
          </div>
        </aside>
      </div>
    </section>

    <section class="theory-section">
      <div class="theory-section__heading">
        <span>02</span>
        <div><small>INTERACTIVE EXPERIMENT</small><h2>{{ theory.experiment.title }}</h2></div>
      </div>
      <div class="experiment-intro">
        <p>{{ theory.experiment.description }}</p>
        <div><small>实验原理</small><span>{{ theory.experiment.principle }}</span></div>
      </div>
      <StaticsExperimentLab :key="theory.id" :experiment="theory.experiment" />
    </section>

    <section class="theory-section">
      <div class="theory-section__heading">
        <span>03</span>
        <div><small>REAL-WORLD APPLICATIONS</small><h2>理论应用</h2></div>
      </div>
      <div class="application-grid">
        <article v-for="(application, index) in theory.applications" :key="application.title">
          <span>0{{ index + 1 }}</span>
          <h3>{{ application.title }}</h3>
          <p>{{ application.description }}</p>
        </article>
      </div>
    </section>

    <section class="theory-section">
      <div class="theory-section__heading">
        <span>04</span>
        <div><small>PEOPLE BEHIND THE THEORY</small><h2>相关科学家</h2></div>
      </div>
      <div class="scientist-list">
        <article v-for="scientist in theory.scientists" :key="scientist.original_name">
          <div class="scientist-avatar" aria-hidden="true">
            <span>{{ initials(scientist) }}</span>
            <i /><i />
          </div>
          <div class="scientist-copy">
            <small>{{ scientist.period }} · {{ scientist.field }}</small>
            <h3>{{ scientist.name }} <span>{{ scientist.original_name }}</span></h3>
            <strong>{{ scientist.contribution }}</strong>
            <p>{{ scientist.introduction }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="related-section">
      <div><small>CONTINUE EXPLORING</small><h2>继续探索静力学</h2></div>
      <div class="related-links">
        <button
          v-for="related in relatedTheories"
          :key="related.id"
          type="button"
          @click="emit('openTheory', related)"
        >
          <span>0{{ related.order }}</span>
          <strong>{{ related.name }}</strong>
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="m7 4 6 6-6 6" /></svg>
        </button>
      </div>
    </section>
  </article>
</template>

<style scoped>
.theory-page { margin: 0 calc(50% - 50vw); padding: 0 max(24px, calc((100vw - 1400px) / 2)); background: #15231f; color: #edf1e8; animation: enter 380ms ease-out; }
@keyframes enter { from { opacity: 0; transform: translateY(8px); } }
.theory-breadcrumb { min-height: 68px; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.13); color: #78857f; font-size: 10px; letter-spacing: 0.08em; }
.theory-breadcrumb button { padding: 0; border: 0; background: transparent; color: #aab5af; cursor: pointer; }
.theory-breadcrumb button:hover { color: #ff8b64; }
.theory-breadcrumb strong { color: #ff8257; font-weight: 500; }
.theory-hero { min-height: 680px; padding: 112px 0 80px; position: relative; display: flex; flex-direction: column; justify-content: center; }
.theory-hero::after { position: absolute; top: 80px; right: 2%; width: 340px; aspect-ratio: 1; content: ''; border: 1px solid rgba(255, 107, 53, 0.16); border-radius: 50%; box-shadow: inset 0 0 0 70px rgba(255, 255, 255, 0.012), inset 0 0 0 140px rgba(255, 107, 53, 0.012); }
.theory-hero__meta { display: flex; align-items: center; gap: 12px; color: #ff8257; font-size: 10px; letter-spacing: 0.15em; }
.theory-hero__meta i { width: 36px; height: 1px; background: currentColor; }
.theory-hero__tagline { margin: 70px 0 13px; color: #8f9b95; font-size: 13px; letter-spacing: 0.12em; }
.theory-hero h1 { position: relative; z-index: 1; max-width: 1080px; margin: 0; font-size: clamp(62px, 9vw, 132px); line-height: 0.95; letter-spacing: -0.065em; }
.theory-hero__intro { max-width: 790px; margin: 38px 0 0; color: #a8b3ad; font-size: 18px; line-height: 1.9; }
.theory-hero__scroll { position: absolute; right: 0; bottom: 55px; display: flex; align-items: center; gap: 10px; color: #69766f; font-size: 9px; letter-spacing: 0.1em; }
.theory-hero__scroll span { width: 42px; height: 1px; background: #ff6b35; }
.theory-section { padding: 90px 0 110px; border-top: 1px solid rgba(255, 255, 255, 0.14); }
.theory-section__heading { display: flex; gap: 19px; align-items: flex-start; margin-bottom: 48px; }
.theory-section__heading > span { margin-top: 6px; color: #ff6b35; font-size: 10px; }
.theory-section__heading small, .related-section small { color: #76837c; font-size: 9px; letter-spacing: 0.17em; }
.theory-section__heading h2, .related-section h2 { margin: 3px 0 0; font-size: 36px; letter-spacing: -0.04em; }
.concept-layout { display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 90px; padding-left: 38px; }
.concept-copy section + section { margin-top: 38px; }
.concept-copy h3 { margin: 0 0 15px; font-size: 20px; }
.concept-copy p { margin: 0 0 12px; color: #a7b2ac; line-height: 1.95; }
.equation-panel { align-self: start; padding: 28px; border: 1px solid rgba(255, 255, 255, 0.17); background: rgba(255, 255, 255, 0.025); }
.equation-panel > p { margin: 0 0 18px; color: #74817a; font-size: 9px; letter-spacing: 0.15em; }
.equation-panel > div { padding: 22px 0; border-top: 1px solid rgba(255, 255, 255, 0.11); }
.equation-panel strong, .equation-panel span { display: block; }
.equation-panel strong { margin-bottom: 9px; color: #ff845b; font-family: Georgia, serif; font-size: 28px; font-weight: 400; font-style: italic; }
.equation-panel span { color: #a4afa9; font-size: 12px; line-height: 1.6; }
.experiment-intro { margin: -20px 0 36px 38px; display: grid; grid-template-columns: 1fr 1fr; gap: 44px; color: #a4afa9; line-height: 1.75; }
.experiment-intro > p { margin: 0; }
.experiment-intro > div { display: grid; gap: 6px; padding-left: 20px; border-left: 2px solid #ff6b35; }
.experiment-intro small { color: #ff8962; font-size: 9px; letter-spacing: 0.12em; }
.application-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; margin-left: 38px; background: rgba(255, 255, 255, 0.13); }
.application-grid article { min-height: 230px; padding: 26px; background: #182722; }
.application-grid span { color: #ff7e52; font-size: 10px; }
.application-grid h3 { margin: 57px 0 12px; font-size: 19px; }
.application-grid p { margin: 0; color: #929f98; font-size: 13px; line-height: 1.75; }
.scientist-list { margin-left: 38px; border-top: 1px solid rgba(255, 255, 255, 0.13); }
.scientist-list article { padding: 38px 0; display: grid; grid-template-columns: 150px 1fr; gap: 38px; border-bottom: 1px solid rgba(255, 255, 255, 0.13); }
.scientist-avatar { position: relative; width: 118px; height: 118px; display: grid; place-items: center; border: 1px solid rgba(255, 107, 53, 0.45); border-radius: 50%; color: #ff8358; font-family: Georgia, serif; font-size: 31px; }
.scientist-avatar i { position: absolute; inset: 13px -9px; border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 50%; transform: rotate(55deg); }
.scientist-avatar i:last-child { transform: rotate(-55deg); }
.scientist-copy small { color: #7c8982; font-size: 9px; letter-spacing: 0.1em; }
.scientist-copy h3 { margin: 8px 0 14px; font-size: 25px; }
.scientist-copy h3 span { margin-left: 8px; color: #7f8d85; font-size: 13px; font-weight: 400; }
.scientist-copy > strong { display: block; color: #e2e8e4; font-size: 13px; line-height: 1.7; }
.scientist-copy p { max-width: 860px; margin: 14px 0 0; color: #9ca8a1; line-height: 1.85; }
.related-section { padding: 85px 0 110px; display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 60px; border-top: 1px solid rgba(255, 255, 255, 0.14); }
.related-links { border-top: 1px solid rgba(255, 255, 255, 0.15); }
.related-links button { width: 100%; min-height: 76px; padding: 0 10px; display: grid; grid-template-columns: 34px 1fr auto; align-items: center; gap: 14px; border: 0; border-bottom: 1px solid rgba(255, 255, 255, 0.15); background: transparent; color: #edf1e8; text-align: left; cursor: pointer; }
.related-links button:hover { background: rgba(255, 107, 53, 0.06); }
.related-links button > span { color: #ff8157; font-size: 10px; }
.related-links svg { width: 18px; fill: none; stroke: #ff8157; stroke-width: 1.5; }
@media (max-width: 900px) { .concept-layout { grid-template-columns: 1fr; gap: 45px; } .application-grid { grid-template-columns: 1fr; } .application-grid article { min-height: 160px; } .related-section { grid-template-columns: 1fr; } }
@media (max-width: 640px) { .theory-hero { min-height: 610px; padding-top: 80px; } .theory-hero::after { width: 230px; top: 115px; } .theory-hero__tagline { margin-top: 52px; } .theory-hero__scroll { display: none; } .theory-section { padding: 70px 0 85px; } .concept-layout, .application-grid, .scientist-list { margin-left: 0; padding-left: 0; } .experiment-intro { margin-left: 0; grid-template-columns: 1fr; } .scientist-list article { grid-template-columns: 1fr; } .scientist-avatar { width: 92px; height: 92px; font-size: 25px; } }
</style>
