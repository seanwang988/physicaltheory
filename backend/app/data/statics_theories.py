from app.models import (
    ApplicationCase,
    ExperimentSpec,
    Formula,
    ScientistProfile,
    TheoryDetail,
    TheoryNode,
    TheorySection,
)


def theory_node(
    theory_id: str,
    name: str,
    english_name: str,
    summary: str,
    order: int,
    experiment_kind: str,
) -> TheoryNode:
    return TheoryNode(
        id=theory_id,
        subject_id="statics",
        name=name,
        english_name=english_name,
        summary=summary,
        order=order,
        experiment_kind=experiment_kind,
    )


STATICS_THEORY_NODES = [
    theory_node(
        "force-composition",
        "力的合成与分解",
        "Force Composition",
        "用矢量描述多个力的共同作用，并把一个力分解到选定方向。",
        1,
        "force-table",
    ),
    theory_node(
        "free-body-equilibrium",
        "受力分析与平衡",
        "Free-Body Equilibrium",
        "通过受力图隔离研究对象，建立质点平衡方程。",
        2,
        "free-body",
    ),
    theory_node(
        "moment-and-couple",
        "力矩与力偶",
        "Moment and Couple",
        "理解力对刚体转动趋势的度量，以及力偶产生的纯转动效应。",
        3,
        "lever",
    ),
    theory_node(
        "center-of-gravity",
        "重心与稳定性",
        "Center of Gravity",
        "用重心投影与支撑区域判断物体是否会倾覆。",
        4,
        "stability",
    ),
    theory_node(
        "static-friction",
        "静摩擦与自锁",
        "Static Friction",
        "研究接触面如何阻止相对滑动，以及临界平衡和自锁条件。",
        5,
        "friction",
    ),
    theory_node(
        "structural-equilibrium",
        "结构与桁架平衡",
        "Structural Equilibrium",
        "把整体平衡与杆件受力结合起来，理解稳定结构如何传递载荷。",
        6,
        "truss",
    ),
]


NEWTON = ScientistProfile(
    name="艾萨克·牛顿",
    original_name="Isaac Newton",
    period="17—18 世纪",
    field="经典力学、数学与光学",
    contribution="建立运动定律与力的定量框架，使平衡成为合外力为零的特殊情形。",
    introduction="牛顿把力、质量和运动联系在统一体系中。静力学虽然研究不加速的物体，但它的平衡方程正是牛顿第二定律在加速度为零时的结果。",
)

STEVIN = ScientistProfile(
    name="西蒙·斯蒂文",
    original_name="Simon Stevin",
    period="16—17 世纪",
    field="静力学、流体静力学与工程",
    contribution="系统研究斜面平衡和力的分解，并用思想实验说明平衡关系。",
    introduction="斯蒂文善于用简单装置揭示一般规律。他对斜面、滑轮和流体压力的研究，让静力学从经验技巧逐步走向可计算的科学。",
)

ARCHIMEDES = ScientistProfile(
    name="阿基米德",
    original_name="Archimedes",
    period="古希腊时期",
    field="静力学、几何学与流体静力学",
    contribution="建立杠杆平衡的定量规律，并研究平面图形的重心。",
    introduction="阿基米德以几何方法研究杠杆和重心。他证明平衡不只取决于力的大小，还取决于力到支点的距离，这成为力矩理论的核心思想。",
)

VARIGNON = ScientistProfile(
    name="皮埃尔·瓦里尼翁",
    original_name="Pierre Varignon",
    period="17—18 世纪",
    field="力学与数学",
    contribution="提出并推广力矩定理：合力对一点的力矩等于各分力力矩之和。",
    introduction="瓦里尼翁把几何矢量方法引入力学分析。以他命名的力矩定理可以减少复杂受力系统的计算，也是工程静力学最常用的工具之一。",
)

GALILEO = ScientistProfile(
    name="伽利略·伽利莱",
    original_name="Galileo Galilei",
    period="16—17 世纪",
    field="力学、天文学与实验科学",
    contribution="研究物体平衡、尺度与结构强度，推动以实验和数学分析自然现象。",
    introduction="伽利略关注为什么大型结构不能只是小型结构的等比例放大。他对尺度、重力和材料承载能力的讨论，为结构稳定与工程力学开辟了新方向。",
)

COULOMB = ScientistProfile(
    name="夏尔·奥古斯丁·库仑",
    original_name="Charles-Augustin de Coulomb",
    period="18—19 世纪",
    field="力学、电学与工程",
    contribution="通过实验总结干摩擦规律，使摩擦力能够进入工程平衡计算。",
    introduction="库仑不仅研究电荷之间的作用，也长期从事工程问题。他对滑动与静摩擦的实验研究形成了经典摩擦模型，至今仍用于机械设计的初步分析。",
)


STATICS_THEORIES = {
    "force-composition": TheoryDetail(
        **STATICS_THEORY_NODES[0].model_dump(),
        tagline="多个方向，一种合力",
        introduction="力是有大小和方向的矢量。当多个力同时作用于一点时，可以用一个等效合力代替它们；反过来，也可以沿方便分析的方向把一个力分解成若干分力。",
        sections=[
            TheorySection(
                title="平行四边形法则",
                paragraphs=[
                    "把两个力矢量的起点放在同一点，以它们为邻边作平行四边形，对角线就是合力。这个几何构造同时包含合力的大小和方向。",
                    "多于两个力时，可以依次相加，也可以先把每个力投影到坐标轴，再分别求各方向分量之和。",
                ],
            ),
            TheorySection(
                title="正交分解",
                paragraphs=[
                    "选择相互垂直的 x、y 轴后，斜向力可以写成水平与竖直分量。"
                    "坐标轴可以自由选择，通常让尽可能多的力落在轴上以简化计算。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="F⃗R = ΣF⃗i", description="合力等于所有力的矢量和"),
            Formula(expression="Fx = F cos θ", description="力在 x 方向的投影"),
            Formula(expression="Fy = F sin θ", description="力在 y 方向的投影"),
        ],
        experiment=ExperimentSpec(
            kind="force-table",
            title="力桌合成实验",
            description="改变两根拉绳的拉力与夹角，观察合力的大小和方向。",
            principle="两个力的合力遵循平行四边形法则；夹角越小，合力通常越大。",
            observation="尝试让两个力大小相同并把夹角调到 180°，合力将趋近于零。",
            controls=["force_a", "force_b", "angle"],
        ),
        applications=[
            ApplicationCase(
                title="缆索吊装", description="把多根缆索的拉力合成为设备受到的总提升力。"
            ),
            ApplicationCase(
                title="风荷载分析", description="将斜向风力分解为建筑物的水平和竖直作用。"
            ),
            ApplicationCase(
                title="机器人末端控制", description="计算多关节驱动力在工具端形成的等效力。"
            ),
        ],
        scientists=[NEWTON, STEVIN],
        related_theory_ids=["free-body-equilibrium", "structural-equilibrium"],
    ),
    "free-body-equilibrium": TheoryDetail(
        **STATICS_THEORY_NODES[1].model_dump(),
        tagline="先隔离，再平衡",
        introduction="受力图把研究对象从环境中单独取出，只保留外界对它施加的力。对静止质点，所有方向上的合力都必须为零。",
        sections=[
            TheorySection(
                title="绘制受力图",
                paragraphs=[
                    "先确定研究对象的边界，再把接触、绳索和支座替换成相应的力。不要把研究对象对外界的反作用力画在同一张图中。",
                    "重力通常作用于重心，光滑接触面只提供法向力，绳索只能沿绳方向提供拉力。",
                ],
            ),
            TheorySection(
                title="建立平衡方程",
                paragraphs=[
                    "把所有外力投影到相互独立的坐标方向。二维质点有两个独立平衡方程，未知量数量不超过方程数量时通常可以直接求解。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="ΣFx = 0", description="水平方向合力为零"),
            Formula(expression="ΣFy = 0", description="竖直方向合力为零"),
            Formula(expression="T = W / (2 sin θ)", description="对称双绳悬挂时每根绳的张力"),
        ],
        experiment=ExperimentSpec(
            kind="free-body",
            title="双绳悬挂实验",
            description="改变悬挂质量与绳索角度，观察两根绳中的张力。",
            principle="竖直方向的两个张力分量共同平衡重力，水平方向分量互相抵消。",
            observation="绳索越接近水平，为提供相同竖直分量所需的张力越大。",
            controls=["mass", "rope_angle"],
        ),
        applications=[
            ApplicationCase(title="吊灯安装", description="估算两侧吊索与固定点需要承受的拉力。"),
            ApplicationCase(
                title="登山保护站", description="避免保护点夹角过大导致锚点载荷急剧增加。"
            ),
            ApplicationCase(
                title="交通标志悬挂", description="根据重量和拉索方向选择合适的线缆与连接件。"
            ),
        ],
        scientists=[STEVIN, NEWTON],
        related_theory_ids=["force-composition", "static-friction"],
    ),
    "moment-and-couple": TheoryDetail(
        **STATICS_THEORY_NODES[2].model_dump(),
        tagline="力 × 力臂 = 转动趋势",
        introduction="同样大小的力，作用位置不同，对物体产生的转动效果也不同。力矩用力与垂直力臂的乘积来衡量这种转动趋势。",
        sections=[
            TheorySection(
                title="力矩与转向",
                paragraphs=[
                    "力矩的参考点必须明确。二维问题通常约定逆时针为正、顺时针为负；只要全程保持一致，符号约定也可以反过来。",
                    "如果力的作用线通过参考点，垂直力臂为零，因此这个力对该点不产生力矩。",
                ],
            ),
            TheorySection(
                title="力偶与刚体平衡",
                paragraphs=[
                    "两个大小相等、方向相反但不共线的平行力构成力偶。力偶的合力为零，却保留与参考点无关的纯转动力矩。刚体平衡必须同时满足合力和合力矩为零。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="M = Fd⊥", description="力矩等于力与垂直力臂的乘积"),
            Formula(expression="ΣMO = 0", description="刚体对任意参考点的合力矩为零"),
            Formula(expression="MO(FR) = ΣMO(Fi)", description="瓦里尼翁力矩定理"),
        ],
        experiment=ExperimentSpec(
            kind="lever",
            title="杠杆平衡实验",
            description="调节支点两侧的砝码和力臂，让杠杆恢复水平。",
            principle="杠杆平衡时，顺时针力矩之和等于逆时针力矩之和。",
            observation="较小的力可以通过更长的力臂平衡较大的力。",
            controls=["left_force", "left_arm", "right_force", "right_arm"],
        ),
        applications=[
            ApplicationCase(
                title="扳手与门把手", description="增加力臂可以用更小的力获得相同转动效果。"
            ),
            ApplicationCase(
                title="塔式起重机", description="用平衡臂和配重抵消吊重产生的倾覆力矩。"
            ),
            ApplicationCase(title="车辆制动", description="制动器通过摩擦力矩降低车轮的转动速度。"),
        ],
        scientists=[ARCHIMEDES, VARIGNON],
        related_theory_ids=["center-of-gravity", "structural-equilibrium"],
    ),
    "center-of-gravity": TheoryDetail(
        **STATICS_THEORY_NODES[3].model_dump(),
        tagline="重力作用的等效位置",
        introduction="复杂物体各部分都受到重力，但在均匀重力场中，可以把总重力等效为作用在重心的一股力。重心越低、支撑区域越宽，物体通常越稳定。",
        sections=[
            TheorySection(
                title="重心与质心",
                paragraphs=[
                    "质心由物体的质量分布决定；重心是合重力的作用点。在地面附近近似均匀的重力场中，两者位置通常重合。",
                    "组合物体的质心坐标可以用各部分质量对坐标的加权平均求得。对称且密度均匀的物体，其质心位于几何对称中心。",
                ],
            ),
            TheorySection(
                title="稳定与倾覆",
                paragraphs=[
                    "当重力作用线落在支撑区域内，支撑力可以调整位置来平衡重力矩；一旦重力作用线越过支撑边缘，物体就会绕边缘倾覆。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="x̄ = Σmixi / Σmi", description="离散质量系统的质心横坐标"),
            Formula(expression="ȳ = Σmiyi / Σmi", description="离散质量系统的质心纵坐标"),
            Formula(expression="|xCG| ≤ b / 2", description="重心投影位于宽度 b 的支撑面内"),
        ],
        experiment=ExperimentSpec(
            kind="stability",
            title="倾覆边界实验",
            description="改变支撑面宽度和重心的水平偏移，观察物体是否稳定。",
            principle="只有当重力作用线穿过支撑区域时，物体才能保持静态稳定。",
            observation="增大底座或让重心靠近中心，可以显著提高抗倾覆能力。",
            controls=["base_width", "cg_offset", "cg_height"],
        ),
        applications=[
            ApplicationCase(title="车辆防侧翻", description="降低电池与底盘位置，使整车重心更低。"),
            ApplicationCase(title="不倒翁", description="利用低重心和曲面底座产生自动恢复的力矩。"),
            ApplicationCase(
                title="高层建筑", description="通过基础、核心筒和配重系统抵抗风致倾覆。"
            ),
        ],
        scientists=[ARCHIMEDES, GALILEO],
        related_theory_ids=["moment-and-couple", "static-friction"],
    ),
    "static-friction": TheoryDetail(
        **STATICS_THEORY_NODES[4].model_dump(),
        tagline="阻止滑动的自适应力",
        introduction="静摩擦力并不总等于最大值，而是在零到极限值之间自动调整，以阻止接触面发生相对滑动。达到极限后再增加切向外力，物体就会开始滑动。",
        sections=[
            TheorySection(
                title="静摩擦的范围",
                paragraphs=[
                    "静摩擦力方向与物体相对滑动趋势相反。计算时应先根据平衡求出所需摩擦力，再检查它是否超过极限值。",
                    "经典库仑模型把最大静摩擦力近似写成正压力与静摩擦系数的乘积。摩擦系数由接触材料和表面状态决定。",
                ],
            ),
            TheorySection(
                title="摩擦角与自锁",
                paragraphs=[
                    "斜面角小于摩擦角时，即使没有其他阻挡，物体也可能保持静止。螺纹、楔块和夹具常利用类似条件实现自锁。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="0 ≤ fs ≤ μsN", description="静摩擦力在极限范围内自适应变化"),
            Formula(expression="fs,max = μsN", description="最大静摩擦力"),
            Formula(expression="tan φ = μs", description="摩擦角与静摩擦系数的关系"),
        ],
        experiment=ExperimentSpec(
            kind="friction",
            title="可调斜面实验",
            description="改变斜面角度和摩擦系数，寻找物块开始滑动的临界角。",
            principle="物块开始下滑的临界状态满足重力沿斜面分量等于最大静摩擦力。",
            observation="当 tan θ 超过 μs 时，静摩擦不足以维持平衡，物块开始滑动。",
            controls=["incline_angle", "friction_coefficient", "mass"],
        ),
        applications=[
            ApplicationCase(title="轮胎抓地", description="利用足够的静摩擦完成加速、转向和制动。"),
            ApplicationCase(
                title="螺纹自锁", description="合理选择螺旋升角，使紧固件在载荷下不自行回转。"
            ),
            ApplicationCase(
                title="攀岩与防滑", description="通过增大正压力、摩擦系数和接触稳定性避免滑落。"
            ),
        ],
        scientists=[COULOMB, STEVIN],
        related_theory_ids=["free-body-equilibrium", "center-of-gravity"],
    ),
    "structural-equilibrium": TheoryDetail(
        **STATICS_THEORY_NODES[5].model_dump(),
        tagline="让载荷找到通往地面的路径",
        introduction="结构静力学研究梁、桁架和框架如何把外部载荷传递到支座。稳定结构既要满足整体平衡，也要保证每个连接点和构件满足局部平衡。",
        sections=[
            TheorySection(
                title="支座与反力",
                paragraphs=[
                    "二维结构中，滚动支座通常提供一个法向反力，铰支座可以提供两个方向的反力，固定端还可以提供约束力矩。",
                    "求解构件内力前，通常先把整个结构作为研究对象，利用整体平衡求出支座反力。",
                ],
            ),
            TheorySection(
                title="桁架与二力杆",
                paragraphs=[
                    "理想桁架由直杆在端点铰接而成，载荷作用在节点上。每根杆只承受沿轴线的拉力或压力，因此可以用节点法或截面法求解杆件内力。"
                ],
            ),
        ],
        formulas=[
            Formula(expression="ΣFx = 0, ΣFy = 0", description="结构整体或节点的平动平衡"),
            Formula(expression="ΣM = 0", description="结构整体的转动平衡"),
            Formula(expression="m + r = 2j", description="简单平面桁架的静定判别关系"),
        ],
        experiment=ExperimentSpec(
            kind="truss",
            title="三角桁架载荷实验",
            description="改变跨中载荷、跨度和高度，观察支座反力与斜杆内力。",
            principle="对称载荷由两侧支座平均承担；桁架越扁，斜杆为提供竖直分量所需的轴力越大。",
            observation="保持载荷和跨度不变，增大桁架高度通常可以减小斜杆轴力。",
            controls=["load", "span", "height"],
        ),
        applications=[
            ApplicationCase(
                title="桥梁桁架", description="用三角形杆系高效地把车辆载荷传递到桥墩。"
            ),
            ApplicationCase(
                title="屋架与空间结构", description="用轻质杆件跨越较大空间并抵抗风雪载荷。"
            ),
            ApplicationCase(
                title="起重机臂架", description="通过拉压杆组合，在较低自重下承担较大吊重。"
            ),
        ],
        scientists=[GALILEO, VARIGNON],
        related_theory_ids=["moment-and-couple", "force-composition"],
    ),
}
