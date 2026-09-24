# Prism 执行 Prompt：Lenormand 当前基线与详细计划落地

你现在在 GitHub 仓库 `eric7villa/xiaoxingchen-engine-core` 的分支：

`codex/lenormand-prism-directory-20260924`

请直接以该分支的文件为输入，不依赖用户本机 Downloads，不要求用户再次上传 ZIP。

## 项目身份

实施项目是 TarotEngine。先读取根目录 `AGENTS.md`，尤其是 `## 0. 先看这里：不要猜项目要做什么`，再读取：

1. `docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md` §0–§2、§4、§7–§8；
2. `docs/governance/PROJECT_MAP_CN.md`；
3. `docs/governance/SOURCE_LIFECYCLE_CN.md`；
4. `docs/status/20260924_lenormand_prism_directory_v1/README_CN.md`；
5. `docs/status/20260924_lenormand_prism_directory_v1/READING_MAP_CN.md`；
6. `docs/status/20260924_lenormand_prism_directory_v1/DIRECTORY_EXTRACTION_INDEX.json`；
7. `docs/status/20260924_lenormand_prism_directory_v1/FINAL_COMPATIBILITY_REPAIR_AND_LN_PLAN_CN.md`；
8. `docs/status/20260924_lenormand_prism_directory_v1/payload/PROMPT_CN.md`；
9. 按 `READING_MAP_CN.md` 指定范围读取 `payload/`。

`payload/` 是递归解包后的目录。不要寻找或假定 ZIP 容器存在；不要扫描与本次 LN 任务无关的完整历史资料来扩大范围。

## 任务目标

完成一次 Lenormand 基线复核和可执行详细计划：

1. 绑定当前 Git commit、AGENTS hash、输入目录 manifest 和 SHA；
2. 对照最近 24 小时 Astra/Doubao/P01–P07 资料，区分当前字节、候选设计、未授权资料和历史快照；
3. 形成 LN 三牌最小路径的最终规范、接口、任务、验收、依赖、owner、回滚和缺口；
4. 五牌/九牌保持默认关闭，并写出明确开启条件；
5. 证明 Tarot、Mentor、Book T、RWS/GD、逆位规则不会进入 LN；
6. 逐项裁决已有 LN 候选 patch：`KEEP_CANDIDATE`、`REWORK`、`HOLD` 或 `REJECT`；
7. 只在当前代码和授权资料确实支持时实施代码。缺资料、缺 approved projection、缺 DB/Provider/浏览器/远端 CI 时保留 `HOLD` / `NOT_RUN`，不能用摘要或模型记忆补齐。

## 五项读题协议

对每个任务和裁决先列：

1. 可观察信息；
2. 可控制动作；
3. 不可用信息/权限；
4. 成功量词；
5. 最坏失败构造。

缺少任一项不得写 `PASS`、`DONE`、`APPROVED` 或 `READY_FOR_DEPLOY`。

## LN 硬边界

- LN 没有 Tarot orientation、逆位、Major 权重、RWS/GD、Book T 或 Tarot Mentor。
- 三牌是当前最小候选路径；五牌/九牌默认关闭。
- 只能消费获准的 36 牌目录、Matthews/Rana 方法资料和 approved projection。
- 书中案例不等于用户事实；不自动抽牌，不制造日期、地点、人物、医疗、法律、经济或隐藏动机。
- 合法 no-match、来源缺失、撤源、冲突和 provider-off 都必须有可观察状态；不能跨卡系或跨生命周期兜底。
- 真实 PostgreSQL、Provider、浏览器、远端 CI、部署和发布保持独立验收。

## 写入范围

允许写入：

- `docs/status/20260924_lenormand_prism_directory_v1/returns/PRISM/attempt_001/`
- 经任务白名单明确需要的 LN 专属代码/测试路径。

禁止：

- 修改 `AGENTS.md`、产品基础、生命周期主人文件；
- 直接应用 5d 候选整树或旧 PHP 代码；
- 把候选资料升级为 approved projection；
- 运行真实 DB、Provider、部署或发布；
- 删除用户已有修改或覆盖共享 owner 文件。

## 必须落盘的回包

在 `returns/PRISM/attempt_001/` 实际写入并读回：

- `RETURN_CN.md`
- `LN_BASELINE_REBIND.json`
- `LN_SPEC_CN.md`
- `LN_INTERFACE_CONTRACTS.json`
- `LN_TASKS.json`
- `LN_ACCEPTANCE_MATRIX.json`
- `LN_GAP_REGISTER.json`
- `LN_DEPENDENCY_DAG.json`
- `LN_PATCH_ADJUDICATION.json`
- `CHECKS.json`
- `MANIFEST.json`
- `SHA256SUMS`

重新计算 manifest 和 SHA，重新打开并核对所有输出文件。最终状态只能是：

`DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW`、`PARTIAL_PENDING_CODEX_REVIEW` 或 `HOLD_WITH_EXACT_GAPS`。

停止时说明已完成、未运行、未授权和需要爸爸裁决的部分。不要只在聊天窗口声称完成。
