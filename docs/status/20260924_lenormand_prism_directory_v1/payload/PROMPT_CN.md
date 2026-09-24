# GPT-6-Astra Pro 补充 Prompt：Book T / Mentor / LN 资料覆盖与缺口裁决

请在先前 LN Pro 计划包的基础上，读取本补充包，独立审计“实际带入了什么、没有带入什么、哪些资料当前最终基线允许使用”。

## 强制读题协议

对每个资料组先列：可观察信息、可控制动作、不可用信息/权限、成功量词、最坏失败构造。任何一项缺失，不得写 PASS、COMPLETE 或 APPROVED。

## 必须回答

1. 核对 `LENORMAND_PRO_PLAN.zip`、A/B 设计输入、`returns 7` 和豆包裁决的实际文件身份与 hash。
2. 分开列出：Book T 运行候选/边界文件、Book T 原始资料、非 281 Mentor 候选、非 281 Mentor 原件、281 全集、LN Matthews/Rana 资料、旧60/新24/师姐资料。
3. 对每组标记 `IN_SCOPE_PRESENT`、`PARTIAL`、`EXPLICITLY_EXCLUDED`、`UNAVAILABLE` 或 `NOT_LN_INPUT`，并给路径、hash、影响范围。
4. 不把 281 全集自动纳入；不把 Tarot Mentor/Book T 迁移到 LN；不把模型一致性或设计候选当批准。
5. 根据最终基线给出资料补齐顺序：哪些是三牌最小路径真正需要的，哪些后置，哪些永久隔离。
6. 设计下一步文件级任务、owner、依赖、正反验收、回滚和关闭门；不得实施代码。

## 最终基线硬边界

- LN 与 Tarot 完全隔离；LN 无 orientation、逆位、Major 权重、RWS/GD 或 Mentor。
- 三牌优先；五/九牌默认关闭。
- 书中案例不等于用户事实；资料缺失、no-match、撤源和冲突必须可记录并 fail-closed。
- Book T 不是最低 Tarot 上线前置，也不是 LN 输入。
- 281 Mentor 是旧版本清理 backlog，不作为当前最低上线前置。
- 真实 DB/Provider/浏览器/远程 CI/部署保持 `NOT_RUN`。

## 交付

请实际落盘并读回：`MATERIAL_COVERAGE_FINAL.json`、`MISSING_MATERIALS_FINAL.json`、`BOOKT_MENTOR_DECISIONS.md`、`LN_SOURCE_ADMISSION_PLAN.md`、`TASKS_MATERIAL_GATES.json`、`ACCEPTANCE_MATERIAL_GATES.json`、`RETURN_CN.md`、`CHECKS.json`、`MANIFEST.json`、`SHA256SUMS`。重新打开 ZIP 做 CRC、成员、路径安全和 hash 校验。状态只能是 `DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW`、`PARTIAL_PENDING_CODEX_REVIEW` 或 `HOLD_WITH_EXACT_GAPS`。
