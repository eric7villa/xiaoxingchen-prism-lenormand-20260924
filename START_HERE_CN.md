# Prism 临时交接入口

1. 先读 `PUBLIC_MIRROR_NOTICE_CN.md` 和 `PUBLIC_SOURCE_IDENTITY.json`。
2. 再读 `docs/status/20260924_lenormand_prism_directory_v1/README_CN.md`、`READING_MAP_CN.md`。
3. 遇到 `bubblewrap is unavailable` 时，执行同目录的 `PRISM_BWRAP_FALLBACK_PROMPT_CN.md`，切换为 GitHub 文件读取/文档设计模式。
4. 主任务 Prompt：`docs/status/20260924_lenormand_prism_directory_v1/PRISM_EXECUTION_PROMPT_CN.md`。
5. 所有缺失原件、授权链和真实运行保持 `UNAVAILABLE`、`HOLD` 或 `NOT_RUN`；不要向本仓库写入秘密。

如果读取工具显示 `Cache miss`，先读 `CACHE_MISS_HANDLING_CN.md`。这不是 bwrap 错误，也不能据此断言 GitHub 文件不存在。

本镜像只允许用于一次 Prism 离线审查。完成后请通知 owner 关闭镜像。
