from app.models import AnimationSpec, Discipline, Formula, SubjectDetail, SubjectNode, TheorySection

from .statics_theories import STATICS_THEORY_NODES


def node(
    node_id: str,
    name: str,
    english_name: str,
    summary: str,
    status: str = "planned",
) -> SubjectNode:
    return SubjectNode(
        id=node_id,
        name=name,
        english_name=english_name,
        summary=summary,
        status=status,
    )


DISCIPLINES = [
    Discipline(
        id="mechanics",
        name="力学",
        english_name="Mechanics",
        color="#ff6b35",
        icon="M",
        summary="研究物体受力、运动、形变以及流体行为的规律。",
        subjects=[
            node("statics", "静力学", "Statics", "研究平衡状态下物体所受力与力矩。", "ready"),
            node("kinematics", "运动学", "Kinematics", "不考虑成因，描述位置、速度和加速度。"),
            node("dynamics", "动力学", "Dynamics", "连接物体运动与作用力的基本规律。", "ready"),
            node(
                "rigid-body", "刚体力学", "Rigid Body Mechanics", "研究刚体的平动、转动与空间姿态。"
            ),
            node("elasticity", "弹性力学", "Elasticity", "研究固体受力后的应力、应变与形变。"),
            node("fluid", "流体力学", "Fluid Mechanics", "研究液体与气体的静止和流动规律。"),
        ],
    ),
    Discipline(
        id="optics",
        name="光学",
        english_name="Optics",
        color="#ffc857",
        icon="O",
        summary="研究光的传播、成像，以及干涉和衍射等波动现象。",
        subjects=[
            node(
                "geometrical-optics",
                "几何光学",
                "Geometrical Optics",
                "用光线模型解释反射、折射和成像。",
            ),
            node("wave-optics", "波动光学", "Wave Optics", "研究干涉、衍射和偏振等波动特性。"),
        ],
    ),
    Discipline(
        id="electromagnetism",
        name="电磁学",
        english_name="Electromagnetism",
        color="#39d0b4",
        icon="E",
        summary="研究电荷、电流、电磁场及其相互作用。",
        subjects=[
            node("electrostatics", "静电学", "Electrostatics", "研究静止电荷及其产生的电场。"),
            node("magnetostatics", "静磁学", "Magnetostatics", "研究恒定电流与稳定磁场。"),
            node(
                "electrodynamics", "电动力学", "Electrodynamics", "研究时变电磁场与带电粒子的运动。"
            ),
        ],
    ),
    Discipline(
        id="thermology",
        name="热学",
        english_name="Thermal Physics",
        color="#a879ff",
        icon="T",
        summary="从宏观和微观层面研究热、能量与物质状态。",
        subjects=[
            node(
                "kinetic-theory",
                "分子动理论",
                "Kinetic Theory",
                "用微观粒子运动解释物质的宏观热性质。",
            ),
            node("thermodynamics", "热力学", "Thermodynamics", "研究热、功、能量与状态变化。"),
            node(
                "statistical-physics",
                "统计物理",
                "Statistical Physics",
                "用概率统计连接微观状态与宏观规律。",
            ),
        ],
    ),
]


DETAILS = {
    "statics": SubjectDetail(
        **next(
            subject.model_dump() for subject in DISCIPLINES[0].subjects if subject.id == "statics"
        ),
        discipline_id="mechanics",
        introduction="静力学关注物体为何能够保持静止或匀速直线运动。核心是识别所有外力，并让合力与合力矩同时为零。",
        sections=[
            TheorySection(
                title="平衡条件",
                paragraphs=[
                    "质点平衡要求各方向的合力为零；有尺寸的物体还必须满足任意参考点处的合力矩为零。",
                    "解决问题时通常先隔离研究对象，画出受力图，再选择合适的坐标轴列方程。",
                ],
            ),
            TheorySection(
                title="受力图",
                paragraphs=[
                    "受力图只保留研究对象及其受到的外力。重力、支持力、摩擦力、拉力和约束反力是常见元素。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="ΣF = 0", description="平动平衡：所有外力的矢量和为零"),
            Formula(expression="Στ = 0", description="转动平衡：所有外力矩的代数和为零"),
        ],
        applications=["桥梁与桁架结构分析", "起重机配重设计", "人体姿态与关节受力分析"],
        animation=AnimationSpec(
            kind="force-motion",
            title="力与运动实验台",
            description="调节推力和质量，观察物体加速度变化；将推力归零可模拟平衡状态。",
            controls=["force", "mass"],
        ),
        theories=STATICS_THEORY_NODES,
    ),
    "dynamics": SubjectDetail(
        **next(
            subject.model_dump() for subject in DISCIPLINES[0].subjects if subject.id == "dynamics"
        ),
        discipline_id="mechanics",
        introduction="动力学研究物体运动状态改变的原因。牛顿运动定律建立了力、质量与加速度之间的定量关系。",
        sections=[
            TheorySection(
                title="牛顿第二定律",
                paragraphs=[
                    "物体的加速度与所受合外力同方向，大小与合外力成正比、与质量成反比。",
                    "力不是维持运动的原因，而是改变运动状态的原因。若合外力为零，速度保持不变。",
                ],
            ),
            TheorySection(
                title="分析步骤",
                paragraphs=[
                    "选择研究对象并画受力图，建立坐标系，把力分解到各轴，最后结合运动学关系求解。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="ΣF = ma", description="合外力等于质量与加速度的乘积"),
            Formula(expression="p = mv", description="动量等于质量与速度的乘积"),
        ],
        applications=["汽车加速与制动", "火箭推进与轨道控制", "机器人运动控制"],
        animation=AnimationSpec(
            kind="force-motion",
            title="牛顿第二定律实验台",
            description="改变合外力和质量，实时观察加速度与位移变化。",
            controls=["force", "mass"],
        ),
    ),
}
