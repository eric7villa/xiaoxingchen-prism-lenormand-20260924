# CHECKPOINT_B_LENORMAND — 本轮回包

爸爸，本轮 B 雷诺曼专项离线设计已完成，提交 Codex 审阅后停止。

**状态：DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW。**
**全部设计权威级别：DESIGN_CANDIDATE_NOT_AUTHORIZED；实现状态：DESIGNED_NOT_IMPLEMENTED。**

不是 S03 整体完成，不是资料批准、代码实施、产品测试通过或运行开放。A 主线、原输入和历史检查点均未修改。

## 1. 实际完成

完成 M/D/L/P 四面身份与逐文件比较；全选 src/tests 静态依赖/符号核查与候选 15 文件检查；实际入口到牌表、结构、检索、准入、输出、研究/审查/交付的调用链；三牌最小受权路径；五九牌默认关闭候选；过度设计与过挡审计；13 个文件/符号级实施任务、44 组成对验收、6 个共享接口请求和来源缺口/主人裁定。

任务覆盖 B-LN-R01–R14。每任务列出 baseline 前提、EXISTING_D / PROPOSED_NEW、已查实符号与候选新增符号、生产者/消费者、字段/失败/权限、迁移、依赖、回滚、CI、先红后绿、主人；每验收有有效好例、真正坏例、前提、精确未来测试文件/符号和命令。**全部产品命令均为 NOT_RUN，不应在读取本回包时自动执行。**

## 2. 应优先审阅的结论

**P0 — 受权消费闭环。** L 的核心门只看核心条目非空，prepare 的 UNBOUND 牌表状态未进入门条件；expected 绑定可选、relation allow-list 默认 None 也不足以表达生产准入。D 的 PG 工具返回 public 投影，不能据此反造 LN 私有批准身份。推荐复用既有 EvidenceRepository、候选/审阅/批准/发布链，补私有读取和当次完整绑定，不增设平行批准权威。以上是静态合同结论，不是生产漏洞复现。

**P0 — 权威与持续有效性。** 现有来源审批 SQL 可复用，但 pin 同 ID 的幂等返回不能证明资料仍 ACTIVE。实际依赖目录/方法/条目须在语义调用与交付前复核，事务/ACL/撤回由 S04 吸收；LN 独立编排不能借 TarotStageExecutor 的固定 R1–R4 职责补闭环。

**P1 — 候选采用与不过挡。** LN 15 文件相对 D 为 7 修改、3 新增、5 相同；P 还含输出键值/casefold 等修订。L 的 DS08 测试绑定不同 reading.py hash，两个补丁均未覆盖此差异。必须按真实目标重绑，不能修改产品凑旧 hash，也不能继承 153/164。缺词表、普通子串、无可选 Rana、合法 GLOBAL 和多证据支持不能被一刀切拒绝；来源与快照身份硬门不放松。

**P1 — 五九牌。** 五牌保留本站五标签、第三张阻力兼中轴非独断、四邻接；九牌保留中心/周围/横纵，正交几何与对角辅助严格分开。几何参与计数不是语义权重证明，本站规则不冒充作者方法。五九模式独立授权、默认关闭，不降成三牌。

## 3. 阅读顺序与成果入口

|文件|用途|
|---|---|
|BASELINE_COMPARISON.md / INPUT_IDENTITIES.json|四面、逐文件身份及测试报告边界|
|CALL_CHAIN.md / SYMBOL_INDEX.json / CALLER_REFERENCE_INDEX.json|真实文件/符号/调用者，区分断点与选集未见|
|SPEC.md|三牌从用户事实到受权证据、组合支持、现实验证与公开输出的候选合同|
|FIVE_NINE_CANDIDATE.md|五九牌几何、方法归属、非独断与默认关闭|
|OVERDESIGN_REVIEW.md|18 项过度设计/安全门成对审计|
|TASKS.md / TASKS.json|13 个实施切片与精确 write-set/hash/符号|
|ACCEPTANCE.md / ACCEPTANCE.json|44 组好坏例、过挡与来源缺失验收，均 NOT_RUN|
|DEPENDENCIES.md / INTERFACE_REQUESTS.json|局部依赖与 S02/S03/S04 主人吸收边界|
|SOURCE_GAPS_AND_OWNER_DECISIONS.md|8 项精确缺口、解锁证据、真正产品/资料决策|
|HISTORICAL_CROSSCHECK.md / SOURCE_MINING.md|历史线索五状态更正与本轮治理审计|
|CANDIDATE_FILE_DIFFS.json / MAIN_D_FILE_DIFFS.json / PATCH_INSPECTION.json|逐文件差异与未应用补丁文本核验|
|CANDIDATE_TEST_REVIEW.json / DS_OUTPUT_DELTA_REVIEW.txt|候选测试静态断言索引与 P 输出差量；不是测试回执或已应用补丁|
|INPUT_VERIFICATION.json / READING_RECEIPT.json / CHECKS.json|实际传输、输入不变、静态一致性、阅读身份回执|
|STATE.json / MANIFEST.json / SHA256SUMS|B 状态与载荷封存；manifest 不列自身/校验单|

B 包仅包含本轮成果和输入身份/审计索引，不复制项目历史树或产品实现。复核源码需配合原输入 ZIP；不把源快照缺省解释为已合并实现。

## 4. 检查与未运行

输入 ZIP SHA-256：`4626f0e759c597ed5c4ccb75495dfdf270e251b63fe4438885a80d2794b6e39a`。

本轮重新执行已审阅的标准库 `VERIFY_PACKAGE.py`，退出 0；14 项离线一致性检查通过，包括 1183 输入文件逐项不变、ZIP 安全/CRC、任务与验收引用、write-set/hash/既有符号、条件依赖无环、共享接口实际定位、L 全15文件检查以及 AGENTS 入场/收工同 hash。S00 的 1097 条输入身份及两个基线 663 个选定文件的包内绑定已重核；未独立取得 Git 对象，不扩张为提交真实性或现网确认。

没有运行产品代码、产品测试、DB、迁移、provider、网络、外部模型、远端 CI、Git 写入或部署；没有批准资料。真实原书、36 张获准牌表、生产批准实值、PG 环境与端到端运行效果仍 UNVERIFIED，分别只阻塞对应验收。当前设计范围没有未完成模块；这些未来前提不伪装成完成，也不让工程设计全局停工。

本轮设计审计发现并更正了符号表面归属、草稿迁移定位和本地 owner-decision 引用；未修改原源码，不能把更正当作产品修复。基础文件 IO 未发生两次独立失败。

## 5. 归档与停止门

输出名 `CHECKPOINT_B_LENORMAND.zip`，成员统一在 `B_LENORMAND/` 下。MANIFEST.json 只列载荷文件，不列 MANIFEST.json 与 SHA256SUMS；SHA256SUMS 覆盖全部载荷及 MANIFEST.json，不列自身。重新打开 ZIP 检查逐成员/CRC、清单集合、内容 hash 与校验单闭合。最终 ZIP 的 SHA-256 和封存结果写在包外 `CHECKPOINT_B_LENORMAND_VERIFICATION.json`，避免自引用。

回滚仅删除本轮新增 B 输出与临时工作区；不得删除原附件或覆盖 A/base/restart/checkpoint。下一门是 Codex 对候选设计的审阅与共享主人吸收，不是自动实施授权。

**交回本 ZIP 后停止。不自动进入 A、S02/S03 实施、不开放任何运行、不续跑。**
