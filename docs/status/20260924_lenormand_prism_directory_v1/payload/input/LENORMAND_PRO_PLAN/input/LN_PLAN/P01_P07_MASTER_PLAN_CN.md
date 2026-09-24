# P01-P07 正式验收与工程补齐总计划

状态：`PLAN_RECONCILED_NOT_IMPLEMENTATION_AUTHORIZATION`

本文件是 2026-09-23 在 **TarotEngine** 项目内形成的当前批次计划主人。它把 P01-P07、两轮
外部回包、8.31 需求、已记录的豆包裁决和当前 Engine 字节重新绑定起来。它不是资料批准、
代码完成、Provider 授权、数据库授权、部署授权或上线证明。

## 1. 项目与基线

### 1.1 实施项目

- 实际实施仓库：`<local-path>`
- 当前分支：`codex/agents-map-rebuild-20260830`
- 当前 HEAD：`ecdfb895fcbbc3f80cc97269388bc0111bc999e0`
- origin：`https://github.com/eric7villa/xiaoxingchen-engine-core.git`
- 当前 `AGENTS.md` SHA-256：
  `c59ebc1cabeb0d63e4a0b57a13375e3a7e863206afa7df0840f5f2f7e4ecbdd8`
- 当前工作树有历史/用户未跟踪内容，dirty count 实测为 70；它不是可直接重放的干净基线。

`<local-path> project/tarot_php_mysql` 是旧 PHP 项目与协作参考仓库，不是本批
替代引擎实施面。本批不把 P01-P07 计划、补丁或状态写入旧仓库。生产身份仍由 Engine 治理
参考所指向的 Aliyun 文档另行约束；本批不连接生产。

### 1.2 三个输入包的绑定

| 输入 | 角色 | 绑定基线 | 当前判断 |
|---|---|---|---|
| `inputs/P01_INPUT_AUTHORITY/` | P01 与 A 计划候选 | `5d771be59c4ce49d1a26d9fced5a4247492dff93` | 已原样收纳；只读候选证据 |
| `inputs/3/P02_EVIDENCE_MENTOR_LN/` | P02/P03 与同一 A 计划候选 | `5d771be59c4ce49d1a26d9fced5a4247492dff93` | 已原样收纳；只读候选证据 |
| `inputs/prism-projects-2026-09-23/PRISM_POST_MINING_C_PROJECT_CICD_20260922/` | C 线后置治理、Harness、CI/CD 输入 | `ecdfb895fcbbc3f80cc97269388bc0111bc999e0` | 已原样收纳；与前两包不是同一基线 |

因此，`5d771be` 与 `ecdfb895` 之间的差异必须先通过 R0 重建；不能将 P01-P07 的回包
直接说成已经针对当前 HEAD 完成。`5d771be` 是 `ecdfb895` 的直系后代候选提交，不是独立
分叉，但它包含尚未逐文件裁决的候选修复，仍须通过 R0 重绑。P01/P02 包中的 `common/plan/`
是 A 详细计划候选；Engine 内的完整 A 计划副本位于
`docs/status/20260922_astra_implementation_pro/IMPLEMENTATION_INPUTS/plan/`，本批计划
是对它的当前状态归一，不另造产品真值。

## 2. 产品对齐检查线

本计划以 Engine `AGENTS.md` 和 `docs/governance/PRODUCT_FOUNDATION_REFERENCE_CN.md`
为稳定规则，并吸收已核验的 8.31 与豆包裁决：

1. 先整副牌与问题主判断，再用单牌、Waite/RWS、Place 和精确命中的 Mentor 补密度。
2. R1 主基调 -> R2 证据/可选 Mentor -> R3 现实机制与强制现实研究 -> R4
   独立会话审查；后段不得静默改写前段，冲突必须回判。
3. `three_story` 不把抽牌顺序、显示左右或中心自动变成时间、因果、固定职位或结果。
4. 不自动抽牌、不默认正位、不把案例当用户事实；完整保留“条件 -> 机制 -> 倾向/分支
   -> 成本/选择 -> 验证信号/退出”。
5. Mentor 是独立可空层；只在卡、正逆位、领域、场景精确命中且逐条获准时启用。合法
   `no-match` 必须继续核心读法，不得用原始课程、模型记忆或模型票数补齐。
6. Tarot 与 Lenormand 的来源、合同、投影、方法和运行链完全隔离。LN 不进入 Tarot
   最低路径；Book T/GD 不是最低上线前置，`four` 才有专门内部例外。
7. 豆包建议 DA-01 至 DA-08 只作为本地裁决输入：最小上线矩阵、LN 后置、宽映射局部
   分级、接口单一主人、产品入口需实证、整副牌输出合同、图文缺口局部 HOLD 等均在
   任务台账中显式绑定，不把建议本身升格为需求批准。

## 3. 分阶段执行计划

### R0：接收、基线重建与证据封存

**文件白名单**：本目录、`docs/status/` 的批次状态文件；不改产品代码。

- 对三个输入包重跑包内 SHA/manifest/CRC，记录输入目录、scope/index、源包 hash。
- 从 `5d771be` 与当前 `ecdfb895` 各自建立文件/接口/测试快照，列出 P01-P07 触及路径。
- 将外部回包状态统一为 `CANDIDATE`、`DESIGNED_NOT_IMPLEMENTED`、`NOT_RUN`、
  `UNVERIFIED` 等事实状态；不沿用“verified/complete”宽表述。
- 以当前 HEAD 为实施基线；5d 只作为候选补丁的祖先/来源，不能自动合流。

**收口**：所有下一批任务能回答“针对哪一个 commit、改哪些路径、证据是哪一包”；否则停止。

### R1：P01 输入与运行权威

统一 session/intake/domain 合同：确认后的 `effective_topic` 与 digest、服务端主体绑定、
pending 一次性 CAS、过期/取消、换人换事零带入、弱问法重写不洗白安全风险、Tarot orientation
必填、Lenormand 禁止 orientation、缺牌 fail-closed。不得引入第二批准系统、客户端 authority、
自动抽牌或内存存储冒充持久化事实。

### R2：P02 证据、Mentor 与 Lenormand 隔离

统一来源坐标、生命周期、获准读取、核心覆盖、Mentor 多命中/no-match、未述方向和隔离
错误。Mentor 仍须 candidate -> review -> 爸爸批准 -> approved projection -> runtime 的
完整链路；旧60、新24、宝剑6/8均不能由“模型互验”直接进入 runtime。LN 的 Matthews/Rana
链路独立，不能读取 Tarot Mentor 或 RWS/GD 规则。

### R3：P03/P04/P05 研究、回执与持久化

每个合法 run 都必须进入现实研究状态：先 Grok Search，失败后按 2s/8s 退避重试两次，再走
独立 Tavily search+fetch 通道，最多三次。闭合两路研究通道、去标识化、请求/响应/操作身份/
服务端时间/字节 hash 回执、联网失败与无可靠解法双状态、撤源竞态、幂等、保留期、事务和数据库
适配。研究只能服务 R3 解法，不能回填
牌义、用户事实、R1/R2 或 Source Mining。真实 Provider/PG 仍是独立后置门。

### R4：P06/P07 完整调用链与 Harness/CI

将 R1-R4 编排、冲突回判、不可变 artifact、零工具 R4、受控交付、Harness grant/consume、
CI 收集和失败证据接成一条 provider-off 可复验链。Harness 控制范围，不判断牌义；CI 通过不
等于产品正确。P07 的 41 `PARTIAL`、15 `WAITING`、0 `DONE` 保持为历史作者状态，必须
逐任务重验，不得用 8 个治理文档 PASS 覆盖 282 个 `NOT_RUN`。

### R5：统一验收、真实门与发布

按 L0-L5 分层：输入/产物身份、代码契约、调用链/DB/安全、真实研究、人工语义/浏览器、
发布/回滚。固定 Python 3.12 与锁依赖，运行 ruff/mypy/schema/unit/集成/迁移/必要 mutation、
Harness、gitleaks、actionlint、Docker `push=false`、SBOM 和证据生成。未授权的 PostgreSQL、
Provider、浏览器、远端 CI、SSH、部署、发布一律 `NOT_RUN`，不以替身冒充真实门。

## 4. 现阶段停止条件与上线定义

本批计划完成不改变运行状态。最低上线仍至少需要：

- 当前 HEAD 上可重放、可回滚的最小 Tarot 主链；
- bounded incremental Mentor consumer；
- 至少一条 source-faithful 且爸爸逐条批准的 runtime Mentor item；
- 合法 no-match、换人换事隔离、确认改问不带旧 facts、缺牌/方向/安全门反例通过；
- R3 强制现实研究按合同进入；两路都失败时可只依据已有 R1/R2 作答，但必须明确记录联网失败；
  研究成功但无可靠解法必须使用另一状态；
- 真实环境、浏览器、部署和发布授权分别通过。

因此当前终态是：**计划已在 Engine 内落盘，工程候选仍未完成，资料未批准，真实运行和
生产发布未开始。**

## 5. 回滚与并行边界

本批只收纳输入和写计划，不改 Engine 代码；回滚是删除本批新增状态目录，不触碰历史目录。
后续可并行做不共享写面的证据审计、Mentor 保真审计和 CI/CD 计划复核；基线重绑、候选批准、
projection、共享控制器合流、统一回归、生产与发布必须由 Codex 串行完成并另获授权。
