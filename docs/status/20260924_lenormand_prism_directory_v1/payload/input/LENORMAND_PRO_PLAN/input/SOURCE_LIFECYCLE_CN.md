# 资料生命周期与批准边界

## 合法状态机

```text
RAW -> EXTRACTED -> NORMALIZED -> CANDIDATE -> REVIEW_REQUIRED
REVIEW_REQUIRED -> HOLD | REJECTED | APPROVED_PROJECTION
HOLD -> REVIEW_REQUIRED | REJECTED
APPROVED_PROJECTION -> INDEXED | SUPERSEDED
INDEXED -> ACTIVE | SUPERSEDED
ACTIVE -> SUPERSEDED
```

`REJECTED` 和 `SUPERSEDED` 是终态。同状态重复请求只返回幂等结果，不创建新的生命周期事件。

数据库 `governance.record_review_decision` 与 Python 状态机使用同一条 HOLD 回转：只有独立 reviewer LOGIN 可以执行 `HOLD -> REVIEW_REQUIRED | REJECTED`，并追加生命周期事件；HOLD 不是无说明死路。

## 明确禁止

- `CANDIDATE -> ACTIVE`。
- 模型身份创建 `APPROVED_PROJECTION`。
- 机械校验把语义内容直接批准；机械 PASS 最多进入 `REVIEW_REQUIRED`。
- `HOLD`、`REJECTED`、`AUDIT_HISTORY` 或 synthetic fixture 进入真实运行时检索。
- Tarot 候选发布进 Lenormand 投影，反之亦然。
- Lenormand 条目携带 orientation。
- reviewer 或 publisher 代替最终用户批准。

## 最终批准记录

最终批准必须由独立用户批准身份创建，并至少绑定：

- candidate ID；
- candidate 内容 SHA-256；
- SourceSystem；
- 决定与时间；
- 批准主体；
- 待发布 projection release。

发布时要在同一数据库事务中重新验证这些绑定关系和有效 Harness grant。批准后候选字节发生任何变化，原批准自动失效，不能“沿用意思相近的批准”。

## no-match

no-match 是正常、可观察的结果，不是需要模型补写的异常。至少区分：

- 没有满足全部过滤条件的获准条目；
- 请求了当前没有获准资料的可选层，例如 Mentor 或 Book T；
- 指定的 projection snapshot 不存在或不可用；
- Provider-off 能力被明确禁用。

运行时总序固定为：指定 snapshot 不存在先返回 `NO_SNAPSHOT`；snapshot 存在但允许
来源层没有任何 ACTIVE 条目返回 `NO_LAYER_MATCH`；层存在但完整过滤链无命中返回
`NO_APPROVED_EVIDENCE`。Provider-off stub 独立返回 `DISABLED_PROVIDER_OFF`。ACTIVE
release 即使条目为空也仍是“snapshot 存在”，不能误报 `NO_SNAPSHOT`。

no-match 不得触发跨系统、跨来源层或生命周期放宽。

## no-match 唯一主人与审计细分注册表

公共 no-match 码的闭集与运行时总序以本文件为唯一主人（一事实一主人）。本节是
2026-09-11 爸爸裁决（dispatch_147 D6 候选甲）的落点：`PRODUCT_FOUNDATION_REFERENCE_CN.md`
§8 只引用本节并保留产品原则；`PROJECT_MAP_CN.md` §6 只引用，不复制码表。

公共码闭集固定为以下四值，不得扩展第五码或第六码：

<!-- NO_MATCH_CLOSED_SET_BEGIN -->
```text
NO_SNAPSHOT
NO_LAYER_MATCH
NO_APPROVED_EVIDENCE
DISABLED_PROVIDER_OFF
```
<!-- NO_MATCH_CLOSED_SET_END -->

细分理由只进审计/保真审查面，不进用户可见输出；任何细分码逐码绑定
{含义, 归并到的公共码, 可见性=内部, 来源合同, 批准状态}。候选合同（如 Mentor 轨
七细分码）是注册表的候选输入，状态 `CANDIDATE_ONLY`；采纳为首批注册表仍需爸爸对
该批单独批准，不得当作已批准口径引用。

R3 研究两终态（检索失败 / 无可靠解决办法）不属于本注册表；其枚举由研究层设计
拥有，不得被公共码吞并。

## 审计与用户可见性

内部生命周期事件和检索审计只记录必要元数据，不能把 secret 或用户隐私复制进日志。普通用户只看安全投影，不看来源名、内部 ID、生命周期、哈希、路径或工程标签。
