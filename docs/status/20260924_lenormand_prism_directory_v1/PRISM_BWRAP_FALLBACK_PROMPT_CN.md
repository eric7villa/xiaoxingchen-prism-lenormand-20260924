# Prism bwrap 不可用时的降级执行 Prompt

你遇到的错误：

```text
bubblewrap is unavailable
no system bwrap was found
```

这是 Prism 执行容器的工具缺失，不是 TarotEngine 代码、LN 资料或 GitHub 分支错误。请不要因为这个错误终止整个任务，也不要把它报告成项目测试失败。

## 降级方式

切换到 **GitHub 文件读取 + 文档设计模式**：

1. 继续读取当前分支 `codex/lenormand-prism-directory-20260924` 的文件；
2. 读取 `README_CN.md`、`READING_MAP_CN.md`、`DIRECTORY_EXTRACTION_INDEX.json`、`FINAL_COMPATIBILITY_REPAIR_AND_LN_PLAN_CN.md` 和 `payload/PROMPT_CN.md`；
3. 使用 Prism 当前可用的文件读取/写入能力，不调用 shell、Docker、bubblewrap、数据库、Provider、浏览器或远程 CI；
4. 继续完成 LN 基线绑定、详细计划、候选裁决、依赖、owner、正反验收、回滚和缺口设计；
5. 若当前环境无法写入仓库，直接在回包中完整输出交付文件内容，并标明 `OUTPUT_WRITE_NOT_AVAILABLE`；不要假称已经落盘；
6. 所有命令测试、ruff、mypy、pytest、compileall、DB、Provider、浏览器和 CI 记为 `NOT_RUN`，原因写 `bwrap_unavailable`；
7. 不要安装系统包，不要修改宿主机，不要索取 Keychain、凭据或生产秘密。

## 仍然必须遵守的边界

- Tarot 与 Lenormand 完全隔离；LN 不使用 Tarot orientation、逆位、RWS/GD、Book T 或 Mentor。
- 三牌是最小候选路径；五牌/九牌默认关闭。
- 候选、摘要、模型一致性和静态文件存在都不是资料批准。
- 缺少 approved projection、36 牌授权目录、Matthews/Rana 原件或私有 retrieval 生命周期时保持 `HOLD` / `NOT_AUTHORIZED`。
- 每个任务先列五项协议：可观察信息、可控制动作、不可用信息/权限、成功量词、最坏失败构造。

## 回包最低要求

即使没有 bwrap，也要输出或写入：

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
- `SHA256SUMS`（只有实际写入文件后才能生成）

终态只能是 `PARTIAL_PENDING_CODEX_REVIEW`、`HOLD_WITH_EXACT_GAPS` 或
`DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW`。其中没有实际测试证据时不得使用任何 `PASS` 作为产品或运行结论。
