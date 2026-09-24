# B 雷诺曼专项 SPEC

**DESIGN_CANDIDATE_NOT_AUTHORIZED · 离线设计完成不等于资料批准、代码实施、S03 完成或运行授权。**

依据固定 M/D/L/P 字节，定位见 CALL_CHAIN.md、BASELINE_COMPARISON.md。需求编号 B-LN-R01–R14 是本专项局部编号，不覆盖 A 需求账或共享需求权威。任务、验收分别见 TASKS.md / TASKS.json、ACCEPTANCE.md / ACCEPTANCE.json。

## 1. 需求与完成边界

|需求|合同|
|---|---|
|B-LN-R01|四面基线分离、输入身份复核、历史声明降级、不改 A|
|B-LN-R02|用户实际给牌，36 牌表身份、模式/slug、抽牌顺序/显示位置准确；不抽牌、不逆位|
|B-LN-R03|三牌关系几何独立于牌义；来源缺失仍能验证结构|
|B-LN-R04|真实受权资料消费：release/snapshot/candidate/approval/内容身份全链、权限与撤回|
|B-LN-R05|两层检索：召回不等于组合语法；scope/role/purpose/方向与多证据收窄|
|B-LN-R06|生成前核心门与交付前复核；非空证据不等于整组充分|
|B-LN-R07|现实条件、可行路径、验证/退出；无网络不冒充研究，无证据不编牌义|
|B-LN-R08|public/private 分界、防逐牌词典、防身份泄漏与合理语言不过挡|
|B-LN-R09|五牌本站位置设计，第三阻力/中轴非独断，四组邻接，默认关闭|
|B-LN-R10|九牌中心/周围/横纵；对角仅辅助；默认关闭|
|B-LN-R11|缺条件/上下文/互补/重复/真冲突分流，不一刀切|
|B-LN-R12|文件/符号精确实施切片、先红后绿、回滚、CI，测试均 NOT_RUN|
|B-LN-R13|共享接口送 S02/S03/S04 主人吸收，不另造同义批准权威|
|B-LN-R14|累计 B 检查点封存、可恢复、不续跑|

本轮可完成：工程合同、静态证据与任务/用例设计。不能由本包完成：原书语义证明、36 张真实获准牌表、真实 user_approval 值、生产 DB 事务/权限效果、provider 输出质量、用户运行授权。所有后者保留精确缺口。

## 2. 最小路径与能力分层

建议保留三层互不冒充的能力：

- **STRUCTURE_ONLY**：用户给定合法形状的三牌，得到位置事实和关系 ID。不知道获准牌表时标为 UNBOUND，不能宣布未知牌名合法或非法，也不能调用牌义模型。
- **AUTHORIZED_PREPARED**（PROPOSED_NEW 内部派生态）：只有服务端验证了牌表、原始投影身份、方法/核心证据和本次覆盖后才成立。不是持久化批准状态，更不是客户端布尔字段。
- **DELIVERABLE**（PROPOSED_NEW 内部派生态）：运行授权仍有效，必要资料未撤回，生成与审查完成，用户事实/边界与输出检查通过，受控交付回读成功。不能直接映射现有 R4_SEALED；共享状态由 S02/S04 决定。

推荐调用序列（全部候选）：parse → canonicalize_layout → resolve_catalog → bind_snapshot → retrieve_core_and_method → admit_claim_support → require_generation_authority → compose → review → revalidate_authority_and_sources → public_project → deliver/readback。任何副作用前须由当次 runtime grant 决定；资料准入与运行授权是两个不同必要条件。

### 三牌示例（纯 synthetic，无真实牌义）

用户给出 `ln-fixture-a / ln-fixture-b / ln-fixture-c`，说明“我有两周准备窗口，预算未确定”。这些 ref 仅存在工程 fixture，不是生产牌名，也不能进入生产投影。几何结果为左至右 A、B、C；邻接 A→B、B→C；全线 A→B→C；全成员集 {A,B,C}。

假设受信 fixture 提供一条明确批准的组合方法及各成员证据，可演示主张 `SYNTHETIC_CLAIM_1` 的支持链，不给 A/B/C 编造书中意义。运行说明必须区分用户事实“两周”、未知“预算”、由证据支持的条件性判断，以及现实待验证项。通过这种 fixture 只能证明身份与形状、关闭行为，不能证明主张牌义正确或审批真实。

## 3. 用户事实、牌表与布局

### 3.1 输入不变项

复用 L:lenormand_runtime/contracts.py 的严格输入合同。cards 只来自用户，禁止抽牌器、填缺牌、去重后继续、把九牌截成三牌、借 Tarot card/orientation 类型。topic 是待讨论文本，不是资料或批准。orientation 键即使 null/空值也拒绝；显示层的旋转效果不能变成逆位含义。

保留原始 cards、draw_order、display_positions；解析失败不改写原始事实。用户明确的位置排列优先作为事实，但不得从任意 slot 名猜空间关系。三牌候选约定规范槽 `left/center/right`；输入适配器须明确给出 ref→slot 一一对应，布局组装按规范槽而非任意数组顺序。无位置输入则采用用户声明的左至右顺序并回显确认；缺少可确定顺序时只请求缺失事实，不偷偷排序。

`spread_mode=THREE_CARD_LINE` 与已有 demo slug `ln-three` 一对一绑定；具体 enum 字面以实际 contracts.py 为准，不另造与它并行的值集。映射存于既有 layout registry 的版本化描述中。不得以 `spread=None` 跳过已知模式的 scope。五/九牌未来 slug 候选 `ln-five-site-v1`、`ln-nine-site-v1` 只在设计/fixture 中保留，不注册为开放入口。

### 3.2 牌表权威

已有 `LenormandDeckCatalog.contains` 是能力形状，不是审批证明。推荐保留协议、扩展服务端解析方法：牌表内容必须来自既有来源生命周期所批准、发布、激活的 LN 方法/目录资料；其来源层、版本、原文定位和权限与实际材料一致，不把本站别名表伪标为 Matthews/Rana。

最小规范目录内容候选为严格 `ln-catalog-v1` JSON（作为既有 CandidateItem.content 的规范化内容，不新建“批准牌表”表）：system、36 个稳定 card_ref、源中名称及原文定位；可选别名有语言/版本和单值映射。仅 `content` 结构化不授予权限，仍由 candidate hash、user_approval、review_decision、release 决定。目录内恰好 36 个唯一身份、无冲突别名；牌义和别名不混存为模型词典。若现有导入 profile 不能表达此文档，先补 LN 特定 profile/解码合同，不改变来源层闭集。

服务端 `ResolvedDeckCatalog`（PROPOSED_NEW，本地只读结果）保存 catalog 所依赖的真实 item/release/snapshot/content hash；本身不可批准或发布。测试 StaticDeckCatalog 永远 synthetic，不能因非 None 变成生产 BOUND。正式卡表不存在时：允许结构分析，核心门关闭；正式目录存在而某 ref 不在表中时：精准返回输入缺陷，不退回“无目录”以绕过成员检查。仅当整表身份不能验证时关闭当次核心语义，不能把无关来源缺一条扩散成服务全局停机。

## 4. 授权资料接入、消费与撤回

### 4.1 复用生命周期，禁止旁路

原始材料接入仍走 RAW→EXTRACTED→NORMALIZED→CANDIDATE→REVIEW_REQUIRED，再由真实用户身份选择 HOLD / REJECTED / APPROVED_PROJECTION，发布→INDEXED→ACTIVE；旧内容按合同 SUPERSEDED。不从本轮设计或历史作者“已测 153/164”得到任何批准。仅具文本权利不等于获准运行，文件收齐不等于每条证据获准。

每条候选沿用 SourceDocument / SourceVersion / SourceSpan / MappingProfile / CandidateItem：source system/layer、原始内容 hash、版次/语言/翻译、span 定位、purpose、四 scope、usage boundary、synthetic 标志和源映射身份。规范化不补写原文没有的规则。重复项合并索引但保留各原文定位；互补项保留分工；真冲突保留分歧和阻断相关主张，不以多数票或模型常识裁决。

D 的 SQL publish_candidate 已校验发布角色/grant、候选状态/system、非 synthetic、runtime_eligible，并关联 USER review 与 user_approval 的 candidate hash。这些是可复用真权威链，不再创建 `lenormand_approvals` 或 `approved=true`。

### 4.2 私有消费字段（PROPOSED_NEW 合同扩展）

沿用 EvidenceRepository.retrieve / RetrievalResult / LenormandEvidenceItem；新增字段只表达现有 DB 事实的读取与绑定，不能成为独立批准来源。

|载体|必须保留/派生字段|权威及用途|
|---|---|---|
|受信查询上下文|system=LENORMAND、purpose、规范 spread、实际 stage/domain/scenario、query_hash、contract_version、lexeme_profile|服务端由已确认输入与模式生成；不接受前端 expected_* 作为凭证|
|快照|snapshot_id、projection_id=release_id、release_sha256、release.status、查询契约版本|从同一事务中的 projection_releases 读取；全部匹配而非 id 二选一|
|证据项|已有 item_id、content/content_sha256、source_layer、lifecycle、purpose、四 scope、usage_boundary、cards、provenance_ref、source_span_ref|从真实 projection_items 及受控视图读；校验内容 hash 和系统隔离|
|批准链扩展|candidate_id、candidate_sha256、review_decision_id、user_approval_id 以及实际匹配结论的证据定位|join 既有 candidate/review/user_approvals；不向模型/用户暴露。不要求把所有敏感表原始列开放给读取角色|
|当次消费绑定|reading/request 身份、选中 item 集、catalog item、method item 集、组合支持映射、内容与快照 digest|复用 reading/source snapshot 与工件 digest 能力；B 仅提扩展，不签发 authority|

推荐新增 `retrieval/postgres_repository.py::PostgresEvidenceRepository`（PROPOSED_NEW）实现既有内部接口，通过受控的 LN private view/function 返回上述最小读模型。不能使用只有 mcp_readonly 权限的账户去读 raw vault / 全部治理表；由 DB owner 决定最小授权函数及独占角色或现有 reading controller 的受限函数。MCP public 视图保持去标识，不增泄漏列。密码、DSN、权限授予和数据库执行不在本任务内。

`projection_id` 在现有 active view 中就是 release_id，不再设一个同义 UUID。candidate 内容 hash 与 release 聚合 hash不同，不混用。通过一个同事务有效性读取形成绑定，再在实际调用/交付处复核；只在 Python 缓存中相信 ACTIVE 不够。响应的 snapshot/query hash 必须与请求一致。空快照有独立存在性判断，不用“没有行”推断 NO_SNAPSHOT。

### 4.3 撤回与并发

区分两个动作：资料撤回/替换通过既有生命周期与发布治理处理；当次运行撤权走 reading authority/TTL，不相互替代。已索引或激活的原始内容不可原地修改后保留旧批准；内容、scope、用途或目录改变都要新候选/新批准/新发布。

现有 `reading.pin_source_snapshot` 是一次 pin 且同 ID 幂等；现有同 ID 的提前返回不能被当作持续 ACTIVE 的证明。消费端必须另查当前有效性，避免 pin 之后资料 SUPERSEDED 仍继续生成。推荐在将有依赖的语义调用开始前和交付提交前复核 snapshot 与依赖项状态；实际原子性边界、锁顺序由 S04 用事务实现。旧批准本身不可凭空增设 revoke 字段：先用现有发布状态/停用机制；若缺少受限的立即停用入口，由 S04 新增函数操作既有状态并写审计，不新建批准台账。

撤回影响相关资料依赖的未交付读牌；不自动切换别的快照继续、不复活旧状态、不删除历史已交付记录。只缺 Rana 可选补充时移除该补充并重做涉及它的判断/审查；若其主张已经成为必要支持，不能静默删掉来源仍输出同一句。Matthews 必需组合规则或目录撤回，停止当次核心。将受影响集合定义为实际依赖项，不以任何来源变更全局停机。

## 5. 检索、scope 与组合语法

### 5.1 召回与准入分开

保留 system→spread→stage/purpose→card/orientation→domain/scenario→lifecycle→source_layer→full_text 的冻结过滤次序；LN 没有 orientation 值。SQL 的 cards 交叠仅召回。由 LN 准入再次核验真实绑定、角色、用途、scope、关系类型、方向和主张支持。max_items/truncated 的处理必须可见：缺必要方法或覆盖时不能因截断“恰好有一个 core”开门；可做受限第二次精确查询，达到预算仍不足则停止该主张，不无限重试。

核心与方法独立查询：core 查卡/主张证据，method 查明确的组合规则。全局方法可能没有 cards，不能被卡交叠或“单条必须覆盖所有成员”误删；它只授权组合方式，不能自己建立所有牌的具体含义。方法查询必须按已批准方法身份、purpose/scope 读取，不扫整本书作为检索旁路。

`allowed_relation_kinds=None` 不得表示生产无限开放。对三牌，服务端模式表给出明确 `{ORDERED_LINE_SEQUENCE, ORDERED_ADJACENCY, FULL_MEMBER_SET}` 候选集合；类型合法仍不等于该类型的语义已获准。未知扩展关系保留诊断且不参与核心推理，不关闭其他已验证关系；结构损坏/矛盾 ID 单独拒绝。参数 None 可用于离线结构预览，但在受权消费处必须解析成显式已审查模式策略。

### 5.2 Scope 未知值

系统、来源身份、快照完整性不允许模糊。用途、已知 spread 与已知上下文必须准确匹配。对用户没有提供的 domain/scenario/stage，只接纳明确 GLOBAL 的适用项，或暂停仅依赖该未知条件的主张并请求对应事实；不能把 requested=None 当成所有 scoped 项都符合，也不能要求每次补齐所有上下文才允许 GLOBAL 项工作。LN 普通证据的 NOT_STATED 并非当前合同支持：现代码只对 Mentor scenario 特许，不能复制旧报告的泛化结论。新增 scoped 值未在词表时先做合同/源映射核对，不能把自然语言同义表达直接判成语义失败。

### 5.3 三牌最小组合充分性

推荐最小支持方案不是 36×35×34 预编句库，也不是单牌三段词典。准入保存 `claim → relation instances → approved method items → member/core evidence items → scope/conditions` 的可回溯支持图（PROPOSED_NEW 内部派生结构，不是新权威数据库）。

整组语义至少需要：用户三成员和顺序完整；一条适用于三牌线性组合的获准方法；三成员各有获准的适用核心支持；主线和两个邻接的作用都被明确处理。允许两种支持方式：源中直接给定整组/有向组合，或者源中批准组合规则 + 覆盖各成员的多条获准证据。不得把三个单牌关键词的集合并集当“语法已获准”。有向 A→B 不等于 B→A，方法对顺序的许可必须可追溯。

无需每条证据同时出自 Matthews 与 Rana。Matthews 作为结构/组合主干，Rana 作为日常信号补充；补充可以为空且明确不做相关主张。若缺 Matthews 主干，不把 Rana 自动提升为结构主干，除非爸爸日后对具体来源与规则另行裁定。主题、现实条件、下一步验证由主张支持图约束，不由作者名数量计票。

整组三牌核心不足时，输出诚实缺口/可保留的结构事实，不生成整组牌义。某个独立可选主张不足时仅弃用该主张，不关闭已经完整成立的核心。真冲突阻断冲突主张；当它影响整组核心的必要前提，才关闭当次核心生成。

## 6. 核心门、现实约束与审查

`CoreEvidenceGate.is_open` 的候选替代条件应为全部必要事实成立：输入/布局完整、获准目录匹配、快照完整且可用、批准链一致、explicit relation policy、必要方法与成员/关系覆盖、无未裁决核心冲突、运行 authority 有效。实现中将证据门与运行 authority 的最终授权检查组合于调用者，避免底层纯几何库承担发权职责。

生产 `guarded_generate` 必须由真实 LN 编排调用，spy 验收要求任何必要门失败时模型/研究/DB 写调用计数为零。render 对已有正文的检查另行保留；不能声称它保证生成前零调用。

现实表达最低包含：主判断的条件性边界；用户给出的客观约束和未知项；可行动路径；关键阻力/替代解释；可观察验证信号与退出条件。保留自然表达，不强制每个字段都有固定长度或出现指定词。`LenormandJudgment` 结构是承载，不是语义质量证明；可以没有适用的 path，但须诚实说明并保留验证/退出，而不能用空元组掩盖缺分析。

研究默认关闭。无联网权时只核对用户事实和已获准材料，明确未检索；真实失败、检索成功但无可靠方案、具有效回执的结果分开。外部研究只能核查现实条件，不能补书本牌义或升级来源批准。独立审查至少检查主张支持、跨系统污染、条件缺失、用户事实编造、权威变更及过度肯定；审查建议不等于用户资料批准。S02/S03 定义 LN 编排职责，S04 接受预算/TTL/工件/交付合同，不能调用 TarotStageExecutor 来凑闭环。

## 7. 失败与公开合同

保留现有四个 no-match：`NO_SNAPSHOT`、`NO_LAYER_MATCH`、`NO_APPROVED_EVIDENCE`、`DISABLED_PROVIDER_OFF`，不新增第五个 public code。来源完整性失败/非法输入/授权失效属于拒绝或错误，不冒充正常无匹配。

|情形|内部处理|用户面|
|---|---|---|
|请求快照不存在或不可用于当前消费|NO_SNAPSHOT；已 pin 后失效还须停止当次操作|资料目前不可用，不猜替代|
|快照存在、允许层无 ACTIVE 项|NO_LAYER_MATCH|必要来源未就绪；可选补充不影响独立完整核心|
|有来源但本次 scope/方法/覆盖无适用项|NO_APPROVED_EVIDENCE + 内部窄化原因|这次输入缺少获准支持，不生成牌义|
|网络/provider 未获准|DISABLED_PROVIDER_OFF，零研究回执|明确未进行联网研究|
|snapshot/hash/system/candidate/approval 绑定不一致|内部 INTEGRITY_REFUSAL（候选类别，不加入 public no-match）|有限安全错误，不回显 ID/SQL/原文|
|已知目录中的未知牌、重复或不完整布局|INPUT_REFUSAL，保留原始输入|指出需要用户修正的槽/输入，不替换牌|
|目录未绑定|STRUCTURE_ONLY；核心门闭|只能确认结构，未能核验牌表与牌义|
|运行 authority 过期/撤销|沿用现有停机语义，不重试签发|停止本次，需新明确授权|

PublicRetrievalResult 与最终判断不是同一对象。公共判断不携带 item_id、candidate_id、approval_id、snapshot、projection/release、span、provenance、内部 relation ID 或原始错误；允许公开来源须走既有被许可的 public_source_ref 与核验链，不能把私有检索 ID 当引用。

## 8. 输出与不过挡

只允许面向用户的判断字段；递归检查键和值、结构化主张中引用的真实内部身份，使用明确 token/编码边界而非普通子串全禁。L 与 P 的防泄漏差异见 OVERDESIGN_REVIEW.md。哈希、实际长不透明 ID、嵌入式身份和 case 变种应拦截；普通词 `intent` 不应因为内部 id=`in` 被禁。中文短 ID 与普通语言无法靠任意 regex 保证，优先避免把内部 ID 送进生成上下文，生成输出使用受控结构投影、引用映射和审查；需要确切表示真实短 ID 的文本则不公开该身份。

禁止逐牌词典是禁止“卡 ID 作键逐条牌义”替代关系主判断，不是禁止自然语言提到用户给的牌。替换/删掉泄漏字符串后不直接放行，必须重新生成受控输出或终止，避免产生无证据残句。没有泄漏也不证明推理正确。

## 9. 五/九牌与默认关闭

完整合同见 FIVE_NINE_CANDIDATE.md。本站位置语义与作者方法分列来源；结构参与度、priority、覆盖计数都不代表语义权重已证明。默认关闭必须同时在入口、模式策略、运行消费门保持；源码存在、import 成功、synthetic 用例通过、某个旗标改 true 都不能构成开放授权。

## 10. 兼容、迁移及落地顺序

先几何/过挡回归，再私有检索与绑定，再资料 profile/目录/组合方法，再生成和输出门，最后按 S02/S04 接线；五/九牌作为独立未来批次。现有 schema contract、OpenAPI/JSON schema 和 DB hash 输入若受字段影响，必须由合同主人同步生成并查 diff，不直接改历史迁移。

私有 join 与最小权限函数需要新迁移；内容目录/方法 JSON 可用既有 CandidateItem.content，不强求通用新表。新迁移编号必须基于实施时真正 HEAD 分配，B 仅给建议预留文件名，不能与其他主线争用。任何未获共享接口裁决的任务允许继续纯局部设计，但禁止擅自提交共享文件。所有实现命令在本包标 NOT_RUN。
