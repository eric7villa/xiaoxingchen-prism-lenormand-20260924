# Prism 临时公共只读镜像说明

本仓库是给 Prism 的临时、最小、只读交接镜像，不是 TarotEngine 主仓库，也不是生产代码仓库。

## 可见范围

- 仅包含 Lenormand 计划、覆盖审计、缺口登记、执行 Prompt，以及 `LENORMAND_PRO_PLAN` 的计划与审查输入。
- 不包含 TarotEngine 的完整 Git 历史、代码树、数据库、Provider、Keychain、密钥、`.env`、真实用户资料或生产配置。
- 不包含 `ASTRA_RETURNS_7` 的完整原始证据树；缺失部分必须保持 `UNAVAILABLE/HOLD`，不得用摘要补齐。
- 所有产品实施、资料批准、runtime 授权、数据库/Provider/浏览器/CI 运行仍未授权。

## 脱敏处理

为避免暴露本机目录和外部审查工作区，公开镜像中的文本副本将本机绝对路径、`/mnt/data` 路径、外部聊天工作区路径替换为相对标签。载荷语义未据此升级，原始 hash 只作为输入身份记录，不能把脱敏副本当作原始字节。

## Prism 运行边界

使用 `PRISM_BWRAP_FALLBACK_PROMPT_CN.md`。不要索取或写入任何 API key、GitHub token、Keychain、数据库凭据或生产秘密；不要运行 shell、Docker、数据库、Provider、浏览器或远程 CI。没有实际写回能力时，完整输出回包并标记 `OUTPUT_WRITE_NOT_AVAILABLE`，不得假称落盘。

镜像任务完成后应立即设为私有或删除；在此之前只允许读取，不允许提交、部署或发布。
