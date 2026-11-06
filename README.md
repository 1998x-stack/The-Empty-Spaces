# The Empty Spaces

# 《空位——门捷列夫与元素周期表的发现》

*The Empty Spaces: Mendeleev and the Discovery of the Periodic Table*

一本围绕元素周期律发现历史的中文叙事性非虚构著作：从18世纪元素概念的建立，经19世纪科学家之间的探索与竞争，到1869年门捷列夫的元素周期系统、1875—1886年实验检验，以及后来原子序数与量子理论对周期律的解释。

## 阅读入口

**[直接阅读序章：一个数字，足以推翻整个理论](manuscript/00-prologue/prologue.md)**

**[第一章：33种基本物质——拉瓦锡的化学革命](manuscript/part-01-chaos/chapter-01.md)**

[查看全书目录与全部22章](manuscript/CONTENTS.md)

## 书稿状态

- 书名：已确定（中英文）。
- 结构：序章 + 五部22章 + 尾声。
- 序章：已完成盐选式历史非虚构叙事修订稿，待原始史料逐项审校；明确区分1875年发现镓与1876年密度复测。
- 第一部第1章：完整叙事初稿已完成，附8条史料注释及审校清单；其余第2—22章和尾声仍为**非空占位稿**，尚未撰写正文。

## 仓库布局

```text
manuscript/
  CONTENTS.md
  00-prologue/                 序章（正文）
  part-01-chaos/              第一部（4章）
  part-02-competitors/        第二部（5章）
  part-03-discovery/          第三部（5章）
  part-04-verification/       第四部（4章）
  part-05-legacy/             第五部（4章）
  06-epilogue/                尾声
research/                     文献／事实核验／时间线
editorial/                    编辑与史料规范
assets/                       图像及版权清单
scripts/                      书稿结构检查
```

## 质量与校核

执行 `python3 scripts/check_manuscript.py`，校验目录章节数量、链接及序章正文基本完整性（不替代历史事实审校）。

史料入口：[来源清单](research/sources.md) · [时间线](research/chronology.md) · [事实核验](research/fact-check.md) · [编辑规范](editorial/STYLE_GUIDE.md) · [叙事引擎](editorial/NARRATIVE_PLAYBOOK.md)

## 版权

本仓库公开可读，不代表书稿已经以开放许可证授权。未经作者／权利人明确许可，不应将内容用于再出版、改编或商业传播。第三方引文和图像适用各自的权利状态。
