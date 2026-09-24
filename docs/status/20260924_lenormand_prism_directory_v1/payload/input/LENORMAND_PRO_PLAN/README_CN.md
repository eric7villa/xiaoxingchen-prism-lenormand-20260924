# Lenormand Pro 计划包

这是给 GPT-6-Astra Pro 的独立 LN 基线重核与详细设计输入包。

## 本包不代表什么

- 不是代码补丁，不是生产镜像，不是资料批准，也不是运行授权。
- 不允许因历史报告写过 `PASS`、`COMPLETE`、`DONE` 而跳过当前字节核验。
- 真实 PostgreSQL、Provider、浏览器、远程 CI、部署保持 `NOT_RUN`。

## 使用顺序

1. 先核对 `INPUT_INDEX.json` 和每个输入文件 SHA-256。
2. 读 `LENORMAND_BASELINE_REPORT_CN.md` 与 `LENORMAND_DETAILED_PLAN_CN.md`。
3. 按 `PROMPT_CN.md` 的强制五项读题协议执行。
4. 产物必须真实落盘、读回、封存并重新打开 ZIP 验证。

## 基线结论

LN 当前是独立设计候选：三牌是最小路径；五牌、九牌默认关闭；Tarot/ Mentor/BookT 不得作为 LN 语义输入；所有候选仍需逐项批准和运行验收。
