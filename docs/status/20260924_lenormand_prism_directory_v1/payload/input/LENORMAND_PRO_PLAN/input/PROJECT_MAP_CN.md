# 小星辰 Engine Core 项目 Map

## 1. 用途与权威流

本 Map 只回答“事实主人在哪里、当前证据状态是什么、能否作为 runtime 资料读取”，不
复制产品真值、当前测试数字或实施日志。

本仓服务的产品目的只有一句：卡牌是帮助用户看清局面、变量、成本与选择，再回到现实
解决问题的入口；完整真值唯一主人是
`docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md`，本 Map 只导航。

权威流固定为：爸爸明确决定 → 稳定产品规则或获准批次合同 → candidate、人工复核与
爸爸批准 → 单卡系 approved projection → 单卡系只读检索 → 安全 Host DTO。测试、
RAG、Harness、Validator、audit、Map、Source Mining 和外部模型意见不能反向定义产品
真值或自行批准资料。

本仓存在两个不可混写的面：**开发与资料批次面**和**每用户读牌运行权威面**。
本 Map 同时导航两面，但两面的状态必须分别读取；开发面的绿灯不代表运行面存在。

## 2. 状态解释

组件状态只允许：

- `ABSENT`：仓内没有该能力；指向 Map 自身只用于拥有“缺失”这一事实。
- `SCAFFOLDED`：合同、容器或骨架存在，不能声称完整实现。
- `PARTIAL`：已有可检查实现，但明确缺少一部分闭环。
- `IMPLEMENTED`：当前字节存在对应实现；不等于语义或生产已验证。
- `VERIFIED`：对 current bytes 有机械断言和实际通过证据；文件存在或关键词命中不够。
- `BLOCKED`：已知必要前置缺失，当前不得继续。

运行资料批准状态只允许 `NOT_APPLICABLE`、`NOT_APPROVED`、
`APPROVED_NOT_CONNECTED`、`APPROVED_CONNECTED`。组件状态与真实获准数据状态必须
分开：计划不得冒充 CURRENT，代码或治理组件实现不等于真实资料获准、连接或可读。

“设计候选已完成”不是状态词。存在设计但没有对应字节的能力一律记 `ABSENT`，
其设计成熟度只在 §5 用散文说明，不进入受控表格，也不进入派生 JSON。

## 3. 导航顺序

1. `AGENTS.md`：稳定协作、安全与证据边界。
2. 本 Map：组件状态与事实主人。
3. `PRODUCT_FOUNDATION_REFERENCE_CN.md`：产品最高检查线和来源层边界。
4. `SOURCE_LIFECYCLE_CN.md`：来源准入、批准与 no-match。
5. `docs/status/CURRENT_STATUS_CN.md`：被验收 subject 与 closure 状态。
6. `docs/decisions`：已记录的架构决定。

## 4. 受控状态投影（JSON 唯一来源）

| id | status | approved_runtime_data_status | owner | canonical_path | runtime_readable |
|---|---|---|---|---|---|
| governance.agents | IMPLEMENTED | NOT_APPLICABLE | stable_agent_rules | AGENTS.md | false |
| governance.product_foundation | VERIFIED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| governance.project_map | VERIFIED | NOT_APPLICABLE | project_navigation | docs/governance/PROJECT_MAP_CN.md | false |
| governance.ownership | VERIFIED | NOT_APPLICABLE | document_ownership | docs/governance/DOCUMENT_OWNERSHIP_MATRIX_CN.md | false |
| governance.current_status | IMPLEMENTED | NOT_APPLICABLE | current_status | docs/status/CURRENT_STATUS_CN.md | false |
| governance.source_mining | IMPLEMENTED | NOT_APPLICABLE | batch_source_mining | docs/status/source_mining | false |
| governance.audit | VERIFIED | NOT_APPROVED | audit_index | docs/work_handoff/20260828/audit/EXTERNAL_REVIEW_DECISION_INDEX_20260828.json | false |
| governance.external_review | VERIFIED | NOT_APPROVED | external_review_returns | docs/work_handoff/20260828/output | false |
| governance.decisions | IMPLEMENTED | NOT_APPLICABLE | project_navigation | docs/decisions | false |
| governance.reading_authority | VERIFIED | NOT_APPLICABLE | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| runtime.rag | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/retrieval | false |
| runtime.conversion | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/conversion | false |
| runtime.harness | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/harness | false |
| runtime.mcp | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/mcp | false |
| runtime.skills | PARTIAL | NOT_APPLICABLE | project_navigation | skills | false |
| runtime.skills_evidence | IMPLEMENTED | NOT_APPLICABLE | project_navigation | skills | false |
| runtime.host | PARTIAL | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/hosts | false |
| runtime.provider | BLOCKED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/mcp/tools.py | false |
| runtime.provider_off_stub | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/mcp/tools.py | false |
| runtime.provider_live | BLOCKED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/mcp/tools.py | false |
| runtime.db | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/db | false |
| runtime.domain | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain | false |
| runtime.governance_engine | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/governance | false |
| runtime.observability | IMPLEMENTED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/observability | false |
| runtime.stage_hint_seam | IMPLEMENTED | NOT_APPLICABLE | project_navigation | alembic/versions/20260826_0002_foundation_authority.py | false |
| runtime.reading_authority_per_user | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.stage_controller | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.stage_main_tone | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.stage_density | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.stage_reality_research | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.stage_final_review | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.stage_artifact_store | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.skills_stage | ABSENT | NOT_APPLICABLE | project_navigation | docs/governance/PROJECT_MAP_CN.md | false |
| runtime.research_worker | PARTIAL | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/research | false |
| runtime.research_attempt_receipt | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.provider_second_leg | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/research.py | false |
| runtime.safety_refusal_gate | PARTIAL | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/intake | false |
| runtime.question_reframe_gate | PARTIAL | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/intake | false |
| runtime.querent_isolation | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.profile_ignore_gate | SCAFFOLDED | NOT_APPLICABLE | project_navigation | src/xiaoxingchen_core/domain/reading.py | false |
| runtime.narrative_over_cardwise | ABSENT | NOT_APPLICABLE | project_navigation | docs/governance/PROJECT_MAP_CN.md | false |
| runtime.closing_allowed_not_mandatory | ABSENT | NOT_APPLICABLE | project_navigation | docs/governance/PROJECT_MAP_CN.md | false |
| infra.database | IMPLEMENTED | NOT_APPLICABLE | project_navigation | alembic/versions | false |
| infra.ci | IMPLEMENTED | NOT_APPLICABLE | project_navigation | .github/workflows/ci.yml | false |
| infra.docker | PARTIAL | NOT_APPLICABLE | project_navigation | .github/workflows/docker_build.yml | false |
| infra.cd_registry_deploy | ABSENT | NOT_APPLICABLE | project_navigation | docs/governance/PROJECT_MAP_CN.md | false |
| data.source_vault | BLOCKED | NOT_APPROVED | project_navigation | docs/migration/SOURCE_VAULT_LAYOUT_CN.md | false |
| data.tarot_waite_rws | SCAFFOLDED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| data.tarot_place | SCAFFOLDED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| data.mentor | SCAFFOLDED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| data.book_t_gd | SCAFFOLDED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| data.lenormand_matthews_rana | SCAFFOLDED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| data.consultation | SCAFFOLDED | NOT_APPROVED | product_foundation | docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md | false |
| data.synthetic_fixture | IMPLEMENTED | NOT_APPROVED | project_navigation | tests | false |

## 5. 读牌运行权威与现有基础

产品与读牌语义权威已经由 `PRODUCT_FOUNDATION_REFERENCE_CN.md` 正式拥有；这只证明
治理文字到位，不代表每用户读牌 runtime 已实现。

上表 12 条读牌 `runtime.*` 能力的状态已按 current bytes 复核：其中 11 条的合同层或
机制层字节已存在于 Engine，状态与 canonical_path 已同步更新进 §4 受控表与派生 JSON
（canonical_path 改指实际字节所在）；仅 `runtime.skills_stage` 仍为 `ABSENT`，其
canonical_path 指向本 Map，含义是“本 Map 拥有这条能力缺失的事实”，不是“该能力位于
本 Map”。下表保留设计成熟度与下一 owner：已落字节的行按实际落点改述，仍无字节的行
记 `DESIGNED_NOT_IMPLEMENTED`；两种表述都不是绿灯：

| id | 设计成熟度 | 下一 owner |
|---|---|---|
| runtime.reading_authority_per_user | 合同层已落 Engine；运行链路未接线 | O-W2 |
| runtime.stage_controller | 状态机与顺序强制已落 Engine；阶段执行器未建 | O-W3 |
| runtime.stage_main_tone | 仅阶段标识与封存槽位（R1）；无阶段执行字节 | O-W3 |
| runtime.stage_density | 仅阶段标识与封存槽位（R2）；无阶段执行字节 | O-W3 |
| runtime.stage_reality_research | 仅阶段标识与封存槽位（R3）；无阶段执行字节 | O-W4 |
| runtime.stage_final_review | 仅阶段标识与封存槽位（R4）；无阶段执行字节 | O-W5 |
| runtime.stage_artifact_store | 合同层与 0004 表已落 Engine；存取链路未接线 | O-W2 |
| runtime.skills_stage | `DESIGNED_NOT_IMPLEMENTED` | O-W3 |
| runtime.research_worker | 机制层已实现（出站去标识、预检门、措辞分流）；真 worker 进程不在本仓 | O-W4 |
| runtime.research_attempt_receipt | 合同层与 0004 表已落 Engine；记录链路未接线 | O-W2 |
| runtime.provider_second_leg | 第二通道合同身份已落 Engine；无 Tavily 客户端字节 | O-W4 |
| runtime.safety_refusal_gate | intake 安全门已实现；运行入口未接线 | O-W5 |

`DESIGNED_NOT_IMPLEMENTED` 不是绿灯，不能作为实施授权、验收证据或发布条件。
设计候选存放在审计仓，不在 Engine 内，也不是 runtime 资料。

`runtime.skills` 是聚合行，因此当前为 `PARTIAL`：`runtime.skills_evidence` 只覆盖现有
4 个证据检索与批次控制 Skill，状态 `IMPLEMENTED`；读牌阶段 Skill 单列为
`runtime.skills_stage`，状态 `ABSENT`。

`runtime.provider` 是聚合阻塞行。`runtime.provider_off_stub` 已实现且固定返回
`DISABLED_PROVIDER_OFF`；`runtime.provider_live` 仍为 `BLOCKED`，Tavily 第二通道
`runtime.provider_second_leg` 的通道合同身份已落 Engine（`SCAFFOLDED`），真 provider
仍未接入。stub 不能冒充任何联网能力。

### 5.1 表达层吸纳能力（2026-09-11，爸爸指示）

AGENTS §10 于 2026-09-11 吸纳第三方参考 Skill 的六条表达层规则（问法改写、核对用户牌、
串联叙事、行动视角/收束非固定、换人换事隔离、忽略长期画像）。五行已按红后绿进入
§4 受控 JSON 投影；经 current-byte 复核，问法改写门为 `PARTIAL`、换人隔离与画像忽略
门为 `SCAFFOLDED`，串联叙事与收束非固定两行仍为 `ABSENT`。上列状态均不是实现绿灯
（`SCAFFOLDED` 与 `PARTIAL` 按定义不得声称完整实现）；设计成熟度与下一 owner 仍以下表为准：

| id | 当前 | 设计成熟度 | 下一 owner | 需求 |
|---|---|---|---|---|
| runtime.question_reframe_gate | `PARTIAL` | intake 问法门已实现；运行入口未接线 | B6（安全门）或独立小批 | A17 |
| runtime.querent_isolation | `SCAFFOLDED` | 第七面合同层已实现；运行链路未接线 | B1（第七面对象内） | B05 |
| runtime.profile_ignore_gate | `SCAFFOLDED` | 第七面合同层已实现；运行链路未接线 | B1 | B05 / §13 |
| runtime.narrative_over_cardwise | `ABSENT` | O-N6 部分覆盖 | B3/W05 验收 | A02 / B03 |
| runtime.closing_allowed_not_mandatory | `ABSENT` | O-N6 部分覆盖 | W05 验收 | A18 |

## 6. 资料层与 no-match

所有资料层当前都没有获准且已连接的真实数据。Waite/RWS 与 Place 是 Tarot 核心证据对；
Mentor、Book T/GD 和 Consultation 是独立可空层；Lenormand 的 Matthews/Rana 路线与
Tarot 完全隔离。细节由产品基础拥有。

no-match 的公共码闭集、运行时总序与审计细分注册表只引用
`SOURCE_LIFECYCLE_CN.md`（no-match 唯一主人）；本 Map 不复制状态机，也不复制码表。

## 7. 工程与发布边界

- 当前 RAG、conversion、Harness、MCP、Skills、Host、数据库、CI 与 Docker 状态只描述
  current bytes 的机械能力，不证明牌义、资料真实性、物理隔离或生产资格。
- Source Vault 未连接，Provider 保持关闭；CD、registry、deploy 和 rollback 运行链
  不存在。不得把计划、历史绿灯或外部候选写成当前能力。
- GitHub 机械门和 Draft PR 是绑定 commit 的证据；未配置服务端强制保护时只能标
  `ADVISORY_NOT_SERVER_ENFORCED`。
- 本 Map 正文不得出现 commit 全值、日期字面量或瞬时测试数字；这些属于
  `docs/status/CURRENT_STATUS_CN.md`。

## 8. 停止线与依赖

- I0-R 只修治理声明、证据门和正式产品入口，不改变 `src/`、数据库、migration、
  workflow、Docker、Harness、MCP、Provider、Source Vault 或生产。真实语义资料未迁移、
  Source Vault 未连接时，任何治理绿灯都不能写成读牌产品完成。I0-R 后不得进入 I1。
- `governance.reading_authority` 由 `PRODUCT_FOUNDATION_REFERENCE_CN.md` 正式拥有。
  任何 runtime 实施仍必须有独立白名单、先红后绿证据与爸爸授权；治理文字不能推导实施权。
- 公网研究来源可见性的验收保持阻塞，直到 `SOURCE_LIFECYCLE_CN.md` 的来源名规则被
  窄化为“获准投影来源”，且安全 DTO 的 allowlist 增加可见来源名与 canonical URL 字段。
  只改治理文字不足以解除该阻塞。
- 表中 `ABSENT` 一律不得因为存在设计候选而升级；升级必须以当前字节和实际断言为准。
