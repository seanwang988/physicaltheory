<script setup lang="ts">
import { computed, onBeforeUnmount, ref } from 'vue'

const force = ref(6)
const mass = ref(3)
const position = ref(8)
const velocity = ref(0)
const isRunning = ref(false)
let frameId: number | null = null
let previousTime = 0

const acceleration = computed(() => force.value / mass.value)
const direction = computed(() => (force.value >= 0 ? '向右' : '向左'))

function tick(time: number) {
  if (!isRunning.value) return
  const delta = Math.min((time - previousTime) / 1000, 0.034)
  previousTime = time
  velocity.value += acceleration.value * delta * 4
  position.value += velocity.value * delta * 3

  if (position.value >= 92 || position.value <= 0) {
    position.value = Math.min(92, Math.max(0, position.value))
    velocity.value *= -0.65
  }
  frameId = requestAnimationFrame(tick)
}

function toggle() {
  isRunning.value = !isRunning.value
  if (isRunning.value) {
    previousTime = performance.now()
    frameId = requestAnimationFrame(tick)
  } else if (frameId !== null) {
    cancelAnimationFrame(frameId)
  }
}

function reset() {
  isRunning.value = false
  if (frameId !== null) cancelAnimationFrame(frameId)
  position.value = 8
  velocity.value = 0
}

onBeforeUnmount(() => {
  if (frameId !== null) cancelAnimationFrame(frameId)
})
</script>

<template>
  <section class="lab" aria-label="力与运动交互动画">
    <div class="lab__visual">
      <div class="lab__readout">
        <span>实时加速度</span>
        <strong>{{ acceleration.toFixed(2) }} m/s²</strong>
      </div>
      <div class="vector" :class="{ 'vector--left': force < 0 }" :style="{ width: `${Math.abs(force) * 7 + 14}px` }">
        <span>F = {{ force }} N</span>
      </div>
      <div class="track">
        <div class="track__ticks" />
        <div class="cart" :style="{ left: `${position}%` }">
          <div class="cart__mass">{{ mass }} kg</div>
          <span /><span />
        </div>
      </div>
    </div>

    <div class="lab__controls">
      <label>
        <span><b>合外力</b><output>{{ force }} N · {{ direction }}</output></span>
        <input v-model.number="force" type="range" min="-10" max="10" step="1" />
      </label>
      <label>
        <span><b>物体质量</b><output>{{ mass }} kg</output></span>
        <input v-model.number="mass" type="range" min="1" max="10" step="1" />
      </label>
      <div class="lab__actions">
        <button class="button button--primary" type="button" @click="toggle">
          {{ isRunning ? '暂停实验' : '开始实验' }}
        </button>
        <button class="button button--ghost" type="button" @click="reset">重置</button>
      </div>
    </div>
  </section>
</template>
