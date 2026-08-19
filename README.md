# 物理原场 · Physical Theory

> 从物理学出发，逐步扩展到化学、生物学、地质学和天文学的交互式科学科普平台。
>
> An interactive science outreach platform that starts with physics and will expand into chemistry, biology, geology, and astronomy.

[中文](#中文介绍) · [English](#english-version)

---

## 中文介绍

### 项目愿景

本项目是一个面向公众的交互式科学科普平台，致力于用清晰的文字、直观的图示、可操作的动画和真实应用案例，让抽象的科学原理变得容易理解、值得探索。

项目将从物理学开始，逐步扩展到化学、生物学、地质学、天文学等自然科学领域，最终形成一套结构统一、内容开放、可持续扩展的科学知识图谱。

平台希望帮助不同年龄和知识背景的用户：

- 从学科地图中发现感兴趣的科学主题；
- 通过图文内容理解基本概念、核心原理和重要公式；
- 通过交互动画观察变量变化及其产生的结果；
- 通过生活、工程和自然现象了解科学知识的实际价值；
- 在跨学科知识之间建立联系，形成更完整的科学认知。

### 学科规划

| 阶段 | 学科 | 规划内容 |
| --- | --- | --- |
| 第一阶段 | 物理学 | 力学、光学、电磁学、热学，以及对应的理论、动画和应用案例 |
| 后续阶段 | 化学 | 物质结构、化学反应、元素与化合物、实验现象 |
| 后续阶段 | 生物学 | 细胞、遗传、进化、生态、人体与生命活动 |
| 后续阶段 | 地质学 | 地球结构、岩石与矿物、板块运动、地质演化 |
| 后续阶段 | 天文学 | 太阳系、恒星、星系、宇宙演化与观测方法 |

未来还可以继续扩展数学、气象学、海洋科学、环境科学等领域。

### 当前进展：物理学

当前版本已经完成可持续扩展的前后端项目框架，并建立了物理学学科地图：

- 力学：静力学、运动学、动力学、刚体力学、弹性力学、流体力学；
- 光学：几何光学、波动光学；
- 电磁学：静电学、静磁学、电动力学；
- 热学：分子动理论、热力学、统计物理。

动力学已经提供首批示例内容，包括理论介绍、核心公式、实际应用，以及可调节合外力和质量的交互式运动实验。其余学科节点已经进入内容目录，可以在后续迭代中逐个完善。

静力学已扩展为包含独立理论页面的专题模块：

- 力的合成与分解：力桌矢量合成实验；
- 受力分析与平衡：双绳悬挂张力实验；
- 力矩与力偶：可调杠杆平衡实验；
- 重心与稳定性：支撑边界与倾覆实验；
- 静摩擦与自锁：可调摩擦系数斜面实验；
- 结构与桁架平衡：三角桁架载荷实验。

每个理论页面均包含分节原理讲解、力学公式、可操作实验动画、实际应用案例、相关科学家介绍和关联理论导航。理论页面使用 `/theories/{theory-id}` 独立地址，可以直接访问和分享。

### 内容设计原则

每个知识节点原则上由以下内容组成：

1. **概念导览**：用简洁语言说明研究对象和核心问题；
2. **理论介绍**：分层讲解基本规律、关键概念与必要公式；
3. **图文说明**：通过示意图、数据图表或分步图解降低理解难度；
4. **动画实验**：允许用户调节变量并实时观察科学规律；
5. **实际应用**：连接生活现象、自然过程和工程技术；
6. **延伸探索**：引导用户前往相关知识节点，建立跨学科联系。

### 技术架构

项目采用前后端分离架构：

- **后端：** Python、FastAPI、Pydantic；
- **前端：** TypeScript、Vue 3、Vite；
- **内容组织：** 结构化学科目录、知识节点和动画配置；
- **交互呈现：** Vue 组件、SVG、CSS 动画及后续可扩展的 Canvas/WebGL；
- **质量保障：** Pytest、Ruff、TypeScript 类型检查和生产构建验证。

```text
physicaltheory/
├── backend/                 # Python / FastAPI 内容 API
│   ├── app/
│   │   ├── data/catalog.py  # 学科目录和首批物理内容
│   │   ├── models.py        # 结构化内容模型
│   │   ├── repository.py    # 内容访问层
│   │   └── main.py          # HTTP API
│   └── tests/               # API 自动化测试
└── frontend/                # TypeScript / Vue 3 / Vite
    └── src/
        ├── components/      # 学科地图、内容页面和动画实验
        ├── api.ts           # API 客户端
        └── types.ts         # 前端内容类型
```

后端内容模型与前端呈现相互分离。新增知识节点时可以优先补充结构化内容；需要独有交互效果时，再增加对应的可视化组件。未来扩展新学科时，可以继续复用目录、内容和动画协议。

### 本地启动

开发环境需要 Python 3.11+ 和 Node.js 20+。

#### 1. 启动后端

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
uvicorn app.main:app --reload
```

API 默认地址为 <http://127.0.0.1:8000>，交互式接口文档位于 <http://127.0.0.1:8000/docs>。

#### 2. 启动前端

打开另一个终端：

```bash
cd frontend
npm install
npm run dev
```

页面默认地址为 <http://127.0.0.1:5173>。开发服务器会把 `/api` 请求代理到本地后端。

### 项目验证

```bash
cd backend
.venv/bin/ruff check app tests
.venv/bin/pytest

cd ../frontend
npm run typecheck
npm run build
```

### 如何扩展内容

#### 新增物理学知识节点

1. 在 `backend/app/data/catalog.py` 中添加节点，或把已有节点状态从 `planned` 改为 `ready`；
2. 在 `DETAILS` 中添加对应的结构化内容，包括理论章节、公式、应用和动画配置；
3. 如果复用现有动画，使用已有的 `animation.kind`；如需新动画，在 `frontend/src/components/` 中添加组件并在内容页面注册；
4. 为新增内容补充 API 测试，并执行完整验证命令。

#### 新增一门科学学科

1. 为新学科建立一级目录、分支主题和知识节点；
2. 复用通用的介绍、图文、动画和应用内容模型；
3. 根据学科特点增加专用可视化，例如分子反应、细胞过程、板块运动或天体轨道；
4. 建立学科内及跨学科的关联关系；
5. 增加内容审核、资料来源和版本记录。

### 近期路线图

- 完善运动学内容，与现有动力学动画形成连续学习路径；
- 接入 KaTeX，提升复杂公式的排版和可读性；
- 为光学增加光线追迹，为电磁学增加场线和带电粒子实验，为热学增加微粒模拟；
- 将内容逐步拆分为按学科组织的 Markdown 或 JSON 文件；
- 增加内容来源、参考资料、难度等级、搜索和知识节点关联；
- 抽象通用科学内容协议，为化学、生物学、地质学和天文学模块做好准备。

---

## English Version

### Vision

This project is an interactive science outreach platform for the general public. It aims to make abstract scientific principles approachable and engaging through clear explanations, visual diagrams, interactive animations, and real-world applications.

The project starts with physics and will gradually expand into chemistry, biology, geology, astronomy, and other natural sciences. Its long-term goal is to build a consistent, open, and extensible knowledge map for exploring science.

The platform is designed to help people of different ages and educational backgrounds:

- discover interesting topics through a visual map of scientific disciplines;
- understand fundamental concepts, core principles, and important equations;
- manipulate variables and observe scientific laws through interactive simulations;
- connect scientific knowledge with everyday life, engineering, and natural phenomena;
- discover relationships across disciplines and develop a broader scientific perspective.

### Discipline Roadmap

| Phase | Discipline | Planned Coverage |
| --- | --- | --- |
| Phase 1 | Physics | Mechanics, optics, electromagnetism, thermal physics, simulations, and applications |
| Future | Chemistry | Structure of matter, chemical reactions, elements, compounds, and experiments |
| Future | Biology | Cells, genetics, evolution, ecology, the human body, and life processes |
| Future | Geology | Earth's structure, rocks and minerals, plate tectonics, and geological history |
| Future | Astronomy | The Solar System, stars, galaxies, cosmic evolution, and observation methods |

The platform may later include mathematics, meteorology, ocean science, environmental science, and other related fields.

### Current Progress: Physics

The current version provides an extensible full-stack foundation and a structured physics map covering:

- **Mechanics:** statics, kinematics, dynamics, rigid body mechanics, elasticity, and fluid mechanics;
- **Optics:** geometrical optics and wave optics;
- **Electromagnetism:** electrostatics, magnetostatics, and electrodynamics;
- **Thermal physics:** kinetic theory, thermodynamics, and statistical physics.

Dynamics includes the first sample lesson, with theory sections, core equations, real-world applications, and an interactive motion experiment where users can adjust net force and mass. The remaining discipline nodes are represented in the catalog and can be developed incrementally.

Statics has been expanded into a complete topic module with six standalone theory pages:

- force composition and decomposition, with an interactive force-table experiment;
- free-body analysis and equilibrium, with a two-cable tension experiment;
- moments and couples, with an adjustable lever experiment;
- center of gravity and stability, with a tipping-boundary experiment;
- static friction and self-locking, with an adjustable inclined-plane experiment;
- structural and truss equilibrium, with a triangular-truss load experiment.

Every theory page includes layered explanations, mechanics formulas, an interactive experiment, real-world applications, scientist profiles, and navigation to related theories. Pages use standalone `/theories/{theory-id}` URLs so they can be opened and shared directly.

### Content Design Principles

Each knowledge node is expected to include:

1. **Concept overview:** a concise introduction to the subject and its central questions;
2. **Theory:** layered explanations of principles, concepts, and essential equations;
3. **Visual explanation:** diagrams, charts, and step-by-step illustrations;
4. **Interactive simulation:** controls that let users change variables and observe outcomes;
5. **Real-world applications:** connections to daily life, nature, and engineering;
6. **Further exploration:** links to related topics within and across disciplines.

### Technology Stack

The project uses a decoupled frontend and backend architecture:

- **Backend:** Python, FastAPI, and Pydantic;
- **Frontend:** TypeScript, Vue 3, and Vite;
- **Content structure:** discipline catalogs, knowledge nodes, and animation specifications;
- **Interactive media:** Vue components, SVG, CSS animation, with room for Canvas and WebGL;
- **Quality assurance:** Pytest, Ruff, TypeScript type checking, and production build validation.

```text
physicaltheory/
├── backend/                 # Python / FastAPI content API
│   ├── app/
│   │   ├── data/catalog.py  # Discipline catalog and initial physics content
│   │   ├── models.py        # Structured content models
│   │   ├── repository.py    # Content access layer
│   │   └── main.py          # HTTP API
│   └── tests/               # Automated API tests
└── frontend/                # TypeScript / Vue 3 / Vite
    └── src/
        ├── components/      # Discipline map, content pages, and simulations
        ├── api.ts           # API client
        └── types.ts         # Frontend content types
```

Content is separated from presentation. A new topic can begin as structured content and receive a dedicated visualization component only when needed. The same catalog, content, and animation contracts can be reused as new scientific disciplines are introduced.

### Local Development

Python 3.11+ and Node.js 20+ are required.

#### 1. Start the backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
uvicorn app.main:app --reload
```

The API runs at <http://127.0.0.1:8000>, with interactive documentation at <http://127.0.0.1:8000/docs>.

#### 2. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The web application runs at <http://127.0.0.1:5173>. During development, Vite proxies `/api` requests to the local backend.

### Verification

```bash
cd backend
.venv/bin/ruff check app tests
.venv/bin/pytest

cd ../frontend
npm run typecheck
npm run build
```

### Extending the Platform

#### Add a physics topic

1. Add a node in `backend/app/data/catalog.py`, or change an existing node from `planned` to `ready`;
2. Add its structured `DETAILS`, including theory sections, equations, applications, and an animation specification;
3. Reuse an existing `animation.kind`, or create and register a new component in `frontend/src/components/`;
4. Add API tests and run the complete verification suite.

#### Add a new scientific discipline

1. Define its top-level catalog, branches, and knowledge nodes;
2. Reuse the common models for introductions, visual explanations, simulations, and applications;
3. Add discipline-specific visualizations such as molecular reactions, cellular processes, plate movement, or orbital motion;
4. Create relationships within the discipline and across other scientific fields;
5. Add editorial review, references, and content versioning.

### Near-Term Roadmap

- Complete kinematics and connect it with the existing dynamics simulation;
- Integrate KaTeX for clearer and more advanced mathematical notation;
- Add ray tracing for optics, field lines and charged particles for electromagnetism, and particle simulations for thermal physics;
- Move growing content into discipline-based Markdown or JSON files;
- Add references, difficulty levels, search, and relationships between knowledge nodes;
- Generalize the science content contract in preparation for chemistry, biology, geology, and astronomy.
