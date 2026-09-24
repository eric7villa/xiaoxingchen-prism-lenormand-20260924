# B 雷诺曼实际调用链与断点

状态：DESIGN_CANDIDATE_NOT_AUTHORIZED。全部是固定快照的静态结论；没有启动应用、执行测试、连接数据库或调用模型。

## 1. 证据口径

本文 M、D、L、P 的身份见 BASELINE_COMPARISON.md。`D:foo` 表示 `base/baseline/d_candidate/foo`；`L:foo` 表示 `ln_candidate/foo`。代码简称 `core/` 统一展开为 `src/xiaoxingchen_core/`。所有位置均相对于本次原输入根，而非 Mac 路径。逐文件 SHA 在 INPUT_IDENTITIES.json；350 个已选 Python 文件（M 115、D 222、L 13）的静态符号/引用扫描见 SYMBOL_INDEX.json 和 CALLER_REFERENCE_INDEX.json。选集之外、动态导入、真实部署均不作不存在证明。

“已连接”只表示可见函数调用；“显式阻断”有分支/合同依据；“未见调用者”只限本次完整已选 src/tests；“候选缺边”表示现有两端的类型或职责无法直接闭合。测试中的构造者不等于生产入口。

## 2. 从用户入口追踪

|边|实际文件、符号与证据|静态判断|
|---|---|---|
|服务入口→运行端口|D:core/demo/cli.py:93 选择 PreviewRuntimePort 或 UnavailableRuntimePort；demo/server.py:192 默认后者|只有预览/不可用替身，未接真实 LN 运行端|
|表单→用户事实|D:core/demo/handlers.py:106 `post_intake` 调用 `parse_intake_fields`、`validate_intake`、`evaluate_question`；:175 到 `_advance`；确认分支保留用户确认|共用议题安全/确认可复用，不等于接入牌义|
|事实→端口|D:core/demo/handlers.py:298–324 `_advance` 调 `port.prepare(facts)`，渲染有限状态|已连接 UI 到抽象端口；未见 DemoRuntimePort→LenormandRuntime 的具体适配器|
|LN 牌阵入口|D:core/demo/catalog.py `SPREAD_CATALOG` 已有 `ln-three`，`open_for_intake=False`；`CARD_CATALOG_STATUS=NOT_CONNECTED`|不是“完全没有 LN slug”；是入口关闭且无获准牌表连接|
|替身→答案|D:core/demo/ports.py:39–66 `RuntimeReply` 只准 ANSWER_READY 携带真实正文；:92–142 两替身不产生答案|结构性阻断已存在，不应删掉制造接通假象|
|预览→阶段|同文件 `_pending_skeleton` 使用 R1–R4，Preview 的可选层为 book-t/mentor|这是通用/塔罗遗留预览，不能当 LN 职责设计；LN 适配须隔离这些展示|

## 3. LN 包内部链（D 与 L 分开）

D 已包含 lenormand_runtime 包，不是主参考 M 的缺包可以推导 D 没有包。D 的 prepare 仅做输入/结构、关系检索、简单准入和门构造；L 增补牌表钩子、收窄策略及泄漏检查，但不是已合入 D。

|阶段|L 的准确位置/符号|输入与输出；缺边|
|---|---|---|
|解析|core/lenormand_runtime/contracts.py `parse_lenormand_request_payload`、`LenormandRuntimeRequest`|允许字段有 topic、spread_mode、cards、draw_order、display_positions、position_semantics；orientation 即使 null 也不是 LN 合同。只消费用户实际给牌，不抽牌|
|牌表|同文件 `LenormandDeckCatalog`、`StaticDeckCatalog`、`deck_binding_status`、`assert_cards_in_catalog`；runtime.py:142+|有对象就报 BOUND；None 跳过成员校验。没有证明此对象对应获准 36 张牌表。未知牌表与已知牌表中的非法牌必须分开|
|结构|layout.py `MODE_REGISTRY`、`validate_layout`、`slot_facts`|3 牌 ALLOWED_STRUCTURE_ONLY；5/9 NOT_OPENED。校验数量、重复、排列、位置及无预设位置语义；显示位置名称与真正几何映射仍需显式约束|
|关系|relations.py `assemble_three_card_relations`、`relation_covers_all_members`|从 layout.cards 构造有序线、A→B、B→C、全成员集；覆盖检查按集合，不验证方向语义。显示顺序不能靠模型猜测|
|检索封装|runtime.py:99 `port_retriever` → evidence.py `build_lenormand_query` → `LenormandEvidencePort.retrieve`|传 snapshot/purpose/spread/domain/scenario；未把服务端查询绑定自动传进 admission_policy，stage_hint 也未贯穿|
|内部检索|evidence.py:132 `LenormandEvidencePort` → D:core/retrieval/repository.py `RepositoryRouter` → `EvidenceRepository.retrieve`|已有 internal RetrievalResult 协议；本选集中实际内存实现可见，真实 PG internal 实现未见|
|二次准入|evidence.py:237 `admit_relation_evidence`|查系统/来源、用途、可选 scope、全成员覆盖、usage role；expected 字段 None 意味不检查，allowed_relation_kinds None 意味不限制；身份绑定 OR 不等于完整绑定|
|核心门|evidence.py:361 `CoreEvidenceGate`、:389 `gate_from_admissions`|只要有 core_items 即可；未纳入获准牌表、完整 snapshot/release/approval、组合方法授权、整体覆盖闭合。是静态设计缺口，不是线上漏洞复现|
|生成前门|evidence.py:382 `guarded_generate`|是可用辅助函数，但本选集没有 LN 生产编排调用模型的闭环，不能把函数存在当实际零调用证明|
|输出|runtime.py `output_port` → output.py `LenormandOutputPort.render` / `render_public`|render 在已有 judgment 上检查门，不能替代生成之前的授权检查；public allowlist 与防逐牌词典、防身份泄漏分开|
|解释授权|relations.py `require_relation_interpretation_authority`|目前始终拒绝；prepare 不调用它。因此不能说整个 prepare 已由此门保护，也不能为接通而直接删拒绝|

## 4. PostgreSQL / MCP 真正的数据形状

D:core/mcp/server.py:112–119 在有数据库 URL 时实例化 `PostgresEvidenceTools.from_url`，否则 `empty_router`。这只是可见工厂路径，本轮未访问 URL 或启动服务。

D:core/mcp/postgres_tools.py `PostgresEvidenceTools._retrieve` 从各系统隔离的 mcp 视图取 ACTIVE 投影，按冻结的八段过滤链执行；LN 卡检索用数组交叠召回，不代表整组组合成立。`lookup_lenormand_core` / `lookup_lenormand_method` 要求对应 purpose 和 LN 来源层。结果构造 `PublicRetrievalResult`，不是内部 `RetrievalResult`。

D:core/domain/evidence.py:303–347 的 PublicEvidenceItem 只含 content、card_bindings、spreads、domains、scenarios；PublicRetrievalResult 只含 matched_items、no_match_reason、truncated。item_id、projection_id、source_span_ref、provenance_ref、usage_boundary、lifecycle、scope kind、query_hash、snapshot_id 不在 public 面。因此不得反向从公共文本或卡名生成“批准身份”。

候选缺边：PG 受信只读服务端消费端 → 内部证据及权威绑定 → LN 二次收窄。推荐在既有 EvidenceRepository / RetrievalResult 合同上添加最小私有读模型，由既有来源/发布/批准记录派生，保持 MCP public 合同不暴露身份。详细字段与权限见 SPEC.md、INTERFACE_REQUESTS.json；不另建同义批准台账。

## 5. 生命周期与持久化边界

来源入口的真实治理落点包括 D:core/domain/lifecycle.py、domain/conversion.py、conversion/promotion.py、governance/review.py 及 D:alembic/versions/20260825_0001_foundation.py、20260826_0002_foundation_authority.py、20260827_0003_candidate_applicability.py。candidate、user_approvals、review_decisions、projection_releases/items、active/mcp 视图已有独立职责。仅看到 ACTIVE 字符串不能替代这些链上的真实批准验证。

D 的 reading/source 运行绑定位于 domain/reading.py、stages/ports.py、stages/postgres_store.py，以及 20260919_0008_reading_delivery_binding_p04.py 的 `reading.source_snapshots` / `reading.pin_source_snapshot`。这些用于读牌工件/交付绑定，不等于 LN 资料自动获准，也不能用读取 public 面代替 pin 原始权威事实。共享变更由 S02/S04 主人吸收，B 不修改它们。

## 6. 研究、审查、输出的缺边

D:core/stages/executor.py:133 `TarotStageExecutor` 明确只支持 Tarot；其 `_retrieve_core_evidence`（:509）构造 TarotEvidenceQuery 与 WAITE_RWS/PLACE；`intake` 发 R1–R4 allowlist，`deliver` 要 R4_SEALED。LN 不得把三牌塞进该执行器或重命名系统后继承固定塔罗职责。

D:core/stages/ports.py 已有单次模型、研究、时钟、ReadingStore 等端口，可复用的是预算/TTL/撤权/隔离/工件完整性机制，不是牌义或阶段职责。`PostgresEvidenceTools.research_with_grok` 为 provider-off stub；研究端口的状态区分 DISABLED、PROVIDER_OFF、SEARCH_FAILED、NO_RELIABLE_SOLUTION、BOUND_BLOCKED。没有网络权时不得伪称“搜过无解”。LN runtime 本身无现实研究、独立审查、持久化交付和真正模型端口调用者。

候选串联顺序为：用户给牌与确认 → 安全/当次身份隔离 → 牌表/布局绑定 → 受权核心/方法检索 → 组合覆盖与主张边界 → 现实约束核对（无网络时仅用用户事实）→ 独立审查 → 生成/展示与交付回读。它不是新的全项目阶段枚举，不映射塔罗 R1–R4。本轮所有这些新增连线仅写任务，不实施。

## 7. 断点总账

明确存在：LN slug 关闭、5/9 registry 关闭、public 字段剥离、CoreEvidenceGate 简化门、解释授权函数恒拒绝、Tarot 专用执行器。

选集未见：获准 36 牌生产牌表实现；PG→LN internal 受权适配器；DemoRuntimePort→LN 真实适配器；LN 专用生成/审查/研究/交付编排。此“未见”不推断选集外或线上状态。

待外部证据：原书获授权文本、批准记录实值、真实 DB 角色与迁移后的视图/事务行为、远端 CI、真实运行效果。以上各缺口只阻断相应运行/语义验收，不阻断本设计与纯结构验收规划。
