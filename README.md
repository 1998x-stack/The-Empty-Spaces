# The Empty Spaces

# 《空位——门捷列夫与元素周期表的发现》

*The Empty Spaces: Mendeleev and the Discovery of the Periodic Table*

一本围绕元素周期律发现历史的中文叙事性非虚构著作：从18世纪元素概念的建立，经19世纪科学家之间的探索与竞争，到1869年门捷列夫的元素周期系统、1875—1886年实验检验，以及后来原子序数与量子理论对周期律的解释。

## 阅读入口

**[直接阅读序章：一个数字，足以推翻整个理论](manuscript/00-prologue/prologue.md)**

**[第一章：33种基本物质——拉瓦锡的化学革命](manuscript/part-01-chaos/chapter-01.md)**

**[第二章：看不见的原子——道尔顿的大胆假说](manuscript/part-01-chaos/chapter-02.md)**

**[第三章：三个元素的秘密——德贝莱纳的第一次突破](manuscript/part-01-chaos/chapter-03.md)**

**[第四章：一场混乱的测量——谁能相信原子量？](manuscript/part-01-chaos/chapter-04.md)**

**[第五章：1860年，卡尔斯鲁厄——一场改变科学的大会](manuscript/part-02-competitors/chapter-05.md)**

**[第六章：元素缠绕的圆柱——尚古多被忽视的发现](manuscript/part-02-competitors/chapter-06.md)**

**[第七章：每逢第八个——纽兰兹与八音律](manuscript/part-02-competitors/chapter-07.md)**

**[第八章：来自德国的竞争者——迈耶距离终点有多近？](manuscript/part-02-competitors/chapter-08.md)**

**[第九章：从西伯利亚到彼得堡——一个化学家的成长](manuscript/part-02-competitors/chapter-09.md)**

**[第十章：一本写不下去的教科书](manuscript/part-03-discovery/chapter-10.md)**

**[第十一章：元素卡片——在纸张上寻找自然秩序](manuscript/part-03-discovery/chapter-11.md)**

**[第十二章：1869年2月——元素之间第一次出现了秩序](manuscript/part-03-discovery/chapter-12.md)**

**[第十三章：给不存在的元素留下位置](manuscript/part-03-discovery/chapter-13.md)**

**[第十四章：从假说到预言——1871年的周期系统](manuscript/part-03-discovery/chapter-14.md)**

**[第十五章：1875年，镓——来自法国的第一份实验判决](manuscript/part-04-verification/chapter-15.md)**

**[第十六章：1879年，钪——第二个空位被填满](manuscript/part-04-verification/chapter-16.md)**

[查看全书目录与全部22章](manuscript/CONTENTS.md)

## 书稿状态

- 书名：已确定（中英文）。
- 结构：序章 + 五部22章 + 尾声。
- 序章：已完成盐选式历史非虚构叙事修订稿，待原始史料逐项审校；明确区分1875年发现镓与1876年密度复测。
- 已完成序章及第1—16章的完整叙事初稿，全部待原始资料逐项审校；各部前章均有专项事实核查。第三部第10—14章已形成完整初稿，第四部第15、16章已完成实验验证史初稿，分别处理1875年镓的发现与1876年密度复测，以及1879年钪的发现和类硼识别；第17—22章与尾声仍为正文占位稿。

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
