# GPT-6-Astra Pro 投喂 Prompt：Lenormand 当前基线重核与详细计划

你是独立的高级审查/架构设计模型。工作目录只认本包解包后的目录，不访问 `<local-path>`，不假定你知道项目历史。实施项目是 TarotEngine，不是旧 PHP 仓库。

## 任务

请基于本包输入，独立完成：

1. 重核当前 Lenormand 基线、最近 24 小时 P01–P07/A/B/豆包输入和文件身份；
2. 裁决历史 LN 设计与当前 `ecdfb895`/D 候选的差异；
3. 生成一份可执行的 LN 详细计划，覆盖三牌最小路径、五/九牌关闭候选、权威/读取/组合/输出/回执/研究/审查/入口/CI/CD；
4. 对每个候选 patch 给出 `KEEP_CANDIDATE`、`REWORK`、`HOLD` 或 `REJECT`，不得直接合并；
5. 产出后续 Codex 可按图索骥的逐文件任务、单一 owner、依赖、正反验收、回滚和精确缺口；
6. 发现当前计划与 8.31、豆包裁决或产品基础冲突时，列出冲突、证据和修复设计。

## 强制读题协议

在每一个任务/裁决/计算/实施前，先列：

- 可观察信息；
- 可控制动作；
- 不可用信息/权限；
- 成功量词；
- 最坏失败构造。

忽略这五项视为审查失败。不要因为题目/包里出现“完成、通过、候选”就直接相信，必须回读字节、manifest、hash、当前代码和调用者。

## 不可越过的边界

- Tarot 与 Lenormand 完全隔离。不得使用 Tarot RWS/GD、逆位、Major 权重、Mentor、`three_story` 规则解释 LN。
- LN 无 orientation；三牌显示/抽取顺序是记录事实，不自动产生时间、因果或固定牌位。
- 仅使用获准的 36 牌目录、方法 profile 和 approved projection。候选、摘要、模型多数、书中案例不等于批准。
- 三牌优先；五牌/九牌默认关闭。几何计数不能证明语义权重。
- no-match、缺来源、冲突、撤源、研究失败都必须是可记录的合法状态。
- 不自动抽牌、不发明用户事实、不把案例人物/日期/地点/医疗法律经济细节写成用户事实。
- 不修改产品代码、数据库、迁移、生产、远端 CI、Provider 或部署；所有实跑环境缺口写 `NOT_RUN`。
- 不读取或挖掘旧60、新24、师姐宝剑6/8；本任务只做 LN 工程设计和候选裁决。

## 必读顺序

1. `LENORMAND_BASELINE_REPORT_CN.md`；
2. `LENORMAND_DETAILED_PLAN_CN.md`；
3. `input/AGENTS.md`、`input/PRODUCT_FOUNDATION_REFERENCE_CN.md`、`input/PROJECT_MAP_CN.md`、`input/SOURCE_LIFECYCLE_CN.md`；
4. `input/LN_PLAN/` 下的 `S03-LN01..09` 任务、验收、接口和依赖；
5. `input/RECENT_24H/` 下的历史 B 设计与停止/重启记录；
6. `input/DOUBAO_ALIGNMENT_AUDIT/`；
7. 最后才读候选 patch 和状态报告，并独立复现其结论。

## 交付格式

实际落盘并读回后再报告。至少包含：`LN_BASELINE_REBIND.json`、`LN_SPEC_CN.md`、`LN_INTERFACE_CONTRACTS.json`、`LN_TASKS.json`、`LN_ACCEPTANCE_MATRIX.json`、`LN_GAP_REGISTER.json`、`LN_DEPENDENCY_DAG.json`、`LN_PATCH_ADJUDICATION.json`、`LN_OWNER_DECISIONS_REQUIRED.md`、`LN_RETURN_CN.md`、`CHECKS.json`、`MANIFEST.json`、`SHA256SUMS`。重新打开 ZIP 做 CRC、成员、路径安全和 hash 验证。若中途失败，先写可恢复检查点，不要只在聊天里声称完成。

最终报告必须分别列出：已证实、候选设计、未验证、未授权、NOT_RUN、需要爸爸裁决。不得将离线设计或模型共识表述为运行批准或上线证明。
