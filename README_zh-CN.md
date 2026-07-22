[English](README.md) | [简体中文](README_zh-CN.md)

# 草类 AI 基因组学证据成熟度框架：可执行配套资源

[![tests](https://github.com/ashelylinluo/grass-ai-readiness/actions/workflows/test.yml/badge.svg)](https://github.com/ashelylinluo/grass-ai-readiness/actions/workflows/test.yml)

本仓库配套稿件 *"AI-driven grass genomics: a user-centric and evidence-guided roadmap from bioinformatics resources to breeding decisions"*（Luo L, Sun Z, Lin Z, et al.）。它提供了证据成熟度框架的可执行实现，使读者能够检查稿件报告的参考评估，并将同一套评价准则应用到新的用例。

该框架围绕草类/禾本科（grass/Poaceae）基因组学中的任何 AI 或生物信息学结果提出一个核心问题：**它能支持一项决策、只能指导一个假设，还是仍然需要基准验证？** 一个工具并不是因为总体表现好就已经“就绪”；只有当证据确实支撑其所声称的具体物种、任务和用户行动时，才可认为它达到相应成熟度。成熟度以特定用例为单位分配为 **tier**：

- **Tier 1 — 决策支持就绪（decision-support ready）：** 在经过验证的条件下支持指定行动（有边界，并非一般性背书）。
- **Tier 2 — 假设指导（hypothesis-guiding）：** 在明确边界内支持候选优先级排序、结果解释或实验设计。
- **Tier 3 — 需要基准验证（benchmark-required）：** 技术上有潜力，但在使用前仍需要更强的任务特异性验证。

tier 是由应用于四个证据门（evidence gates）的有序决策规则推导而来，而不是平均分或总体质量分。四个 evidence gates 分别是：直接草类验证（Direct grass validation）、输入透明度（Input transparency）、基准充分性（Benchmark adequacy）和可访问性与复用性（Accessibility and reuse）。在当前证据快照（2026-07-08）中，18个 reference use cases 的结果为 **0 Tier 1 / 15 Tier 2 / 3 Tier 3**。

---

## 快速复现检查（Quick reproducibility check）

克隆仓库：

```bash
git clone https://github.com/ashelylinluo/grass-ai-readiness.git
cd grass-ai-readiness
```

编译 Python 脚本：

```bash
python -m compileall grass-ai-readiness/scripts
```

复现 18 个 reference assessments 和 10 个 synthetic boundary tests：

```bash
python grass-ai-readiness/scripts/assign_tier.py \
  --selftest \
  grass-ai-readiness/references/anchor-cases.tsv \
  grass-ai-readiness/references/synthetic-boundary-tests.tsv
```

预期输出：

```text
28/28 rows reproduce — all consistent.
```

---

## 仓库内容

本仓库包含三个自动化程度递增的资源：

### 1. 评价准则 — `Supplementary_Table_S5.xlsx`

这里包含定义本身：四个证据门的判定标准（Pass / Partial / Not demonstrated）、leakage 和 action-type 规则、有序决策规则，以及 18 个专家整理的参考评估（expert-curated reference assessments）（UC01–UC18）及其逐门证据。这是事实来源；另外两个资源是对它的可执行化。

### 2. 交互式评估器 — `grass-ai-readiness-assessor.html`

一个单文件、自包含的网页（无需服务器、无需依赖；用任意浏览器打开即可）。设置四个证据门评级、leakage 状态和 action type 后，tier 会实时更新，并高亮显示**触发了哪条决策规则**。它包含全部 18 个 reference cases，并附有逐门证据摘要和来源细节（citation、DOI、version、snapshot date），因此每个案例都可追溯到其来源，也可按 tier 浏览和筛选。它最适合希望查看逻辑并检查参考案例的人工用户。

### 3. Agent Skill（智能体技能）— `grass-ai-readiness/`

一个 [Agent Skill](https://agentskills.io/specification)，可让 AI assistant 将评价准则应用于**新的**用例，而不仅仅是复现这 18 个参考案例。assistant 读取证据并为四个 evidence gates 评级；确定性脚本依据固定规则分配 tier，因此结果不依赖模型的主观判断。它最适合评估稿件未覆盖的工具。

```
grass-ai-readiness/
├── SKILL.md                          # instructions the assistant follows
├── scripts/
│   ├── assign_tier.py                # deterministic tier assignment (the rules, in code)
│   └── validate_assessment.py        # checks an assessment is evidence-backed and rule-consistent
├── assets/
│   └── assessment-template.json      # fillable structured-output template
└── references/
    ├── rubric-definitions.md         # gate definitions + ordered decision rules
    ├── anchor-cases.md               # 18 reference assessments, with evidence + sources
    ├── anchor-cases.tsv              # machine-checkable form
    ├── synthetic-boundary-tests.md   # constructed rows exercising every rule (NOT literature cases)
    └── synthetic-boundary-tests.tsv  # machine-checkable form
```

同时提供了打包后的 `grass-ai-readiness.skill` 文件，供支持该格式的客户端一键导入。开放规范将包含 `SKILL.md` 的*目录*定义为可移植格式，因此上方目录是规范发行形式；`.skill` 文件仅作为便利选项提供。

---

## 如何使用各个资源

### 交互式评估器

在浏览器中打开 `grass-ai-readiness-assessor.html`。无需安装任何内容。

### 直接使用 tier 引擎

决策规则可作为独立脚本运行，适合脚本化处理或验证：

```bash
python grass-ai-readiness/scripts/assign_tier.py \
  --dv P --it P --ba P --ar Pa \
  --leakage No --action decision
# → Tier 2 — hypothesis-guiding   (Rule 7)
```

复现每一个参考行（18 个案例加上 synthetic boundary tests）：

```bash
cd grass-ai-readiness
python scripts/assign_tier.py --selftest \
  references/anchor-cases.tsv references/synthetic-boundary-tests.tsv
# → 28/28 rows reproduce — all consistent.
```

检查一个已完成的评估是否可审计且与规则一致：

```bash
python scripts/validate_assessment.py my_assessment.json
python scripts/validate_assessment.py --references references/
```

`validate_assessment.py` 会强制要求每个证据门都包含提取出的证据*以及*证据位置，并要求记录的 tier 与规则生成的 tier 相同；人工写入的 tier 不能在静默状态下与引擎结果不一致。

### Agent Skill（智能体技能）

安装 `.skill` 文件（或让你的 agent 指向 `grass-ai-readiness/` 目录），然后用自然语言提出成熟度问题，例如 *"Is a wheat-trained sequence-to-function model ready for ranking drought-linked regulatory variants in tall fescue?"* assistant 会界定有边界的用例，依据评价准则和引用证据为四个 evidence gates 评级，运行 `assign_tier.py`，并返回可审计的评估。

---

## 两种评估模式

由于代码仓库和预印本会发生变化，Agent Skill（智能体技能）区分两种模式：

- **快照复现模式（Snapshot reproduction）** — 复现截至 2026-07-08 的稿件评估；18 个 anchor ratings 固定不变。
- **当前证据再评估模式（Current-evidence reassessment）** — 重新检查当前论文、代码仓库、licence 和 release，并基于当前证据重新评级；同时保留原始 anchor，并把任何变化与 recheck date 分开报告。

Tiers 是快照。随着证据、代码或 benchmarks 变化，tier 也可能移动；在依赖某个评级前应重新检查。

---

## 适用范围与注意事项

- 评级具有**用例特异性（use-case-specific）**，不是对论文、工具、开发者或整体科学质量的排名。Tier 3 并不意味着论文不好，而是意味着支持*该决策*的证据尚未到位。
- tier 随所声明的 species/task/action 变化，而不是随方法本身固定。相同模型可以在一个经过验证的群体中是 Tier 1，在迁移到另一个群体后变成 Tier 3。
- 18 个 reference assessments 是**专家整理的（expert-curated）**，并非独立重新验证。
- 本框架生成的评估是解释性辅助，而非权威背书。
- 该评价准则是针对 grass/Poaceae AI-genomics 校准的；对于远离这一领域的用例，其校准可能无法直接迁移。

---

## Licence

代码和交互式评估器以 MIT License 发布（见 `LICENSE`）。参考评估、rubric 文本和表格数据以 CC BY 4.0 发布（见 `LICENSE-DATA`）。

## Citation

如果使用本框架或其实现，请引用已归档记录（另见 `CITATION.cff`）：

> Luo L, Sun Z, Lin Z, et al. Supplementary data and literature-mapping records for "AI-driven grass genomics: a user-centric and evidence-guided roadmap from bioinformatics resources to breeding decisions". Zenodo, 2026. doi:10.5281/zenodo.20825481

*上述 DOI 指向现有的数据记录。该可执行配套资源的独立软件 DOI 将在 GitHub release 归档到 Zenodo 时生成；届时请同步更新此处、HTML 和 `CITATION.cff` 中的 DOI。*

---

## 稿件 Data availability statement 建议用语

> The literature-mapping records and supplementary assessment data are archived on Zenodo (doi:10.5281/zenodo.20825481). The executable companion to the readiness framework is publicly available in the project repository and archived as a versioned software release on Zenodo (doi:[SOFTWARE DOI]). The release includes the manuscript-defined four-gate rubric and 18 expert-curated reference use-case assessments, a browser-based interactive assessor, deterministic tier-assignment scripts, synthetic boundary tests, and an Agent Skill for evaluating new use cases.

*Replace `[SOFTWARE DOI]` with the DOI minted for the GitHub release before inserting this statement into the manuscript.*

以下中文仅供作者内部沟通，正式论文请使用上方英文版本。

上述 Data availability 建议句说明：文献映射记录和补充评估数据已经以 Zenodo 记录（doi:10.5281/zenodo.20825481）归档；证据成熟度框架的可执行配套资源将在项目仓库公开，并在 GitHub release 归档到 Zenodo 后形成带版本的软件发布记录。该发布包含稿件定义的框架（manuscript-defined framework）中的四门评价准则、18 个 expert-curated reference use-case assessments、浏览器交互式评估器、确定性 tier 分配脚本、synthetic boundary tests，以及用于评估新用例的 Agent Skill（智能体技能）。在正式稿件中使用前，请将 `[SOFTWARE DOI]` 替换为 GitHub release 对应的 Zenodo 软件 DOI。
