# B 过度设计与安全门审计

DESIGN_CANDIDATE_NOT_AUTHORIZED。当前发现基于固定源码和未应用 patch 的静态分析，不称生产漏洞复现，也不把历史作者测试计作本轮实跑。每个新增/加强硬门同时给有效正控和真正反例；详细测试见 ACCEPTANCE.json。

## 1. 先纠正旧结论，再设计

|旧/泛化说法|本轮字节结论|处理|
|---|---|---|
|LN 所有 scope 与 purpose 都不查|D 简化准入存在缺口；L 已新增显式 expected_* 与 purpose/role 二次收窄|不能再把已修分支当未修；剩余在默认 None、绑定传递、受信权威来源|
|任何补充条目都能开核心门|L 的 _may_establish_core 已检查 CORE_EVIDENCE、may_establish_core、runtime_eligible、purpose|保留此修复；新门补全目录、发布/批准和组合充分性|
|NOT_STATED 会让所有 LN scoped 证据变成 GLOBAL|domain/evidence 只特许 Mentor scenario，LN 普通证据构造并不支持该值|不引入无依据的 LN NOT_STATED 特判或全局停机|
|没有 LN slug|D demo/catalog 已有 ln-three，入口关闭|补 registry→slug 的权威映射，不造第二份同义 slug 表|
|本包能直接接真实 PostgreSQL|PG MCP 是 PublicRetrievalResult，LN private 准入要 RetrievalResult 与身份|补内部读模型，不从 public 内容反造批准|
|输出键/大小写/嵌入 hash 都已有保护|L helper 主要扫值；P output 另有键/值、casefold、嵌入 hash 修订|区分 L 与 P；P 未应用且没有真正接通生产|
|153/164 tests 是本轮通过|只是历史报告；本轮产品测试 0 次|所有用例/命令 NOT_RUN|

## 2. 成对审计矩阵

|ID / 硬门|应保留的有效好例|必须拦的坏例|推荐范围与原因|
|---|---|---|---|
|OD-01 资料身份|同一获准 snapshot/release/items，内容与审批链一致|同名资料但 hash/版本/候选不同，或客户端 approved=true|身份完整性硬拒绝，不接受语义近似替代 hash|
|OD-02 牌表绑定|暂无目录时仍可核验三槽结构；获准目录里的牌可进入后续门|提供任意 StaticDeckCatalog 就自称获准；已知目录中的未知牌|UNBOUND 只关闭核心语义；不把未取得目录等同非法牌|
|OD-03 明确策略|三牌注册的 ORDERED_LINE_SEQUENCE/ORDERED_ADJACENCY/FULL_MEMBER_SET 有对应方法|allowed_relation_kinds=None 让任意新类型参与核心|生产必须解析显式模式策略；离线结构可以保留未知候选，不全局关闭|
|OD-04 scope|用户未给 domain，但 GLOBAL 资料确实适用|SCOPED=某职业场景，因 requested=None 直接吞入|保留 GLOBAL 路径，仅需要该条件的主张暂停；不强迫所有用户补完所有字段|
|OD-05 词表缺值|原文明确条件，新同义短语尚未注册，可保留候选供映射审查|把条件丢掉或改 GLOBAL 以绕过 schema|缺词表是映射缺口，不是语义错误；批准链不放松|
|OD-06 多证据|获准组合规则 + 三成员分别获准证据，有方向/适用条件|只有三个关键词，集合并集冒充组合语法|允许有证据的组合，拒无方法的拼接；不要求每条 item 都覆盖全部成员|
|OD-07 来源职责|Matthews 主干完整，Rana 可选补充无匹配，主张不依赖它|Rana 信号被提升成缺失的 Matthews 结构规则|按角色隔离；是否开放具体 Matthews-only 片段属产品/资料范围决策，工程不强制每条双作者|
|OD-08 重复/互补|完全重复去重仍保留多出处；互补支持不同条件/成员|真实冲突按 item_order 取第一或模型投票|去重不是删来源；真冲突只阻断相关主张及其依赖|
|OD-09 全局关闭|九牌对角未获准而非对角主干完整；无 Rana 可选层|必要目录/核心方法撤回仍继续输出|以实际依赖图确定作用面，不因无关资料缺一条全服务停机|
|OD-10 跨系统|合法 LN 身份资料的说明文字出现 workplace/replacement 等普通词|typed SourceLayer=WAITE_RWS / system=TAROT，被伪贴自然标签洗白|按真实 source identity/layer 隔离，不用任意自然文字 contains('PLACE') 判体系|
|OD-11 内部短 ID|内部 id=in 时普通词 intent、within 或中文正常叙述|确实把实际内部 ID 当身份向用户展示|结构化引用/身份集合优先；文本扫描尽量明确边界，不能普通子串全禁|
|OD-12 键值泄漏|合法 allowlist 判断结构，无实际身份|键或值含实际 projection/snapshot/candidate/approval ID，大小写/嵌入编码变种|从私有上下文收集完整身份；键和值递归扫描；最终 StrictModel 仍保留|
|OD-13 逐牌词典|自然句提到用户给牌并说明组合条件|{card_ref: 逐牌牌义} 或与 main_judgment 混合伪装|拒词典形状，不禁自然提牌；不把格式合格当组合逻辑合格|
|OD-14 用户事实|“预算未知，需确认”，不要求出现特定关键词|把原书例中人物/经历断言为用户历史，或自由文本编造条件|证据/用户事实支持图与审查；仅禁 profile/memory 键不足|
|OD-15 布局不独断|第三张参与两翼联合支持；外围可反证中心初判|重复关系充计数；中心一条证据决定全局|先去重/几何验证，再语义支持检查；不生造百分比权重|
|OD-16 对角范围|真实正交边 (1,4)；获准对角仅辅助|对角一步 (0,4) 或跨行 (2,3) 标正交边|坐标通用规则替代有限黑名单；缺对角不关闭合法主干|
|OD-17 入口可达性|候选仅设计/测试导入、runtime registry 关闭|换一种 import 写法或旗标令未授权模式可达|全 src/entrypoint 检查 + 真实入口拒绝用例；不把局部 AST 扫描当绝对证明|
|OD-18 研究与安全|普通情感/关系问题符合既有安全边界；无联网时如实未研究|仅因情感词拒绝正常请求，或联网未发生却声称“查无可靠方案”|沿用真实议题安全门，分清 provider-off 与研究失败，不把可选联网做核心前置硬依赖|

## 3. 字面扫描的具体根因

L:cross_system.py 的 FORBIDDEN_PROVENANCE_MARKERS 包含 PLACE、GD 等，`assert_no_forbidden_provenance` 将任意 tag 规范化后做 contains。若把自然文本误当身份 tag，workplace/replacement 会含 PLACE；两字母标记也容易碰撞。runtime.prepare 当前主要传 cards，未证明这些自然文本实际经该 helper 进入生产，所以本轮定为“辅助函数的过挡风险”，不是已触发的线上故障。

推荐接口把来源 system/layer/registry key 与展示文本分开。registry key 精确解析；未知 key 进入来源未解析状态，不按自然句猜作者。缺来源身份时仍不可用于核心，但保留文本作为未准入候选供后续处理。不要通过删除所有禁用体系检查来修正过挡。

L:output.py 的 `_iter_text_values` 不扫描字典键，`assert_no_internal_identifiers` 对传入实际 ID 做 case-sensitive 子串查找。P 的 `_iter_text_tokens` 加键，hash 正则去单词边界，needle 匹配使用 casefold/ASCII 词边界改善部分过挡。纯 alpha 的判断用 isalpha 而边界规则偏 ASCII，不能据此宣布中文短 ID 情形完备。P 不解决运行端没有传入 snapshot/query/approval 等身份的问题。

必须区分 helper 与最终 render：未知键常被 StrictModel 另行拒绝，所以“键扫描漏”不等于任意 key payload 最终一定泄漏；允许字段里的自然文本携带实际 ID 则是另一条路径。设计验收要同时测 helper 和真实 output_port，不用单层测试替代整体结论。

## 4. 语义不足不能靠扩充禁词表解决

纯结构无法证明：关系文本真有原文支持；模型没有把书中例子当用户事实；中心/中轴不是唯一决定；结论与条件相符。新增“必须含但是/可能/建议”或最少字数硬门会错挡合理表达，也能被无意义套句绕过。

推荐把支持材料与用户事实以明确角色交给生成器，并在独立审查中逐主张核对。审查保留可解释的失败原因和最小返工范围。没有原书时这些语义用例标 SOURCE_BLOCKED / NOT_RUN，不拿 synthetic 标签填补真实性。

组合支持图是对已有获准证据的运行期派生索引，不额外创建一个可以写 approved 的关系授权数据库。方法是否可用取决于具体获准来源和规范化方法内容；关系实例本身不提升成来源权威。避免建立两套不断互相同步的 approval 状态。

## 5. 保留的硬边界与不采用的捷径

保留：系统隔离、无 orientation、用户给牌、不可补牌、输入唯一/完整、来源权限与身份、hash/快照完整性、真实用户批准、生成前门、研究授权、TTL/撤权、公开投影边界、5/9 默认关闭。

拒绝：None=全部关系获准；任意非空核心 item=完整运行；pub→private 反造身份；目录对象=审批；全部永久关闭当修复；为每个漏洞再建同义权威 DTO/数据库；要求每种表达进词表；靠隐藏内部码或简单替换文本放行；把候选/历史测试/目录存在当语义批准。

所有推荐都是本轮候选，待相应主人纳入正式合同后另批实施。
