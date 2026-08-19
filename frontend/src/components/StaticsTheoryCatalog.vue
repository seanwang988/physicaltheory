<script setup lang="ts">
import type { StaticsExperimentKind, TheoryNode } from '../types'

defineProps<{
  theories: TheoryNode[]
}>()

const emit = defineEmits<{
  openTheory: [theory: TheoryNode]
}>()

const experimentLabels: Record<StaticsExperimentKind, string> = {
  'force-table': '力桌实验',
  'free-body': '悬挂实验',
  lever: '杠杆实验',
  stability: '倾覆实验',
  friction: '斜面实验',
  truss: '桁架实验',
}
</script>

<template>
  <section class="statics-catalog">
    <header class="statics-catalog__header">
      <div>
        <p>STATICS KNOWLEDGE PATH</p>
        <h2>静力学理论专题</h2>
      </div>
      <span>06 个理论 · 06 组交互实验</span>
    </header>

    <div class="statics-catalog__grid">
      <button
        v-for="theory in theories"
        :key="theory.id"
        class="theory-card"
        type="button"
        @click="emit('openTheory', theory)"
      >
        <span class="theory-card__number">0{{ theory.order }}</span>
        <div class="theory-card__copy">
          <small>{{ theory.english_name }}</small>
          <h3>{{ theory.name }}</h3>
          <p>{{ theory.summary }}</p>
        </div>
        <div class="theory-card__footer">
          <span>{{ experimentLabels[theory.experiment_kind] }}</span>
          <svg viewBox="0 0 28 28" aria-hidden="true">
            <circle cx="14" cy="14" r="13" />
            <path d="m11 8 6 6-6 6" />
          </svg>
        </div>
      </button>
    </div>
  </section>
</template>

<style scoped>
.statics-catalog {
  padding: 76px 0 90px;
  border-top: 1px solid rgba(255, 255, 255, 0.14);
}

.statics-catalog__header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 32px;
  margin-bottom: 38px;
}

.statics-catalog__header p {
  margin: 0 0 5px;
  color: #7e8b84;
  font-size: 10px;
  letter-spacing: 0.17em;
}

.statics-catalog__header h2 {
  margin: 0;
  font-size: 36px;
  letter-spacing: -0.04em;
}

.statics-catalog__header > span {
  color: #8f9b95;
  font-size: 11px;
  letter-spacing: 0.08em;
}

.statics-catalog__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.14);
}

.theory-card {
  min-height: 300px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  border: 0;
  background: #1a2a25;
  color: #edf1e8;
  text-align: left;
  cursor: pointer;
  transition: background 180ms ease, transform 180ms ease;
}

.theory-card:hover {
  z-index: 1;
  background: #22362f;
  transform: translateY(-3px);
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.24);
}

.theory-card__number {
  color: #ff6b35;
  font-size: 10px;
}

.theory-card__copy {
  margin-top: 36px;
}

.theory-card small {
  color: #75847d;
  font-size: 9px;
  letter-spacing: 0.13em;
  text-transform: uppercase;
}

.theory-card h3 {
  margin: 7px 0 15px;
  font-size: 22px;
  letter-spacing: -0.03em;
}

.theory-card p {
  margin: 0;
  color: #9aa7a1;
  font-size: 13px;
  line-height: 1.75;
}

.theory-card__footer {
  margin-top: auto;
  padding-top: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #ff8b62;
  font-size: 10px;
  letter-spacing: 0.08em;
}

.theory-card svg {
  width: 28px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.2;
}

@media (max-width: 900px) {
  .statics-catalog__grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 620px) {
  .statics-catalog__header { align-items: start; flex-direction: column; }
  .statics-catalog__grid { grid-template-columns: 1fr; }
  .theory-card { min-height: 250px; }
}
</style>
