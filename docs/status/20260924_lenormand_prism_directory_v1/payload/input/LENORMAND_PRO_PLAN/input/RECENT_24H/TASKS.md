# B 雷诺曼精确实施切片

DESIGN_CANDIDATE_NOT_AUTHORIZED。全部命令 NOT_RUN；本检查点仅含设计。

路径均为未来目标仓库相对路径，不允许修改本附件输入。EXISTING_D 绑定 D 文件 SHA；PROPOSED_NEW 在 D 中不存在；候选中已有但 D 没有的符号明确记 candidate_only_symbols，实施时仍属新增。先重绑实际目标和前置任务输出，再写成对测试实测 RED，获独立实施授权后改最小代码实测 GREEN；本轮均 NOT_RUN。既有正确行为不得捏造 RED。环境按本 D pyproject 的 Python 3.12 与锁定依赖，不能临时联网安装；PG 测试另需授权的临时 PostgreSQL 17。共享接口未接受只阻断相应接线，不阻断局部设计。

## B-LN-T00 基线重绑与候选采用台账

需求：B-LN-R01, B-LN-R12, B-LN-R14

主人：Codex 集成主人；依赖：none

目标以 D 为参考；逐文件采用 L/P，不整树覆盖。L 的 DS08 BASE_READING_SHA256 与 D 不同且 patch 未携该行；按真实目标重审重绑，不改 reading.py 凑 hash。

### 精确 write-set

- `docs/design/lenormand/BASELINE_ADOPTION.md` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：baseline_adoption_ledger.
- `tests/sprint48/lenormand/test_ds08_lenormand_runtime.py` [EXISTING_D] 既有符号：test_domain_modules_resolve_into_the_candidate_workdir；候选新增符号：reviewed_BASE_READING_SHA256_binding.
- `tests/sprint48/lenormand/test_b_baseline_binding.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_baseline_binding_controls.

字段、状态与失败：baseline SHA、采用/拒绝 delta、导入根；错版本停止本批

生产者 → 消费者：冻结 M/D/L/P -> 目标worktree/采用台账/测试

权限：另批代码授权；不改 A/原附件/旧检查点

迁移：无

回滚：撤自己工作树增量，保留采用记录，不回写输入

CI: 模块导入根与基线hash、写集闭合；153/164不继承

主人裁定：工程建议 D 为目标逐文件吸收，无需爸爸技术投票

验收：AC-B-01, AC-B-02

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_baseline_binding.py -m 'not integration and not mutation'`

## B-LN-T01 三牌规范槽与有向关系几何

需求：B-LN-R02, B-LN-R03, B-LN-R11

主人：LN结构主人；依赖：B-LN-T00

复用 THREE_CARD_LINE 和 ln-three；保留原始用户 facts，按明确显示槽而非任意数组顺序构造关系；不抽牌/不补牌/不逆位，结构仍 NOT_APPROVED。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/contracts.py` [EXISTING_D] 既有符号：LayoutMode, parse_lenormand_request_payload；候选新增符号：ResolvedLayoutInput.
- `src/xiaoxingchen_core/lenormand_runtime/layout.py` [EXISTING_D] 既有符号：ModeSpec, validate_layout, slot_facts；候选新增符号：canonicalize_three_card_slots, spread_slug_for_mode.
- `src/xiaoxingchen_core/lenormand_runtime/relations.py` [EXISTING_D] 既有符号：assemble_three_card_relations, dedupe_relation_instances；候选新增符号：validate_relation_identity, parse_relation_id.
- `tests/sprint48/lenormand/test_b_geometry.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_geometry_controls.

字段、状态与失败：规范左中右、ref-slot一一映射、draw_order排列、direction/kind/members一致；非法输入沿用受治拒绝

生产者 → 消费者：用户确认 -> layout -> relation instances -> 准入

权限：局部代码授权；几何不依赖原书，不启用入口

迁移：无；registry数据版本变化需显式绑定

回滚：回退局部几何，不改原输入或默认关闭

CI: 输入/槽/方向正反与跨系统回归

主人裁定：推荐显式显示槽映射，不增加过去现在未来职责

验收：AC-B-03, AC-B-04, AC-B-05

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_geometry.py -m 'not integration and not mutation'`

## B-LN-T02 私有授权读模型与public去标识

需求：B-LN-R04, B-LN-R05, B-LN-R08, B-LN-R13

主人：S02合同 + S04数据主人；依赖：B-LN-T00

复用 RetrievalResult/LenormandEvidenceItem，增加既有 DB 事实镜像，不创造第二审批源。旧无绑定fixture仍可做结构测试但不得生产开门。public投影保持不增身份字段。

### 精确 write-set

- `src/xiaoxingchen_core/domain/evidence.py` [EXISTING_D] 既有符号：RetrievalResult, LenormandEvidenceItem, PublicRetrievalResult；候选新增符号：ProjectionConsumptionBinding, EvidenceApprovalBinding.
- `src/xiaoxingchen_core/retrieval/repository.py` [EXISTING_D] 既有符号：EvidenceRepository, RepositoryRouter；候选新增符号：private_binding_contract_notes.
- `schemas/v1/contracts/retrieval-result.schema.json` [EXISTING_D] 既有符号：（无）；候选新增符号：consumption_binding_schema.
- `schemas/v1/contracts/evidence-item.schema.json` [EXISTING_D] 既有符号：（无）；候选新增符号：lenormand_approval_binding_schema.
- `tests/sprint48/lenormand/test_b_private_contract.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_private_contract_controls.

字段、状态与失败：system/query_hash/snapshot_id/release_id/release_sha256/contract_version/lexeme_profile；item的candidate/hash/review/user_approval绑定；错误非public第五码

生产者 → 消费者：受信PG -> internal result -> LN；public单向剥离

权限：IR-B-LN-01/02先接受；客户端不能自报approved

迁移：本任务无；SQL在T03。schema只允许这两份预期变化，导出额外改动须归因

回滚：回退可选载体与schema但保持核心关闭

CI: public不泄漏、系统schema隔离、伪绑定不准入

主人裁定：推荐扩展原合同不建LN审批表；未接受不写共享文件

验收：AC-B-06, AC-B-07

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_private_contract.py -m 'not integration and not mutation'`

## B-LN-T03 PG私有检索、批准链与撤回

需求：B-LN-R04, B-LN-R05, B-LN-R06, B-LN-R13

主人：S04 DB/权限主人；依赖：B-LN-T02

新增内部 EvidenceRepository，通过最小函数join既有release/items/candidate/review/user_approvals，保留八段filter。快照存在性与空项分开。复核pin后撤回；需要立即停用入口时操作既有SUPERSEDED并写审计。

### 精确 write-set

- `src/xiaoxingchen_core/retrieval/postgres_repository.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：PostgresEvidenceRepository, retrieve, revalidate_bound_snapshot.
- `alembic/versions/20260922_0010_lenormand_private_consumption.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：upgrade, downgrade, lenormand_projection.read_bound_evidence, lenormand_projection.supersede_bound_release.
- `tests/sprint48/lenormand/test_b_postgres_consumption.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_postgres_consumption_controls.

字段、状态与失败：projection_id就是release_id；同事务header/item/approval/hash完整；pin幂等非持续有效证明；身份错误拒绝

生产者 → 消费者：既有来源治理/发布 -> 受限SQL函数 -> internal repository -> LN

权限：另批临时PG17授权；MCP账户不得读raw/governance或另一system；不存DSN

迁移：新增迁移；0010以当前0009为父仅预留，实施HEAD有冲突先由S04重分配并更新写集，不改历史迁移

回滚：先关消费者撤新函数execute；不复活旧release、不删批准/交付记录；downgrade仅撤本次函数面

CI: 真实PG角色/过滤/并发撤回测试，缺环境BLOCKED_NOT_RUN，synthetic不得替代PASS

主人裁定：IR-B-LN-02冻结最小ACL/锁顺序；建议消费与交付提交重验同事务

验收：AC-B-08, AC-B-09, AC-B-10, AC-B-11, AC-B-12

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_postgres_consumption.py -m integration`

## B-LN-T04 获准目录与方法内容解码

需求：B-LN-R02, B-LN-R04, B-LN-R05, B-LN-R11

主人：S03来源/LN；资料批准仅爸爸；依赖：B-LN-T02

用既有CandidateItem.content存严格ln-catalog-v1/ln-method-v1规范JSON；解析不授予权利。36稳定身份，单值别名；方法含kind/arity/order/条件/反例。没有原书不补义、不伪AUTHOR_TEXT。

### 精确 write-set

- `src/xiaoxingchen_core/conversion/lenormand_payloads.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：LenormandCatalogPayload, LenormandMethodPayload, decode_lenormand_payload.
- `src/xiaoxingchen_core/lenormand_runtime/contracts.py` [EXISTING_D] 既有符号：LenormandRuntimeRequest；候选新增符号：ResolvedDeckCatalog, resolve_authorized_catalog.
- `schemas/v1/lenormand-catalog-content.schema.json` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：ln_catalog_v1.
- `schemas/v1/lenormand-method-content.schema.json` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：ln_method_v1.
- `tests/sprint48/lenormand/test_b_source_payloads.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_source_payloads_controls.

字段、状态与失败：目录/方法版本、系统、唯一卡/别名、顺序/适用范围；绑定T02，synthetic不进生产；缺词表保留review不改GLOBAL

生产者 → 消费者：原始受权材料 -> 既有conversion/review/publish -> decoder -> LN

权限：schema另批实施；原书读取/规范化/批准需新授权，本轮不挖掘

迁移：无新权威表，复用content/hash/span/approval；不增来源层

回滚：停对应decoder消费，保留源/候选/审计；不得格式错退成UNBOUND绕过

CI: 目录36唯一/别名冲突/hash/源版本/synthetic生产拒绝；语义独立验收

主人裁定：SG-01/02/03原件权利/目录/具体规则待批准；格式技术推荐

验收：AC-B-13, AC-B-14, AC-B-15

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_source_payloads.py -m 'not integration and not mutation'`

## B-LN-T05 二次收窄、支持图与生成前门

需求：B-LN-R04, B-LN-R05, B-LN-R06, B-LN-R11

主人：LN消费主人；依赖：B-LN-T01, B-LN-T02, B-LN-T04

吸收L角色/scope修复，替换unbound仍开门的旧预期。显式关系集合；core/method分查，GLOBAL method无cards不误删。允许批准规则+多条成员证据，禁止单牌词并集或一个邻接撑整组。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/evidence.py` [EXISTING_D] 既有符号：LenormandEvidencePort, admit_relation_evidence, CoreEvidenceGate, gate_from_admissions, guarded_generate；候选新增符号：ClaimSupport, validate_consumption_binding, admit_method_support, require_complete_core_support.
- `src/xiaoxingchen_core/lenormand_runtime/runtime.py` [EXISTING_D] 既有符号：LenormandRuntime, PreparedLenormandReading, port_retriever；候选新增符号：prepare_authorized.
- `src/xiaoxingchen_core/lenormand_runtime/relations.py` [EXISTING_D] 既有符号：（无）；候选新增符号：validate_method_application, require_relation_interpretation_authority.
- `src/xiaoxingchen_core/lenormand_runtime/__init__.py` [EXISTING_D] 既有符号：（无）；候选新增符号：reviewed_public_exports.
- `tests/sprint48/lenormand/test_ds_lenormand_admission_hardening.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：rebound_candidate_tests_without_unbound_green.
- `tests/sprint48/lenormand/test_b_authorized_admission.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_authorized_admission_controls.

字段、状态与失败：UNBOUND不开核心；完整目录/snapshot/release/审批、明确policy、方法/成员/方向/冲突支持；主张依赖图不是新审批库

生产者 → 消费者：绑定query/result + 目录/方法 -> ClaimSupport -> core gate -> 受控调用者

权限：不签运行权、不批准来源；生产只接受受信端口

迁移：无；依赖T02/03读取合同

回滚：关闭authorized prepare只留结构，不能恢复简化fail-open门

CI: 正反模型计数、method无cards、scope未知、截断、多证据、双作者不过挡

主人裁定：IR-B-LN-03方法profile；OD-F-01 / OD-F-04具体Matthews-only范围仍须产品批准

验收：AC-B-16, AC-B-17, AC-B-18, AC-B-19, AC-B-20, AC-B-21, AC-B-22

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_authorized_admission.py -m 'not integration and not mutation'`

## B-LN-T06 公共输出、防泄漏与不过挡

需求：B-LN-R07, B-LN-R08, B-LN-R11

主人：LN输出 + S04公共投影主人；依赖：B-LN-T02, B-LN-T05

选择性移植P相对L输出增量，补完整身份清单与短ID正常词对照，保留StrictModel/禁词典。生成前与render后门分别验收，字段正确不等于语义正确。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/output.py` [EXISTING_D] 既有符号：LenormandJudgment, LenormandOutputPort, assert_no_per_card_glossary；候选新增符号：collect_private_tokens, assert_no_internal_identifiers, project_reviewed_judgment.
- `src/xiaoxingchen_core/lenormand_runtime/runtime.py` [EXISTING_D] 既有符号：LenormandRuntime；候选新增符号：complete_internal_identifier_inventory.
- `tests/sprint48/lenormand/test_ds_integration_output_leak_hardening.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：reviewed_P_output_leak_regressions.
- `tests/sprint48/lenormand/test_b_public_output.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_public_output_controls.

字段、状态与失败：candidate/approval/snapshot/query/relation/span身份；public只判断/条件/路径/阻力/验证/边界/退出；错则受控重生成或停，不字符串替换放行

生产者 → 消费者：审查主张+私有支持 -> public projector -> demo/交付

权限：不增public来源权限、不回显内部错误/ID

迁移：无

回滚：关闭输出路径，保留最小公共面与核心门，不恢复泄漏版

CI: helper/finalrender、中文短ID、大小写、嵌hash、嵌套键值、用户事实支持

主人裁定：技术推荐；公开来源依原许可，不向爸爸询问正则细节

验收：AC-B-23, AC-B-24, AC-B-25, AC-B-26

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_public_output.py -m 'not integration and not mutation'`

## B-LN-T07 体系隔离由身份而非普通子串决定

需求：B-LN-R05, B-LN-R08, B-LN-R11

主人：LN来源边界主人；依赖：B-LN-T02

分离registry键/system/layer与展示文字；修复PLACE/GD普通词误挡但不取消体系门。未解析来源保留review不入核心。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/cross_system.py` [EXISTING_D] 既有符号：assert_no_forbidden_provenance, assert_cross_system_clean；候选新增符号：validate_provenance_identity.
- `tests/sprint48/lenormand/test_b_cross_system.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_cross_system_controls.

字段、状态与失败：typed身份精确校验；未知来源与禁用体系分开；不能自然词contains判权威

生产者 → 消费者：来源注册身份 -> cross_system -> admission

权限：不增allowlist、不接Tarot/RWS/GD兜底

迁移：无

回滚：停未解析身份消费，不恢复自然文本黑名单作为唯一判据

CI: workplace/replacement好例与伪装Tarot坏例成对

主人裁定：工程修复推荐，不需新增产品裁定

验收：AC-B-27, AC-B-28

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_cross_system.py -m 'not integration and not mutation'`

## B-LN-T08 LN编排、现实核对与独立审查

需求：B-LN-R06, B-LN-R07, B-LN-R08, B-LN-R13

主人：S02编排 + S03 LN + S04运行权威；依赖：B-LN-T03, B-LN-T05, B-LN-T06, B-LN-T07

IR-B-LN-05先冻结system-specific operation载体再接线。复用安全/隔离/预算/时钟/撤权/工件，不调用TarotStageExecutor或继承R1-R4职责。研究默认关闭，工件与交付回读明确。默认factory不启用。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/orchestration.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：LenormandOrchestrator, prepare, compose, review, deliver.
- `src/xiaoxingchen_core/demo/lenormand_port.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：LenormandDemoRuntimePort.
- `tests/sprint48/lenormand/test_b_orchestration.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_orchestration_controls.

字段、状态与失败：确认事实、当次身份/authority、支持图、research状态、review结论、交付digest；本地操作不自封共享阶段

生产者 → 消费者：DemoRuntimePort -> LN编排 -> 受控模型/研究/clock/store适配 -> public交付

权限：阻塞于共享operation权威合同；不新建issuer/state/approval表；运行另批

迁移：本任务不改reading状态机；若共享合同需扩展由S02/S04另给精确写集，完成前不得接真库

回滚：移除适配注入回到UnavailableRuntimePort；不复活终态

CI: 零调用前门、过期/撤回/换人、研究未发生不伪结果、不套塔罗、交付回读

主人裁定：IR-B-LN-05必要共享缺口；不以本任务宣布S03整体完成

验收：AC-B-29, AC-B-30, AC-B-31, AC-B-32

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_orchestration.py -m 'not integration and not mutation'`

## B-LN-T09 五牌候选几何与中轴非独断

需求：B-LN-R09, B-LN-R11, B-LN-R12

主人：LN五牌候选主人；依赖：B-LN-T01

选择性引入L候选模块/测试；固定五标签、四邻接，先去重再参与/非中轴覆盖；支持图审查与计数分开，仍默认不可达。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/layout_candidates.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：CandidateModePlan, assemble_candidate_relations, assert_pivot_is_not_sole_authority, validate_candidate_slots.
- `tests/sprint48/lenormand/test_ds_lenormand_layout_candidates.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：rebound_L_candidate_geometry_tests.
- `tests/sprint48/lenormand/test_b_five_candidate.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_five_candidate_controls.

字段、状态与失败：FIVE_CARD_LINE、5唯一槽/卡、pivot2、四邻接、两翼支持；validator通过不改变关闭

生产者 → 消费者：synthetic用户几何 -> 候选关系 -> 审计，不到生产generator

权限：另批候选代码/测试；无书本/模式运行授权

迁移：无

回滚：撤候选增量或保持不可达；不改生产数据

CI: 缺槽/重复/越界/缺邻接、中心独断、重复充计数、两翼反证

主人裁定：本站标签依本任务设计；真语义/运行OD-F-02 / OD-F-03 / OD-F-05另批

验收：AC-B-33, AC-B-34, AC-B-35

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_five_candidate.py -m 'not integration and not mutation'`

## B-LN-T10 九牌候选与对角辅助边界

需求：B-LN-R10, B-LN-R11, B-LN-R12

主人：LN九牌候选主人；依赖：B-LN-T09

复用T09新增候选模块，固定3x3中心/周围集合/横纵；用坐标规则识别正交边、一步对角、跨行；缺对角只去辅助不关闭独立主干。

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/layout_candidates.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：is_orthogonal_edge, validate_candidate_relation_geometry, assert_diagonal_is_support_only, candidate_module_is_imported_by_consumer.
- `tests/sprint48/lenormand/test_b_nine_candidate.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_nine_candidate_controls.

字段、状态与失败：NINE_CARD_GRID_3X3、center4、ring无向、3row3column、diagonal辅助；priority非语义权重

生产者 → 消费者：规范坐标 -> 候选关系 -> 结构/支持审计

权限：另批工程测试，无语义/运行批准

迁移：无

回滚：只回退新增候选分支，不改三牌/DS07原账本

CI: 12边、一步对角/跨行/远角、ring不定方向、无对角不过挡、中心非独断

主人裁定：对角最多辅助且需要具体方法授权，不建议提高职责

验收：AC-B-36, AC-B-37, AC-B-38, AC-B-39

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_nine_candidate.py -m 'not integration and not mutation'`

## B-LN-T11 未来五九牌分模式开放（当前禁止）

需求：B-LN-R09, B-LN-R10, B-LN-R13

主人：爸爸明确授权范围；S02/S03/S04实施；依赖：B-LN-T08

只有目录/方法/PG/运行权/语义和负例验收全满足才按单模式开放。五九牌独立，九牌对角可单独仍关。候选flag/import不是授权。 Conditional dependencies: FIVE_CARD_LINE requires T09; NINE_CARD_GRID_3X3 requires T10. Neither mode waits for approval of the other mode.

### 精确 write-set

- `src/xiaoxingchen_core/lenormand_runtime/layout.py` [EXISTING_D] 既有符号：ModeSpec, assert_mode_open；候选新增符号：authorized_mode_release_mapping.
- `src/xiaoxingchen_core/demo/catalog.py` [EXISTING_D] 既有符号：（无）；候选新增符号：reviewed_ln_five_nine_intake_records.
- `src/xiaoxingchen_core/demo/cli.py` [EXISTING_D] 既有符号：（无）；候选新增符号：explicit_authorized_ln_factory_injection.
- `tests/sprint48/lenormand/test_b_mode_activation.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_mode_activation_controls.

字段、状态与失败：模式slug/layout_version/资料release/批准/runtime grant分别绑定；缺必要前提保持关，不能减牌

生产者 → 消费者：具体产品/资料授权+已验收实现 -> 服务端策略 -> 显式入口

权限：本轮没有；必须新授权，技术任务不能自动启用

迁移：不新建来源权威；共享运行DB先由S02/S04完成

回滚：关闭相关模式与新运行、撤当次runtime权；不删除历史交付

CI: 默认都拒绝、单模式不连开、撤回/故障/原文语义验收

主人裁定：OD-F-02 / OD-F-03 / OD-F-05分别决定5/9及对角范围，当前未决/关闭

验收：AC-B-40, AC-B-41

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_mode_activation.py -m 'not integration and not mutation'`

## B-LN-T12 回归CI与可复核交付

需求：B-LN-R01, B-LN-R12, B-LN-R13, B-LN-R14

主人：Codex/CI主人；依赖：B-LN-T00, B-LN-T05, B-LN-T06, B-LN-T07, B-LN-T09, B-LN-T10

建立精确写集、源身份、schema差异、synthetic与DB/源语义分轨结果。默认CI不联网/真实provider；每项记真实结果或NOT_RUN，封存manifest/hash。

### 精确 write-set

- `.github/workflows/ci.yml` [EXISTING_D] 既有符号：（无）；候选新增符号：lenormand_design_regression_job.
- `docs/design/lenormand/ACCEPTANCE_RECEIPT.md` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：observed_command_results_with_scope.
- `tests/sprint48/lenormand/test_b_ci_boundaries.py` [PROPOSED_NEW] 既有符号：（无）；候选新增符号：paired_ci_boundaries_controls.

字段、状态与失败：scope/status/baseline/command/result；缺依赖精准作用面；无测试不填PASS

生产者 → 消费者：实际代码diff/测试/授权 -> CI证据 -> reviewer

权限：CI改动另批；不连生产DB/provider、不读禁挖资料

迁移：无

回滚：禁新job保留旧安全检查与历史证据

CI: 正反/过挡有真实结果或明确阻塞；无越界/secret/输入变更

主人裁定：技术推荐；远端CI本轮不刷新

验收：AC-B-42, AC-B-43, AC-B-44

NOT_RUN: `python -m pytest -q tests/sprint48/lenormand/test_b_ci_boundaries.py -m 'not integration and not mutation'`

