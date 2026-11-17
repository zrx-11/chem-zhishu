#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成《无机及分析化学题库》40 题单书。"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "04-无机及分析化学题库")
os.makedirs(os.path.join(BOOK, "chapters"), exist_ok=True)

UNITS = [
    ("ch01", "第 1 单元：基础计算与物质结构", "u01", "物质的量、浓度、pH、电子排布、VSEPR、晶体类型"),
    ("ch02", "第 2 单元：反应原理与元素化学", "u02", "速率方程、平衡常数、勒夏特列、卤素、氮硫、铁铜"),
    ("ch03", "第 3 单元：酸碱与配位滴定", "u03", "弱酸 pH、缓冲、指示剂、混合碱、EDTA、条件稳定常数"),
    ("ch04", "第 4 单元：氧化还原与沉淀重量", "u04", "电极电势、K、KMnO4、碘量法、Ksp、三种沉淀滴定、换算因数"),
    ("ch05", "第 5 单元：仪器分析与分离", "u05", "比尔定律、标准曲线、玻璃电极、萃取、色谱、电位滴定"),
]

Q = {
"ch01": [
("18 g H₂O 中含有的水分子数约为（ ）", ["6.022×10²³", "3.011×10²³", "1.204×10²⁴", "6.022×10²²"], 0,
 "n=18/18=1 mol，N=1×6.022×10²³。"),
("0.20 mol/L NaOH 溶液 500 mL 中 NaOH 的物质的量为（ ）", ["0.05 mol", "0.10 mol", "0.20 mol", "0.40 mol"], 1,
 "n=cV=0.20×0.500=0.10 mol。"),
("标准状况下 5.6 L O₂ 的物质的量为（ ）", ["0.125 mol", "0.50 mol", "0.25 mol", "2.5 mol"], 2,
 "n=5.6/22.4=0.25 mol。"),
("K₂Cr₂O₇ 中 Cr 的化合价为（ ）", ["+3", "+6", "+7", "+2"], 1,
 "2×(+1)+2x+7×(−2)=0，x=+6。"),
("Cr 原子的基态电子排布为（ ）", ["[Ar]3d⁵4s¹", "[Ar]3d⁴4s²", "[Ar]3d⁶4s⁰", "[Ar]3d³4s³"], 0,
 "Cr 为半充满稳定结构，3d⁵4s¹。"),
("NH₃ 分子的空间构型为（ ）", ["直线形", "平面三角形", "三角锥形", "四面体形"], 2,
 "N 有 3 个成键电子对和 1 对孤对电子，VSEPR 为三角锥。"),
("下列晶体中熔点最高的是（ ）", ["NaCl", "干冰", "冰", "SiO₂"], 3,
 "SiO₂ 是原子晶体，共价键网络，熔点最高。"),
("pH=2 的 HCl 溶液的物质的量浓度为（ ）", ["0.20 mol/L", "0.010 mol/L", "0.10 mol/L", "0.0010 mol/L"], 1,
 "pH=2，[H⁺]=10⁻²=0.010 mol/L，强酸完全电离。"),
],
"ch02": [
("反应 A→产物，A 的浓度加倍时反应速率加倍，该反应对 A 的级数为（ ）", ["0", "1", "2", "3"], 1,
 "v∝[A]^n，浓度加倍速率加倍，n=1。"),
("反应 N₂+3H₂⇌2NH₃ 的浓度平衡常数表达式为（ ）", ["[NH₃]²/([N₂][H₂]³)", "[NH₃]/([N₂][H₂])", "[N₂][H₂]³/[NH₃]²", "[NH₃]²/([N₂][H₂])"], 0,
 "生成物系数为指数，反应物在分母。"),
("某时刻 Q<K，反应将（ ）", ["正向进行", "逆向进行", "已达平衡", "无法判断"], 0,
 "Q<K 表示生成物不足，反应正向。"),
("合成氨 N₂+3H₂⇌2NH₃（ΔH<0），增大压强时平衡（ ）", ["正向移动", "逆向移动", "不移动", "先正后逆"], 0,
 "正向气体分子数减少，加压向正向。"),
("催化剂对化学平衡的影响是（ ）", ["提高 K", "降低 K", "降低活化能，K 不变", "改变平衡转化率"], 2,
 "催化剂同等加快正逆反应，不改变 K。"),
("卤素单质的氧化性顺序为（ ）", ["F₂>Cl₂>Br₂>I₂", "I₂>Br₂>Cl₂>F₂", "Cl₂>F₂>Br₂>I₂", "Br₂>Cl₂>I₂>F₂"], 0,
 "电负性、电极电势决定，F₂ 最强。"),
("Fe³⁺ 在水溶液中的常见颜色为（ ）", ["浅绿色", "黄色", "蓝色", "紫色"], 1,
 "Fe³⁺ 黄，Fe²⁺ 浅绿，Cu²⁺ 蓝。"),
("铜与稀硝酸反应的主要还原产物是（ ）", ["NO₂", "N₂O", "NO", "NH₃"], 2,
 "稀硝酸被还原为 NO，浓硝酸为 NO₂。"),
],
"ch03": [
("0.10 mol/L HAc（Ka=1.8×10⁻⁵）的 pH 约为（ ）", ["1.00", "2.87", "4.74", "7.00"], 1,
 "[H⁺]=√(1.8×10⁻⁶)=1.34×10⁻³，pH=2.87。"),
("0.10 mol/L HAc 与 0.10 mol/L NaAc 等体积混合，pH 约为（pKa=4.74）（ ）", ["2.87", "4.44", "4.74", "8.72"], 2,
 "等浓度比 1:1，pH=pKa=4.74。"),
("强碱滴定弱酸，计量点附近应选（ ）", ["甲基橙", "甲基红", "酚酞", "石蕊"], 2,
 "计量点显碱性，突跃在碱性区，选酚酞。"),
("双指示剂法测混合碱，V₁=V₂，组成是（ ）", ["Na₂CO₃", "NaOH", "NaHCO₃", "NaOH+NaHCO₃"], 0,
 "只有 Na₂CO₃ 时两步消耗相同。"),
("用 0.1000 mol/L NaOH 滴定 25.00 mL HCl，消耗 20.00 mL，c(HCl) 为（ ）", ["0.08000 mol/L", "0.1000 mol/L", "0.1250 mol/L", "0.2000 mol/L"], 0,
 "c=0.1000×20.00/25.00=0.08000。"),
("Na₂CO₃ 与 HCl 的计量系数比 n(Na₂CO₃):n(HCl) 为（ ）", ["1:1", "1:2", "2:1", "1:3"], 1,
 "Na₂CO₃+2HCl=2NaCl+H₂O+CO₂。"),
("EDTA 与大多数金属离子形成的配合物配位比为（ ）", ["1:1", "1:2", "2:1", "1:4"], 0,
 "EDTA 六齿配体，一个分子配一个金属离子。"),
("lgK(ZnY)=16.5，pH=5 时 lgαY(H)=6.45，lgK' 为（ ）", ["22.95", "16.5", "10.05", "8.00"], 2,
 "lgK'=16.5−6.45=10.05。"),
],
"ch04": [
("电池 (−)Zn|Zn²⁺||Cu²⁺|Cu(+) 的标准电动势为（ ）", ["0.34 V", "0.76 V", "1.10 V", "1.51 V"], 2,
 "E°=0.34−(−0.76)=1.10 V。"),
("n=2、E°=1.00 V 的电池反应，lgK 约为（ ）", ["16.9", "33.8", "59.2", "1.00"], 1,
 "lgK=nE°/0.0592=2/0.0592=33.8。"),
("用 Na₂C₂O₄ 标定 KMnO₄，n(MnO₄⁻):n(C₂O₄²⁻) 为（ ）", ["1:1", "2:5", "5:2", "1:2"], 1,
 "2MnO₄⁻+5C₂O₄²⁻+16H⁺=2Mn²⁺+10CO₂+8H₂O。"),
("间接碘量法测 Cu²⁺，n(Cu²⁺):n(S₂O₃²⁻) 为（ ）", ["1:1", "2:1", "1:2", "1:3"], 0,
 "2Cu²⁺生成 1I₂，1I₂消耗 2S₂O₃²⁻，折算 1:1。"),
("AgCl 在 0.10 mol/L NaCl 中的溶解度约为（Ksp=1.8×10⁻¹⁰）（ ）", ["1.8×10⁻⁹ mol/L", "1.3×10⁻⁵ mol/L", "1.8×10⁻¹⁰ mol/L", "1.3×10⁻⁴ mol/L"], 0,
 "同离子效应，s=Ksp/[Cl⁻]=1.8×10⁻⁹。"),
("Ag₂CrO₄ 的溶解度 s 与 Ksp 的关系为（ ）", ["s=√Ksp", "s=∛Ksp", "s=∛(Ksp/2)", "s=∛(Ksp/4)"], 3,
 "Ksp=(2s)²s=4s³，s=∛(Ksp/4)。"),
("莫尔法使用的指示剂是（ ）", ["K₂CrO₄", "铁铵矾", "荧光黄", "淀粉"], 0,
 "Ag⁺ 与 CrO₄²⁻ 生成砖红色 Ag₂CrO₄。"),
("由 Fe₂O₃ 称量形式求 Fe 的换算因数为（ ）", ["M(Fe)/M(Fe₂O₃)", "2M(Fe)/M(Fe₂O₃)", "M(Fe₂O₃)/2M(Fe)", "3M(Fe)/M(Fe₂O₃)"], 1,
 "1 mol Fe₂O₃ 含 2 mol Fe。"),
],
"ch05": [
("某溶液吸光度 A=1.0，透光率 T 为（ ）", ["10%", "20%", "50%", "90%"], 0,
 "T=10^-A=10^-1=0.10。"),
("A=0.500，b=1.0 cm，ε=1.0×10⁴ L/(mol·cm)，浓度为（ ）", ["5.0×10⁻⁴ mol/L", "2.0×10⁻⁴ mol/L", "5.0×10⁻⁵ mol/L", "1.0×10⁻⁵ mol/L"], 2,
 "c=A/(εb)=0.500/(1.0×10⁴)=5.0×10⁻⁵。"),
("分光光度法选择最大吸收波长的主要原因是（ ）", ["灵敏度最高", "颜色最深", "避免干扰", "仪器默认"], 0,
 "λmax 处 ε 最大，灵敏度最高。"),
("25℃ 时玻璃电极的 pH 响应斜率约为（ ）", ["0.59 mV/pH", "59 mV/pH", "5.9 mV/pH", "590 mV/pH"], 1,
 "2.303RT/F=0.0592 V=59.2 mV。"),
("分配比 D=9，水相与有机相体积相等，一次萃取率为（ ）", ["50%", "75%", "80%", "90%"], 3,
 "E=D/(D+1)=9/10=90%。"),
("分离挥发性有机物最常用的方法是（ ）", ["气相色谱", "液相色谱", "离子交换", "沉淀"], 0,
 "气相色谱适合挥发性、热稳定物质。"),
("电位滴定判断终点的依据是（ ）", ["颜色变化", "沉淀生成", "电势突跃", "气体放出"], 2,
 "用电势突跃或导数极值确定终点。"),
("下列不属于重量分析对称量形式要求的是（ ）", ["组成固定", "性质稳定", "摩尔质量大", "溶解度大"], 3,
 "称量形式应难溶、稳定、组成固定、摩尔质量大；溶解度大是反要求。"),
],
}

for cid, title, slug, topics in UNITS:
    qs = Q[cid]
    lines = [f"# {title}", "", f"- **本单元考点**：{topics}", "- **题量**：8 题（选择题，答案与解析见测验页）", "",
             "## 本单元怎么练", "",
             "先合上书，按顺序做测验页的 8 道题；做完再逐题看解析。错题回到 03 书对应章节，把该节的例题重算一遍。", "",
             "## 题目清单", ""]
    for i, (stem, opts, ans, exp) in enumerate(qs, 1):
        lines.append(f"{i}. {stem}")
        lines.append("   " + "  ".join(f"{chr(65+j)}. {o}" for j, o in enumerate(opts)))
        lines.append("")
    lines += ["## 做完之后", "",
              "把错题对应的公式抄到一张纸上，第二天不看书画一遍。计算题必须自己动手算，不要只看解析。"]
    open(os.path.join(BOOK, "chapters", f"{slug}.md"), "w", encoding="utf-8").write("\n".join(lines))

chapters = [dict(id=cid, title=title, file=f"chapters/{slug}.md", difficulty=2,
                 source="依据《无机及分析化学》与《学习指导》考点自编", prerequisites=[] if i == 0 else [UNITS[i-1][0]])
            for i, (cid, title, slug, topics) in enumerate(UNITS)]
quizzes = []
n = 0
for cid, *_ in UNITS:
    for stem, opts, ans, exp in Q[cid]:
        n += 1
        quizzes.append(dict(id=f"q{n:02d}", chapterId=cid, type="single", question=stem,
                            options=opts, answer=ans, explain=exp, relatedConceptId="",
                            optionMisconceptions=[]))
manifest = dict(
    slug="inorganic-analytical-chem-bank",
    title="无机及分析化学题库：40 题通关",
    subtitle="按五个单元排的单选题，覆盖计算、判断与实验条件",
    book=dict(title="无机及分析化学题库", author="自编（依据教材与学习指导）",
              source=["无机及分析化学 (韩忠霄, 孙乃有).pdf",
                      "无机及分析化学学习指导与习题解析 (马凤霞, 王秀彦).pdf"]),
    audience="已完成 03 书一轮学习、需要做题巩固的人",
    goal="用 40 道单选检验基础计算、四大滴定、沉淀重量、仪器分析，错题可回到 03 书对应章节",
    learningPath=[dict(step=f"0{i+1}", title=t, chapterIds=[c], checkpoint="8 题正确率 ≥ 75%")
                  for i, (c, t, *_rest) in enumerate(UNITS)],
    chapters=chapters, concepts=[],
    glossary=[{"term": "滴定度", "def": "每毫升滴定剂相当于待测物的质量", "chapterId": "ch03"},
              {"term": "条件稳定常数", "def": "扣掉副反应后的有效稳定常数", "chapterId": "ch03"},
              {"term": "换算因数", "def": "待测物与称量形式之间的摩尔质量比（含系数）", "chapterId": "ch04"},
              {"term": "摩尔吸光系数", "def": "A=εbc 中的 ε，表示物质吸光能力", "chapterId": "ch05"},
              {"term": "萃取率", "def": "被萃取到有机相的目标物占总量的百分比", "chapterId": "ch05"}],
    patterns={"file": "patterns.md"}, cheatsheet={"file": "cheatsheet.md"},
    quizzes=quizzes,
    flashcards=[dict(id=f"f{i:02d}", chapterId=cid, front=f"第 {i+1} 单元最重要的公式或判断是什么？",
                     back="见 03 书对应章节的速查表与复习锚点", tags=[cid])
                for i, (cid, *_rest) in enumerate(UNITS)],
    companion="inorganic-analytical-chem-bank学习伴侣.html",
)
json.dump(manifest, open(os.path.join(BOOK, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open(os.path.join(BOOK, "patterns.md"), "w", encoding="utf-8").write(
"# 做题模式\n\n## 单选四步\n1. 先判断考的是哪个章节。\n2. 写出对应公式或条件。\n3. 代数据，注意单位。\n4. 看选项量级，排除明显不合理的。\n\n## 错题处理\n- 计算错：重算一遍，找出哪一步单位或系数错。\n- 概念错：回到 03 书对应章节的精讲和常见误解。\n- 条件错：把指示剂、pH、温度条件抄进速查表。\n")
open(os.path.join(BOOK, "cheatsheet.md"), "w", encoding="utf-8").write(
"# 题库速查\n\n| 场景 | 要点 |\n|---|---|\n| 物质的量 | n=m/M=cV=V/Vm |\n| 弱酸 pH | pH=1/2(pKa−lg c) |\n| 缓冲 | pH=pKa+lg([A⁻]/[HA]) |\n| 配位 | lgK'=lgKf−lgαY(H) |\n| 电极 | E=E°+0.0592/n lg(Ox/Red) |\n| 沉淀 | AB 型 s=√Ksp |\n| 分光 | A=εbc |\n| 萃取 | E=D/(D+V水/V有机) |\n")
print("题库：", len(chapters), "单元", len(quizzes), "题")
