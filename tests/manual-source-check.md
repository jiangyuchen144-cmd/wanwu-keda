# 人工来源抽查

独立审查之外，对涉及外部数字的题做一次人工抽查。目的不是替代审查，而是检查「来源是否真的支持正文」。

- 抽查日期：2026-11-12
- 抽查范围：q3、q4、q5、q7 的主要外部数字
- 方法：打开原始链接/机构页面；记录序列名、年龄段、日期、口径

## q3

| 正文主张 | 来源 | 核对结果 |
| --- | --- | --- |
| 世界银行 2025 年 6 月后国际极端贫困线为 3.00 美元/天（2021 PPP） | [World Bank: Measuring Poverty](https://www.worldbank.org/ext/en/topic/poverty/measuring-poverty) | **支持**。页面明确写「global poverty lines were updated in June 2025」「$3.00 per person per day」「around 1 in 10 people」 |
| UNDP 2025 MPI：109 国约 11 亿人，半数以上儿童 | [UNDP 2025 Global MPI](https://hdr.undp.org/content/2025-global-multidimensional-poverty-index-mpi) | **支持**。页面写 109 countries、1.1 billion、over half children |
| Chetty et al. 2016 MTO 后续 | AER 链接 | 未逐页核对；题面结论与论文公开摘要方向一致，保留为待审 |
| Acemoglu et al. 2001 殖民死亡率工具变量 | AER 链接 | 未逐页核对；正文已说明识别假设强、有争议 |
| Kraay & McKenzie 2014；Banerjee et al. 2015 | JEP / AEJ 链接 | 未逐页核对；正文以「综述/六国实验」限定，未给精确效应量 |

## q4

| 正文主张 | 来源 | 核对结果 |
| --- | --- | --- |
| 美国 2026-10 失业率 4.1% | [FRED UNRATE](https://fred.stlouisfed.org/series/UNRATE) | **支持**。Oct 2026: 4.1，Updated Nov 6, 2026 |
| 美国 2026-10「25-54 岁就业人口比 71.9%」 | 草稿链接 [FRED LNS11300036](https://fred.stlouisfed.org/series/LNS11300036) | **不支持/错配，已修正**。LNS11300036 是「Labor Force Participation Rate - 20-24 Yrs」，2026-10 为 71.9；25-54 岁就业人口比是 [LNS12300060](https://fred.stlouisfed.org/series/LNS12300060)，2026-10 为 **80.7**。最终答案已改为 80.7% / LNS12300060 |
| Stanford Canaries 2026-08：19%、15%、11%、10%，非因果 | [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/news/canariesaug26/) | **支持**。页面明确 19% / 15% / 11% / 10%，并写「descriptive patterns, not causal estimates」 |
| ILO–NASK 2025：全球 25%，高收入 34% | [ILO news](https://www.ilo.org/resource/news/one-four-jobs-risk-being-transformed-genai-new-ilo%E2%80%93nask-global-index-shows) | **支持**。25 per cent global；高收入 34 per cent |
| Eloundou 2023：80% / 19% | arXiv:2303.10130 | 未逐页核对；这是常见的任务暴露估计，正文已标「能力暴露，不是失业预测」 |
| Acemoglu 2024：TFP ≤0.66%，难任务 <0.53% | [NBER WP 32487](https://www.nber.org/papers/w32487) | **支持**。摘要明确 0.66%、0.53% |

**结论**：q4 草稿存在一个明确的数据/来源错配。它不改变「美国总量未崩塌」的方向，但必须修正数字和链接；否则读者会拿 20-24 岁劳动参与率当 25-54 岁就业人口比。

## q5

| 正文主张 | 来源 | 核对结果 |
| --- | --- | --- |
| Acemoglu et al. 2019：民主化使人均 GDP 长期提高约 20% | [MIT DSpace 摘要](https://dspace.mit.edu/entities/publication/06a93eaf-b0a8-4c93-a0bf-d9771698b99a) | **支持**。摘要写「about 20 percent in the long run」，并提 dynamic panel、propensity score、IV |
| Przeworski et al. 2000 的增长结论 | 原书 | 未核对原书数据表；草稿自己标为二手摘要、中等证据 |
| Sen 的饥荒论证 | Development as Freedom | 未逐字核对；草稿已限定为「大规模饥荒」并说明条件 |
| V-Dem/Polity/Freedom House 编码差异 | 方法常识 | 未逐一核对具体国家；草稿标为方法层面判断 |

## q7

| 正文主张 | 来源 | 核对结果 |
| --- | --- | --- |
| Gollwitzer & Sheeran 2006 元分析：94 项研究，d≈0.65 | ScienceDirect 章节；常见摘要表述为「94 independent tests」 | **已修正**。草稿把「独立检验」写成「研究」；独立审查核对后改为「94 个独立检验」，d=0.65 保留。ScienceDirect 本次返回 403，审查看法标为付费墙限制，不是链接失效。 |
| Sirois & Pychyl 2013：拖延优先修复当下情绪 | 2013 综述 | 未读全文；草稿只作为解释框架，未做个人诊断，方向可保留 |

## 说明

- 「支持」只表示来源页面与正文数字/方向一致，不表示该研究本身无争议。
- 未逐页核对的原始论文不能标「已核实」；草稿中保留「中等证据/未读原文」的限定是正确方向。
- 人工抽查发现的问题会与独立审查结果并列写入 `tests/test-report.md`；不因为审查没发现就当作通过。
