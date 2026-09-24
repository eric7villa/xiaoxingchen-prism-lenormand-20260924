# Lenormand 独立详细计划（Pro 审查版）

状态：`DESIGN_CANDIDATE_NOT_AUTHORIZED`

## 0. 每一步的强制读题协议

在每个任务、计算、裁决或实施前，先写：

1. 可观察信息；
2. 可控制动作；
3. 不可用信息/权限；
4. 成功量词；
5. 最坏失败构造。

省略任一项不得把结果写成 PASS、DONE 或 READY。

## 1. L0 基线重绑

**目标**：把历史 B、P02/P03、A_FULL_PLAN 与当前 `ecdfb895` 分开绑定。

**动作**：重算包内 SHA/manifest；比较主参考与 D 候选；列出 LN 独占路径、共享接口、历史候选 patch；建立 `CURRENT_LN_BASELINE.json`。

**收口**：每个后续任务都能回答 commit、文件白名单、输入身份、证据位置和回滚点。任何 hash 不一致进入 HOLD。

## 2. L1 体系与权威边界

对应 `S03-LN01..04`。

- 固化 `system=LENORMAND`、独立 operation/authority、三牌有向身份。
- orientation 在 LN 中不存在；不能从 Tarot orientation、Tarot Mentor 或 RWS 投影带入。
- 仅允许获准的 36 牌目录、方法 profile 和公共投影；原始来源、未审候选、作者私有字段不得被 MCP 读取。
- 候选 → review → owner approval → approved projection → runtime 的生命周期必须可追踪；no-match/no-source 是合法停止，不得强填。

## 3. L2 三牌最小运行链

对应 `S03-LN01/02/03/05/06` 与 `S02-T11`。

- 输入：真实问题、三张实际牌、记录顺序；不自动抽牌、不默认方向、不制造固定位置。
- 查询：只按 LN system、method scope、card ids、生命周期和授权身份取数据。
- 组合：建立有向相邻关系和支持图；关系是信号支持，不是牌义拼接总和。
- 输出：现实条件、短期验证信号、可执行选择/边界/退出；不得输出 Tarot 术语、Book T/GD、Mentor 标签或来源报告。
- 无匹配、来源缺失、冲突或撤源均 fail-closed，并保留可解释状态。

## 4. L3 五牌与九牌候选（默认关闭）

对应 `S03-LN07..09`。

- 五牌只在明确开关、获准 profile 和完整验收下开放；第三张是阻力位+中轴卡点，不是单牌结论。
- 九牌只保留中心/周边/横竖线优先级，对角辅助必须独立开关和证据。
- 几何参与数量不能证明语义权重；不能把“5/9 已设计”当作“可运行”。
- 入口、API、公共投影均默认 disabled；未获批准时返回明确的 unavailable/no-match，不泄漏内部资料。

## 5. L4 共享运行接口对齐

只复用跨系统的安全、会话、回执、预算、撤源和研究接口，不复用 Tarot 语义。

- LN COMPOSE artifact 独立 hash、method_scope、system 标记。
- R3 研究仅消费已闭合 LN 结果；研究失败与无可靠解法区分。
- R4 可审查和重组，但不得创造新牌证据、改写 LN 原始 artifact 或调用 Mentor。
- 单一 owner：authority、retrieval、compose、output、receipt 各一套，不建立平行批准系统。

## 6. L5 验收、回滚与上线门

### 必须有的正例

- 三张获准牌按真实顺序完成 prepare/compose/output；输出包含现实条件与验证信号。
- 合法 no-match 继续核心 LN 结构，不强行填补。
- 反向/异常输入不被当作 Tarot 方向；换人换事不带入旧事实。
- 撤源发生在 prepare 与 run 之间时，运行停止且留下 receipt/状态。

### 必须拒绝的反例

- 未获准目录、原始表、Mentor 或 Tarot evidence 被检索。
- 自动抽牌、默认正位、把三牌显示位置变成时间或固定职责。
- 用书中案例推断用户具体人物、日期、疾病、法律/经济事实。
- 五/九牌未开关却从网页/API可见；公共投影反推私有批准信息。
- 几何计数替代语义证据；Tarot/GD/逆位术语渗入 LN。

### 上线分层

`L0` 文件/身份闭合 → `L1` 契约/schema → `L2` provider-off 三牌调用链 → `L3` 授权 DB/撤源/回执 → `L4` 人工语义/浏览器 → `L5` 真实 Provider/部署。未具备环境的层保持 `NOT_RUN`，不能被离线替身覆盖。

## 7. 任务清单与交付

Astra 需要输出：

- `LN_BASELINE_REBIND.json`、`LN_REQUIREMENT_TRACE.json`；
- `LN_SPEC_CN.md`、`LN_INTERFACE_CONTRACTS.json`、`LN_TASKS.json`、`LN_ACCEPTANCE_MATRIX.json`；
- `LN_GAP_REGISTER.json`、`LN_DEPENDENCY_DAG.json`、`LN_OWNER_DECISIONS_REQUIRED.md`；
- `LN_PATCH_ADJUDICATION.json`（逐文件 KEEP/REWORK/HOLD/REJECT，不能直接合并）；
- `LN_CICD_AND_RELEASE_PLAN.md`、`LN_RETURN_CN.md`、`CHECKS.json`、`MANIFEST.json`、`SHA256SUMS`。

终态只能是 `DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW`、`PARTIAL_PENDING_CODEX_REVIEW` 或 `BLOCKED_WITH_EXACT_GAP`；不得写 `DONE`、`PRODUCTION_READY` 或 `APPROVED`。
