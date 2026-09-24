# Lenormand 当前基线与最近 24 小时核对

状态：`BASELINE_REBOUND_DESIGN_ONLY_NOT_AUTHORIZED`

## 1. 项目与绑定

- 实施项目：`<local-path>`
- 旧 PHP 仓库：`<local-path> project/tarot_php_mysql`，只作历史参考，不是实施面。
- 主参考 HEAD：`ecdfb895fcbbc3f80cc97269388bc0111bc999e0`
- D 候选：`5d771be59c4ce49d1a26d9fced5a4247492dff93`，只能作候选对照，不自动合并。
- `AGENTS.md` SHA-256：`c59ebc1cabeb0d63e4a0b57a13375e3a7e863206afa7df0840f5f2f7e4ecbdd8`
- 当前工作树有历史/用户未跟踪状态文件；本包不把 dirty tree 当成可发布树。

## 2. 已有 LN 设计来源

最近 24 小时可核验的主要输入：

1. `docs/status/20260922_astra_parallel_dispatch/ASTRA_B_LENORMAND_DEEP_20260922/`：独立 LN 设计派发包及其停止/重启记录。它证明历史设计输入曾被封存，不证明 LN 已实现。
2. `docs/status/20260923_execution_dispatch_v6/PRISM_R2_RESEARCH_LN/common/A_FULL_PLAN/`：当前 P01–P07 归一后的详细计划副本，含 `S03-LN01..09`、接口、任务、验收、依赖和 B 设计原件索引。
3. `docs/status/20260923_execution_dispatch_v6/PRISM_R2_RESEARCH_LN/common/`：R2/R3 共享计划；LN 与 Tarot、Mentor、BookT、R3 研究的隔离合同在此绑定。
4. `docs/status/20260924_astra_final_adjudication_v1/input/DOUBAO_ALIGNMENT_AUDIT/`：豆包对齐审计。其结论是 LN 整体后置于 Tarot 最低路径，保留独立系统、最小三牌、五/九牌默认关闭、公共投影不能反推私有批准信息。

## 3. 当前真实状态

- LN 三牌最小路径：有设计候选，未实施、未授权、未通过运行验收。
- 五牌/九牌：候选设计存在，默认关闭，不能因有几何/任务文件而开放。
- 36 牌目录与作者来源：需要逐条获准读取和身份/生命周期检查；不以模型共识、历史候选或几何计数替代批准。
- 读取、组合支持图、输出、运行载体和入口：均为设计或候选补丁，不能称为生产调用链。
- 真实 PostgreSQL、Provider、浏览器、远程 CI、部署：未运行，均保持 `NOT_RUN`。
- LN 不消费 Tarot Mentor、RWS/GD、Tarot orientation、Tarot R1/R2 规则；不得把 LN COMPOSE 铸造成 Tarot R2。

## 4. 产品边界

- LN 是现实信号语法：问题上下文、相邻牌、组合、中心/焦点、线向、障碍/路径、短期验证信号和具体条件。
- 三牌只读有向线与组合，不套 Tarot 图像、逆位、Major 权重或固定时间轴。
- 五牌本站候选位置为：现状 / 助力 / 阻力兼中轴 / 隐藏变量 / 建议；第三张有结构权重但不能单牌独断，必须读取四个相邻对。
- 九牌候选优先中心、中心周边、横/竖线；对角线仅在明确批准的方法中作辅助。
- 书中案例、医疗/法律/经济细节、具体日期地点、人物叙事都不是用户事实，只能转化为经批准的机制、信号或条件。
- 研究只能服务 R3 解决方案，不能回填 LN 牌义、用户事实或 Mentor。

## 5. 尚未证明的事项

1. 当前代码中 LN 的完整 prepare → authorized retrieval → compose → output → status/cancel 链是否闭合。
2. B 候选与 `ecdfb895`/`5d771be` 的逐文件差异是否仍适配当前字节；不能直接套历史 patch。
3. 获准目录、私有 PG scope、撤源竞态、回执和幂等是否有单一 owner。
4. 三牌最低路径的语义金丝雀是否覆盖“现实信号而非 Tarot 化”的反例。
5. 五/九牌的开放条件、公共投影和浏览器入口是否 fail-closed。

## 6. 本包的用途

本包只给 GPT-6-Astra Pro 做独立核验、裁决和详细设计；不授权改代码、批准资料、运行 DB/Provider、部署或发布。Astra 必须先复算当前字节，再决定保留、修订、拒绝或保持缺口。
