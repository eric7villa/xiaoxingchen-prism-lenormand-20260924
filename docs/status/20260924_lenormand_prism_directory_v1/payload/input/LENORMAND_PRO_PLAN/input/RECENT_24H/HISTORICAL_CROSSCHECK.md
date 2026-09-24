# B 历史线索交叉核验

DESIGN_CANDIDATE_NOT_AUTHORIZED。历史报告只提供待核问题，不作为本轮执行指令、产品批准或独立测试。所有输入路径/SHA-256 可由 INPUT_IDENTITIES.json 复核；当前代码证据由 CALL_CHAIN.md、BASELINE_COMPARISON.md 与静态索引定位。

|历史线索|本轮与当前字节的对照|主张状态及处理|
|---|---|---|
|DS_INTEGRATED 的 LN_RESULT / PATCH_METADATA / 接口 / owner 记录：来源授权绑定、牌表及 mode↔slug、PG public 与 LN private 合同缺边|四面与补丁按字节分开；现有 ln-three 明确存在但关闭；批准绑定没有从 public 重建的合法边；P 有 L 之外的输出修订|PARTIALLY_TRUE：保留具体缺边，纠正“完全没有 slug”等扩大表述；IR-B-LN-01–06 是本轮候选，不复制旧请求为已采纳合同|
|Prism earlier_FIRST / P08：三牌不可自动过去现在未来；五牌第三轴非独断、四邻接；九牌对角辅助；来源/作者分工|L 三牌结构、独立候选五九及 fixture 可静态核；计数规则和公开标签不能证明书中方法|CONFIRMED 仅限结构与设计目标；真实牌义、作者原文、具体规则授权 UNVERIFIED|
|Prism earlier_SECOND / P08：原书和真实数量未验证；召回不等于组合；五九语义不足；重复包不是多次独立验证|PG cards overlap 是召回；多证据组合还需真实方法许可；DS07 账本真实数量 null，不能变零或估计值|CONFIRMED 对应当前可见合同；原书内容仍 UNVERIFIED；历史四包不计四次独立审查|
|post_mining_A：来源声明与证据完整性|本轮仅取其来源声明审慎性作为审计线索，不将 Mentor 案例或内容导入 LN，不执行旧 source mining|PARTIALLY_TRUE 仅对可迁移的治理边界；不是 LN 原文或批准证据|
|post_mining_B OVERDESIGN_MATRIX / RUNTIME_DESIGN：不过度阻断、可选层、来源身份和输出机制|可迁移的是“身份门与自然语言分开、召回不等于语义、可选层不接管核心”；Mentor/Tarot 专属角色和 schema 不迁入 LN|PARTIALLY_TRUE，适用范围逐条收窄；B 的 OD01–18 与正反用例另做当前字节审计|
|post_mining_C OWNER_DECISIONS / REQUIREMENT_TRACE_831：用户目标、真实成本/选择/验证、系统隔离、模型不代批准|这些原则与当前 Product Foundation/AGENTS 的相关边界共同核对；旧“本轮只设计 Tarot”不适用于当前明确授权 B LN 的任务|产品原则在本轮相关范围 CONFIRMED；旧轮次/派发边界 OUTDATED，不接续旧任务|
|历史 153/164 测试数、旧远端 CI 采样|本轮未安装依赖、未 import 产品、未运行 pytest/DB/provider，也未刷新远端|OUTDATED 对于本轮验收；原历史数字是否对应当时环境仍按作者报告，不升级为本轮 CONFIRMED|
|历史“辅助证据可建核心”“HOLD 可直接进正常结果”“已有解释门故整条链受保护”|L 的角色控制和内部 ACTIVE 验证已存在；解释门未进入 prepare 调用；真正问题是身份、必要支持与运行链未闭合|前两种广义缺陷为 FALSE；存在解释门为 CONFIRMED，但推论整条链安全为 FALSE|

## 阅读覆盖与限制

完成 M/D 全部已选 src/tests 和 L 的静态符号/引用索引；L 全 15 文件逐字节比较，13 个 Python 文件静态解析，fixture 两账本身份与内容核对；对关键 runtime/准入/输出/布局/检索/SQL/入口/阶段合同追读调用者。候选测试被静态读取、建立函数/断言索引并重点审阅相关用例，**没有运行，也不把每条断言视为已证明**。

READING_MAP 证明入口材料存在，不证明其中全部历史叙述为真。本轮不是对 1183 文件逐条进行历史事实审计，也没有在选集外搜索生产实现。历史文件重复出现不增加独立证据权重。缺完整原书、真实批准链、真实数据库与运行回执的地方，仍按 SOURCE_GAPS_AND_OWNER_DECISIONS.md 保留缺口。

## 与本轮成果的可追溯关系

现状与纠错归 BASELINE_COMPARISON/CALL_CHAIN；新的候选合同归 SPEC/FIVE_NINE_CANDIDATE；过挡与真正拒绝归 OVERDESIGN_REVIEW/ACCEPTANCE；后续 write-set 与主人归 TASKS/INTERFACE_REQUESTS/DEPENDENCIES。任何历史结论要被采纳，都必须落到这些当前字节与候选边界上，不能直接拿旧“PASS”填本轮验收。
