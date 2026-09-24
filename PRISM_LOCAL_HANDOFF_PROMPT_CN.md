# Prism 本地 Lenormand 完整执行 Prompt

> 这是一次本地文件读取与离线设计审查。不要读取 GitHub，不要把 GitHub 的 `Cache miss` 当作文件不存在，也不要索取任何凭据。

## 0. 直接执行

收到本 Prompt 后立即开始，不要先要求重新上传 ZIP。当前工作区中应存在：

```text
docs/status/20260924_prism_handoff/START_HERE_CN.md
docs/status/20260924_prism_handoff/public_mirror/
```

先完整读取 `START_HERE_CN.md`，再把 `public_mirror/` 视为本批唯一输入根。不要访问用户 Downloads、旧 PHP 仓库或 GitHub URL。

如果 `START_HERE_CN.md` 或 `public_mirror/` 不存在，逐项报告缺失路径并停止为：

```text
READ_CHANNEL_UNAVAILABLE / UNVERIFIED
```

不得根据文件名、摘要、历史记忆或模型共识补齐缺失内容。

## 1. 项目身份与不可变边界

实施项目是 `TarotEngine`，不是 `<legacy-php-reference>`。本轮只做 Lenormand 当前基线复核、资料覆盖审计、详细设计和候选裁决；不做生产发布。

产品目的：用户提出真实问题并提供自己实际抽到的牌面，系统在获准来源和严格边界内，帮助用户看清局面、机制、变量、成本、选择、验证信号、边界和退出，回到现实解决问题。

本轮必须保持：

- Tarot 与 Lenormand 完全隔离；
- Lenormand 不使用 Tarot orientation、逆位、RWS/GD、Book T、Tarot Mentor 或 Tarot 的 R1–R4 位置语义；
- 三牌是当前最小候选路径；五牌、九牌默认关闭并独立解锁；
- 不自动抽牌，不制造用户事实、人物、地点、日期、动机、医疗、法律、经济结论或保证结果；
- 缺少获准资料、批准投影、生命周期或安全条件时使用 `UNAVAILABLE`、`HOLD`、合法 `NO_MATCH` 或 `NOT_AUTHORIZED`；
- 候选设计、静态检查、模型回包和文件存在都不等于资料批准、runtime 授权或上线。

## 2. 输入读取顺序

只读取本地镜像中实际存在的文件，按以下顺序登记读取结果：

1. `PUBLIC_MIRROR_NOTICE_CN.md`
2. `PUBLIC_SOURCE_IDENTITY.json`
3. `docs/status/20260924_lenormand_prism_directory_v1/README_CN.md`
4. `docs/status/20260924_lenormand_prism_directory_v1/READING_MAP_CN.md`
5. `docs/status/20260924_lenormand_prism_directory_v1/PRISM_EXECUTION_PROMPT_CN.md`
6. `docs/status/20260924_lenormand_prism_directory_v1/PRISM_BWRAP_FALLBACK_PROMPT_CN.md`（只读规则，不因 `Cache miss` 自动执行）
7. `docs/status/20260924_lenormand_prism_directory_v1/payload/COVERAGE_AUDIT_CN.md`
8. `docs/status/20260924_lenormand_prism_directory_v1/payload/MATERIAL_COVERAGE.json`
9. `docs/status/20260924_lenormand_prism_directory_v1/payload/MISSING_MATERIALS.json`
10. `docs/status/20260924_lenormand_prism_directory_v1/payload/PROMPT_CN.md`
11. `docs/status/20260924_lenormand_prism_directory_v1/payload/input/LENORMAND_PRO_PLAN/README_CN.md`
12. `INPUT_INDEX.json`、`PACKAGE_MANIFEST.json`、`PACKAGE_SHA256SUMS`、`LENORMAND_BASELINE_REPORT_CN.md`、`LENORMAND_DETAILED_PLAN_CN.md`、`PROMPT_CN.md`
13. `input/AGENTS.md`、`input/PRODUCT_FOUNDATION_REFERENCE_CN.md`、`input/PROJECT_MAP_CN.md`、`input/SOURCE_LIFECYCLE_CN.md`
14. `input/LN_PLAN/` 下所有实际存在的计划、规范、接口、任务、依赖、缺口、主人决定和来源锚点文件
15. `input/RECENT_24H/` 下所有实际存在的文件
16. `input/DOUBAO_ALIGNMENT_AUDIT/` 下所有实际存在的文件

`DIRECTORY_EXTRACTION_INDEX.json` 只用于理解原始目录的递归解包关系，不代表被排除的文件已提供。

公共镜像已对本机路径和外部审查工作区做脱敏；因此不要把脱敏副本声称为原始来源字节，也不要重新计算出“原始包 hash 已验证”的结论。`PUBLIC_MIRROR_SHA256SUMS` 只能验证当前脱敏镜像。

## 3. 开工记录与五项读题协议

在任何分析、裁决或设计之前先写一份开工记录，至少包含：

- 当前实际工作区路径（若不可观察则写 `UNVERIFIED`）；
- 输入根目录和实际存在文件数；
- 公共镜像身份、源分支/源提交记录（仅按 `PUBLIC_SOURCE_IDENTITY.json`）；
- 本地镜像 SHA 校验结果；
- 可用、缺失、被排除和未授权的资料组；
- 本轮允许写入路径和禁止动作。

对每一个任务、资料裁决和验收项，**必须先列出以下五项，再开始计算或实施**：

1. 可观察信息；
2. 可控制动作；
3. 不可用信息/权限；
4. 成功量词；
5. 最坏失败构造。

缺少任一项，不得写 `PASS`、`DONE`、`APPROVED`、`READY_FOR_DEPLOY` 或“已完成上线”。

## 4. 必须完成的审查工作

### 4.1 基线重绑

- 绑定当前本地镜像身份、公共镜像 commit/tag、manifest、SHA 和读取范围；
- 区分当前字节、历史回包、候选设计、模型建议、未批准资料和缺失原件；
- 读取并复核 Doubao alignment audit，但把它当外部候选证据，不当作爸爸批准；
- 对 Astra/P01–P07 相关记录只使用镜像中实际存在的文件，不把缺失的 `ASTRA_RETURNS_7` 原始证据树当作已读；
- 明确指出脱敏路径、镜像排除项、缺失 13 个历史精确文件（若输入记录仍如此声明）及其影响；
- 不修改主项目代码、AGENTS、产品基础、生命周期主人或任何原始输入。

### 4.2 资料覆盖与准入

分别裁决下列资料组，不得混为一组：

1. 获准 36 牌 Lenormand 目录；
2. Matthews 结构/组合/牌阵方法资料；
3. Rana 日常信号/组合补充资料；
4. Book T/GD；
5. Tarot Mentor（旧 60、新 24、师姐宝剑 6/8、历史 281）；
6. 书中案例、模型回包、摘要、候选 projection；
7. 私有 retrieval、批准链、撤回、TTL、ACL 和真实数据库回执。

每组给出：实际路径、输入身份、来源角色、字节/哈希可见性、生命周期、当前状态、对三牌的影响、后续解锁证据。`UNAVAILABLE` 不得被改写成 `PARTIAL_APPROVED`。

### 4.3 三牌最小路径设计

形成从用户输入到输出的完整候选合同，至少覆盖：

- 用户真实问题、真实三张牌、牌序/相邻关系和无 orientation 合同；
- 36 牌成员校验、重复牌、未知牌、空输入、缺牌和非法输入的 fail-closed；
- Matthews/Rana 的来源角色与证据作用域；
- 组合、相邻牌、中心/焦点、线方向、障碍/路径、短期验证信号和现实条件；
- 获准 evidence 读取、scope、候选/审阅/批准/release/snapshot 生命周期；
- 合法 `NO_MATCH`、来源缺失、撤源、冲突、provider-off 和安全失败状态；
- 现实研究只服务解法层，不回填牌义、用户事实或来源身份；
- R4/隔离审查如有设计，明确其输入是冻结工件，不得新建牌义或重新检索；
- 普通用户输出不得泄露治理路径、hash、生命周期、Prompt、内部 ID 或候选状态。

### 4.4 五牌/九牌边界

保留候选设计但默认关闭：

- 五牌：`现状 / 助力 / 阻力 / 隐藏变量 / 建议`；第三张是阻力兼中轴，不得单牌独断；必须检查 `1→2、2→3、3→4、4→5`；
- 九牌：中心、中心周围、横线/竖线为主，对角线仅在另有获准方法时作为辅助；几何参与数量不是语义权重证明；
- 五牌和九牌必须各自有来源身份、模式 allow-list、浏览器/API 关闭门、独立批准、独立回归和独立开启条件；
- 不得用三牌测试冒充五牌/九牌语义验收，也不得把作者方法缺失时的几何实现写成已获准牌义。

### 4.5 既有候选/补丁裁决

对镜像中实际存在的 patch、候选文件、测试或差异逐项标记：

- `KEEP_CANDIDATE`
- `REWORK`
- `HOLD`
- `REJECT`
- `NOT_PRESENT`

每项给出原文件路径、当前 hash（若可见）、问题、证据、最小修改、依赖、回滚和正反验收。没有实际目标代码和授权时只做裁决，不应用补丁。

## 5. 任务和验收设计要求

将后续工作拆成文件级任务，至少覆盖：

1. 基线/输入身份；
2. 36 牌目录与来源 admission；
3. 私有受权读取与持续有效性；
4. 三牌解析与组合支持；
5. no-match、撤源、冲突、TTL、ACL、幂等；
6. 独立编排、冻结工件、R4 审查和交付；
7. 研究边界与去标识化；
8. 五牌/九牌关闭和未来解锁；
9. schema、迁移、CI、证据与回滚。

每个任务必须包含：owner、write-set、producer/consumer、输入身份、前置依赖、权限、失败码/状态、正常例、反例、先红后绿信号、精确验收文件/符号/命令、回滚顺序和当前状态。

每条验收必须是成对的好例/坏例，并区分：

- 设计证据；
- 静态机械检查；
- 本地实际测试；
- 资料语义批准；
- 真实 DB/Provider/浏览器/远端 CI；
- 发布授权。

没有实际运行就写 `NOT_RUN + 原因`，不能用“文件存在”“旧报告通过”“模型一致”替代。

## 6. 必须落盘的输出

允许写入：

```text
docs/status/20260924_prism_handoff/returns/PRISM_LOCAL/attempt_001/
```

必须实际写入并读回以下文件；不能写回时，完整输出每个文件内容并标记 `OUTPUT_WRITE_NOT_AVAILABLE`：

```text
RETURN_CN.md
SOURCE_MINING.md
LN_BASELINE_REBIND.json
LN_SPEC_CN.md
LN_INTERFACE_CONTRACTS.json
LN_TASKS.json
LN_ACCEPTANCE_MATRIX.json
LN_GAP_REGISTER.json
LN_DEPENDENCY_DAG.json
LN_PATCH_ADJUDICATION.json
MATERIAL_COVERAGE_FINAL.json
MISSING_MATERIALS_FINAL.json
BOOKT_MENTOR_DECISIONS.md
LN_SOURCE_ADMISSION_PLAN.md
TASKS_MATERIAL_GATES.json
ACCEPTANCE_MATERIAL_GATES.json
CHECKS.json
MANIFEST.json
SHA256SUMS
```

`MANIFEST.json` 与 `SHA256SUMS` 的覆盖规则必须明确，不能自引用；重新打开/读取所有输出后再写最终回执。输出目录不能包含 API key、token、cookie、Keychain、数据库凭据、生产日志或未脱敏用户资料。

## 7. 状态与停止门

最终状态只能是：

- `DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW`：设计文件齐全、输出可读回、镜像校验通过，但仍未批准、未实施、未运行；
- `PARTIAL_PENDING_CODEX_REVIEW`：有明确完成部分和剩余文件/证据；
- `HOLD_WITH_EXACT_GAPS`：缺失输入或权限阻断当前必要工作，并逐项给出解锁条件。

不得写 `READY_FOR_DEPLOY`、`APPROVED`、`RUNTIME_AUTHORIZED` 或“全量完成”。

真实 PostgreSQL、Provider、浏览器用户链、远端 CI、部署、发布、资料批准、runtime projection 和 API key 使用均保持 `NOT_RUN` / `NOT_AUTHORIZED`。

完成本 Prompt 的离线范围后立即停止，返回：核心结论、P0/P1 风险、实际写入、校验命令与退出码、NOT_RUN、缺失资料、回滚点和下一道人工门。不要自动访问 GitHub、不要提交主仓库、不要公开/关闭仓库、不要执行部署。
