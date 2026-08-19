<script setup lang="ts">
import { computed, ref } from 'vue'

import type { ExperimentSpec } from '../types'

defineProps<{
  experiment: ExperimentSpec
}>()

const forceA = ref(40)
const forceB = ref(30)
const vectorAngle = ref(60)
const mass = ref(10)
const ropeAngle = ref(45)
const leftForce = ref(40)
const leftArm = ref(3)
const rightForce = ref(30)
const rightArm = ref(4)
const baseWidth = ref(90)
const cgOffset = ref(0)
const cgHeight = ref(70)
const inclineAngle = ref(20)
const frictionCoefficient = ref(0.45)
const frictionMass = ref(5)
const trussLoad = ref(60)
const trussSpan = ref(8)
const trussHeight = ref(3)

const radians = computed(() => (vectorAngle.value * Math.PI) / 180)
const resultant = computed(() =>
  Math.sqrt(
    forceA.value ** 2 +
      forceB.value ** 2 +
      2 * forceA.value * forceB.value * Math.cos(radians.value),
  ),
)
const resultantAngle = computed(
  () =>
    (Math.atan2(forceB.value * Math.sin(radians.value), forceA.value + forceB.value * Math.cos(radians.value)) *
      180) /
    Math.PI,
)
const vectorBX = computed(() => 200 + forceB.value * 2 * Math.cos(radians.value))
const vectorBY = computed(() => 170 - forceB.value * 2 * Math.sin(radians.value))
const resultantX = computed(() => 200 + forceA.value * 2 + forceB.value * 2 * Math.cos(radians.value))
const resultantY = computed(() => vectorBY.value)

const weight = computed(() => mass.value * 9.8)
const ropeTension = computed(
  () => weight.value / (2 * Math.sin((ropeAngle.value * Math.PI) / 180)),
)

const leftMoment = computed(() => leftForce.value * leftArm.value)
const rightMoment = computed(() => rightForce.value * rightArm.value)
const momentDifference = computed(() => leftMoment.value - rightMoment.value)
const beamRotation = computed(() => Math.max(-12, Math.min(12, momentDifference.value / 12)))
const leverBalanced = computed(() => Math.abs(momentDifference.value) < 3)

const stabilityLimit = computed(() => baseWidth.value / 2)
const isStable = computed(() => Math.abs(cgOffset.value) <= stabilityLimit.value)

const inclineRadians = computed(() => (inclineAngle.value * Math.PI) / 180)
const downhillForce = computed(() => frictionMass.value * 9.8 * Math.sin(inclineRadians.value))
const frictionLimit = computed(
  () => frictionCoefficient.value * frictionMass.value * 9.8 * Math.cos(inclineRadians.value),
)
const isSlipping = computed(() => downhillForce.value > frictionLimit.value)
const inclineEndX = computed(() => 100 + 220 * Math.cos(inclineRadians.value))
const inclineEndY = computed(() => 280 - 220 * Math.sin(inclineRadians.value))

const trussReaction = computed(() => trussLoad.value / 2)
const trussAngle = computed(() => Math.atan(trussHeight.value / (trussSpan.value / 2)))
const diagonalForce = computed(() => trussLoad.value / (2 * Math.sin(trussAngle.value)))
const trussApexY = computed(() => 270 - trussHeight.value * 48)
</script>

<template>
  <div class="statics-lab">
    <div class="statics-lab__stage">
      <svg v-if="experiment.kind === 'force-table'" viewBox="0 0 400 330" role="img" aria-label="力的合成动态图">
        <defs>
          <marker id="arrow-orange" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" /></marker>
          <marker id="arrow-green" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" /></marker>
        </defs>
        <circle class="guide" cx="200" cy="170" r="105" />
        <line class="axis" x1="55" y1="170" x2="350" y2="170" />
        <line class="force force--a" x1="200" y1="170" :x2="200 + forceA * 2" y2="170" marker-end="url(#arrow-orange)" />
        <line class="force force--b" x1="200" y1="170" :x2="vectorBX" :y2="vectorBY" marker-end="url(#arrow-orange)" />
        <line class="force force--result" x1="200" y1="170" :x2="resultantX" :y2="resultantY" marker-end="url(#arrow-green)" />
        <line class="construction" :x1="200 + forceA * 2" y1="170" :x2="resultantX" :y2="resultantY" />
        <line class="construction" :x1="vectorBX" :y1="vectorBY" :x2="resultantX" :y2="resultantY" />
        <text x="210" y="192">O</text><text :x="200 + forceA * 1.1" y="157">F₁</text><text :x="vectorBX - 18" :y="vectorBY - 10">F₂</text><text class="result-text" :x="resultantX - 8" :y="resultantY - 13">FR</text>
      </svg>

      <svg v-else-if="experiment.kind === 'free-body'" viewBox="0 0 400 330" role="img" aria-label="双绳悬挂受力动画">
        <defs><marker id="arrow-rope" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" /></marker></defs>
        <line class="ceiling" x1="55" y1="45" x2="345" y2="45" />
        <line class="rope" x1="70" y1="45" x2="200" y2="205" /><line class="rope" x1="330" y1="45" x2="200" y2="205" />
        <line class="force force--result" x1="200" y1="205" x2="145" y2="138" marker-end="url(#arrow-rope)" />
        <line class="force force--result" x1="200" y1="205" x2="255" y2="138" marker-end="url(#arrow-rope)" />
        <line class="force force--weight" x1="200" y1="235" x2="200" y2="302" marker-end="url(#arrow-rope)" />
        <rect class="hanging-mass" x="165" y="205" width="70" height="48" rx="3" />
        <text x="200" y="234" text-anchor="middle">{{ mass }} kg</text><text x="112" y="128">T</text><text x="276" y="128">T</text><text x="210" y="296">W</text>
      </svg>

      <svg v-else-if="experiment.kind === 'lever'" viewBox="0 0 400 330" role="img" aria-label="杠杆力矩平衡动画">
        <g class="lever-group" :transform="`rotate(${beamRotation} 200 180)`">
          <rect class="lever-beam" x="45" y="170" width="310" height="18" rx="4" />
          <line class="force force--weight" :x1="200 - leftArm * 38" y1="90" :x2="200 - leftArm * 38" y2="165" />
          <circle class="weight" :cx="200 - leftArm * 38" cy="82" :r="12 + leftForce / 8" />
          <line class="force force--weight" :x1="200 + rightArm * 32" y1="90" :x2="200 + rightArm * 32" y2="165" />
          <circle class="weight" :cx="200 + rightArm * 32" cy="82" :r="12 + rightForce / 8" />
        </g>
        <path class="fulcrum" d="M200 182 L170 260 L230 260 Z" />
        <line class="ground" x1="125" y1="261" x2="275" y2="261" />
        <text x="60" y="300">ML = {{ leftMoment }} N·m</text><text x="245" y="300">MR = {{ rightMoment }} N·m</text>
      </svg>

      <svg v-else-if="experiment.kind === 'stability'" viewBox="0 0 400 330" role="img" aria-label="重心稳定性动画">
        <line class="ground" x1="35" y1="285" x2="365" y2="285" />
        <rect class="support" :x="200 - baseWidth * 0.8" y="269" :width="baseWidth * 1.6" height="16" />
        <g :class="{ tipping: !isStable }" :transform="`translate(${cgOffset * 1.6} 0)`">
          <rect class="body-block" x="150" :y="250 - cgHeight * 1.6" width="100" :height="cgHeight * 1.6" rx="4" />
          <circle class="center-of-gravity" cx="200" :cy="250 - cgHeight * 0.8" r="7" />
          <line class="gravity-line" x1="200" :y1="250 - cgHeight * 0.8" x2="200" y2="285" />
          <text x="212" :y="244 - cgHeight * 0.8">CG</text>
        </g>
        <text x="200" y="315" text-anchor="middle">支撑边界 ±{{ stabilityLimit.toFixed(0) }} cm</text>
      </svg>

      <svg v-else-if="experiment.kind === 'friction'" viewBox="0 0 400 330" role="img" aria-label="静摩擦斜面动画">
        <line class="incline" x1="100" y1="280" :x2="inclineEndX" :y2="inclineEndY" />
        <path class="incline-fill" :d="`M100 280 L${inclineEndX} ${inclineEndY} L${inclineEndX} 280 Z`" />
        <g class="friction-block" :class="{ 'friction-block--slipping': isSlipping }" :transform="`translate(${190 + inclineAngle * 0.35} ${245 - inclineAngle * 1.55}) rotate(${-inclineAngle})`">
          <rect x="-27" y="-35" width="54" height="35" rx="3" />
          <text x="0" y="-13" text-anchor="middle">{{ frictionMass }} kg</text>
        </g>
        <path class="angle-arc" d="M135 280 A35 35 0 0 0 132 267" />
        <text x="140" y="270">θ = {{ inclineAngle }}°</text>
      </svg>

      <svg v-else viewBox="0 0 400 330" role="img" aria-label="三角桁架载荷动画">
        <defs><marker id="arrow-load" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" /></marker></defs>
        <line class="truss-member" x1="55" y1="270" x2="345" y2="270" />
        <line class="truss-member truss-member--compression" x1="55" y1="270" x2="200" :y2="trussApexY" />
        <line class="truss-member truss-member--compression" x1="345" y1="270" x2="200" :y2="trussApexY" />
        <circle class="truss-joint" cx="55" cy="270" r="7" /><circle class="truss-joint" cx="345" cy="270" r="7" /><circle class="truss-joint" cx="200" :cy="trussApexY" r="7" />
        <line class="force force--weight" x1="200" :y1="trussApexY - 85" x2="200" :y2="trussApexY - 12" marker-end="url(#arrow-load)" />
        <path class="support-symbol" d="M55 277 L35 310 L75 310 Z" /><path class="support-symbol" d="M345 277 L325 310 L365 310 Z" />
        <text x="212" :y="trussApexY - 55">{{ trussLoad }} kN</text><text x="84" y="320">RA = {{ trussReaction }} kN</text><text x="254" y="320">RB = {{ trussReaction }} kN</text>
      </svg>

      <div class="statics-lab__status">
        <template v-if="experiment.kind === 'force-table'"><span>合力</span><strong>{{ resultant.toFixed(1) }} N · {{ resultantAngle.toFixed(1) }}°</strong></template>
        <template v-else-if="experiment.kind === 'free-body'"><span>单根绳张力</span><strong>{{ ropeTension.toFixed(1) }} N</strong></template>
        <template v-else-if="experiment.kind === 'lever'"><span>平衡状态</span><strong>{{ leverBalanced ? '力矩平衡' : momentDifference > 0 ? '左侧下沉' : '右侧下沉' }}</strong></template>
        <template v-else-if="experiment.kind === 'stability'"><span>稳定状态</span><strong>{{ isStable ? '重力线在支撑面内' : '超过边界，即将倾覆' }}</strong></template>
        <template v-else-if="experiment.kind === 'friction'"><span>运动趋势</span><strong>{{ isSlipping ? '静摩擦不足，开始滑动' : '保持静止' }}</strong></template>
        <template v-else><span>斜杆轴力</span><strong>{{ diagonalForce.toFixed(1) }} kN</strong></template>
      </div>
    </div>

    <div class="statics-lab__controls">
      <template v-if="experiment.kind === 'force-table'">
        <label><span>力 F₁ <output>{{ forceA }} N</output></span><input v-model.number="forceA" type="range" min="10" max="60" /></label>
        <label><span>力 F₂ <output>{{ forceB }} N</output></span><input v-model.number="forceB" type="range" min="10" max="60" /></label>
        <label><span>夹角 θ <output>{{ vectorAngle }}°</output></span><input v-model.number="vectorAngle" type="range" min="10" max="180" /></label>
      </template>
      <template v-else-if="experiment.kind === 'free-body'">
        <label><span>悬挂质量 <output>{{ mass }} kg</output></span><input v-model.number="mass" type="range" min="1" max="30" /></label>
        <label><span>绳与水平夹角 <output>{{ ropeAngle }}°</output></span><input v-model.number="ropeAngle" type="range" min="10" max="80" /></label>
      </template>
      <template v-else-if="experiment.kind === 'lever'">
        <label><span>左侧力 <output>{{ leftForce }} N</output></span><input v-model.number="leftForce" type="range" min="10" max="70" /></label>
        <label><span>左力臂 <output>{{ leftArm }} m</output></span><input v-model.number="leftArm" type="range" min="1" max="4" /></label>
        <label><span>右侧力 <output>{{ rightForce }} N</output></span><input v-model.number="rightForce" type="range" min="10" max="70" /></label>
        <label><span>右力臂 <output>{{ rightArm }} m</output></span><input v-model.number="rightArm" type="range" min="1" max="4" /></label>
      </template>
      <template v-else-if="experiment.kind === 'stability'">
        <label><span>底座宽度 <output>{{ baseWidth }} cm</output></span><input v-model.number="baseWidth" type="range" min="50" max="130" /></label>
        <label><span>重心水平偏移 <output>{{ cgOffset }} cm</output></span><input v-model.number="cgOffset" type="range" min="-70" max="70" /></label>
        <label><span>重心高度 <output>{{ cgHeight }} cm</output></span><input v-model.number="cgHeight" type="range" min="35" max="110" /></label>
      </template>
      <template v-else-if="experiment.kind === 'friction'">
        <label><span>斜面角度 <output>{{ inclineAngle }}°</output></span><input v-model.number="inclineAngle" type="range" min="0" max="45" /></label>
        <label><span>静摩擦系数 <output>{{ frictionCoefficient.toFixed(2) }}</output></span><input v-model.number="frictionCoefficient" type="range" min="0.1" max="0.8" step="0.05" /></label>
        <label><span>物块质量 <output>{{ frictionMass }} kg</output></span><input v-model.number="frictionMass" type="range" min="1" max="15" /></label>
      </template>
      <template v-else>
        <label><span>跨中载荷 <output>{{ trussLoad }} kN</output></span><input v-model.number="trussLoad" type="range" min="20" max="120" step="5" /></label>
        <label><span>桁架跨度 <output>{{ trussSpan }} m</output></span><input v-model.number="trussSpan" type="range" min="4" max="12" /></label>
        <label><span>桁架高度 <output>{{ trussHeight }} m</output></span><input v-model.number="trussHeight" type="range" min="1" max="5" step="0.5" /></label>
      </template>

      <aside>
        <small>观察任务 / OBSERVE</small>
        <p>{{ experiment.observation }}</p>
      </aside>
    </div>
  </div>
</template>

<style scoped>
.statics-lab { display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(290px, 0.55fr); border: 1px solid rgba(255, 255, 255, 0.17); background: #192923; }
.statics-lab__stage { position: relative; min-height: 470px; display: grid; place-items: center; overflow: hidden; background-image: radial-gradient(circle at 50% 48%, rgba(255, 107, 53, 0.08), transparent 54%), linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px); background-size: auto, 24px 24px, 24px 24px; }
svg { width: min(92%, 590px); overflow: visible; }
svg text { fill: #aeb9b3; font-size: 11px; font-family: inherit; }
.axis, .guide, .construction, .gravity-line, .angle-arc { fill: none; stroke: rgba(238, 244, 240, 0.2); stroke-width: 1; stroke-dasharray: 4 5; }
.force { stroke: #ff6b35; stroke-width: 3; transition: all 260ms ease; }
.force--result { stroke: #39d0b4; }
.force--weight { stroke: #ff7c4c; }
marker path { fill: #39d0b4; }
#arrow-orange path, #arrow-load path { fill: #ff6b35; }
.result-text { fill: #39d0b4; }
.ceiling, .ground, .incline { stroke: rgba(238, 244, 240, 0.55); stroke-width: 3; }
.rope { stroke: #8d9b94; stroke-width: 2; }
.hanging-mass, .lever-beam, .body-block, .friction-block rect { fill: #263c34; stroke: #ff6b35; stroke-width: 2; }
.lever-group { transition: transform 360ms ease; }
.weight { fill: #ff6b35; opacity: 0.85; transition: all 220ms ease; }
.fulcrum, .support-symbol { fill: #2c443b; stroke: #84928b; stroke-width: 1.5; }
.support { fill: #64736c; transition: all 240ms ease; }
.center-of-gravity { fill: #ff6b35; filter: drop-shadow(0 0 7px rgba(255, 107, 53, 0.8)); }
.body-block, .gravity-line { transition: all 260ms ease; }
.tipping { transform-origin: center bottom; animation: warning-wobble 700ms ease-in-out infinite alternate; }
.incline-fill { fill: rgba(255, 255, 255, 0.035); stroke: none; }
.friction-block { transition: transform 320ms ease; }
.friction-block--slipping { animation: slip-pulse 650ms ease-in-out infinite alternate; }
.truss-member { stroke: #39d0b4; stroke-width: 5; }
.truss-member--compression { stroke: #ff6b35; transition: all 260ms ease; }
.truss-joint { fill: #edf1e8; }
@keyframes warning-wobble { to { transform: rotate(2deg); } }
@keyframes slip-pulse { to { opacity: 0.55; transform: translate(6px, 5px); } }
.statics-lab__status { position: absolute; top: 22px; left: 24px; display: grid; gap: 4px; }
.statics-lab__status span { color: #819088; font-size: 9px; letter-spacing: 0.12em; }
.statics-lab__status strong { color: #edf1e8; font-size: 18px; font-weight: 500; }
.statics-lab__controls { padding: 28px; border-left: 1px solid rgba(255, 255, 255, 0.14); }
.statics-lab__controls label { display: block; padding: 16px 0 21px; border-bottom: 1px solid rgba(255, 255, 255, 0.09); }
.statics-lab__controls label > span { display: flex; justify-content: space-between; gap: 16px; margin-bottom: 16px; font-size: 12px; }
output { color: #ff916c; }
input { width: 100%; accent-color: #ff6b35; }
aside { margin-top: 28px; padding: 18px; border: 1px solid rgba(255, 107, 53, 0.28); background: rgba(255, 107, 53, 0.05); }
aside small { color: #ff8a61; font-size: 9px; letter-spacing: 0.15em; }
aside p { margin: 9px 0 0; color: #aeb9b3; font-size: 12px; line-height: 1.7; }
@media (max-width: 900px) { .statics-lab { grid-template-columns: 1fr; } .statics-lab__controls { border-top: 1px solid rgba(255, 255, 255, 0.14); border-left: 0; } }
@media (max-width: 600px) { .statics-lab__stage { min-height: 360px; } .statics-lab__controls { padding: 20px; } }
</style>
