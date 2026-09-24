# Prism `Cache miss` 处理协议

## 事实分类

`Cache miss` 是当前读取工具/抓取层没有取得正文的内部状态，不是 GitHub 返回的 HTTP 错误。它不能证明仓库不存在、文件不存在、Prompt 有错、内容有错或 bwrap 不可用。

当前镜像已由 owner 从本地核验：仓库公开，API、网页、raw 和 commit 固定 raw 端点均可取得 `200`。Prism 仍看不到正文时，只能记录为 `READ_CHANNEL_UNAVAILABLE` / `UNVERIFIED`。

## 重试顺序

按以下 commit 固定地址尝试，不要只依赖默认分支缓存：

1. `https://github.com/eric7villa/xiaoxingchen-prism-lenormand-20260924/blob/f25cbb5056e81e95070e14f073c0ce4fd9b17317/START_HERE_CN.md`
2. `https://github.com/eric7villa/xiaoxingchen-prism-lenormand-20260924/raw/f25cbb5056e81e95070e14f073c0ce4fd9b17317/START_HERE_CN.md`
3. `https://raw.githubusercontent.com/eric7villa/xiaoxingchen-prism-lenormand-20260924/f25cbb5056e81e95070e14f073c0ce4fd9b17317/START_HERE_CN.md`

成功读到入口后，再按 `START_HERE_CN.md` 的相对路径读取其余文件。不要把公共镜像的 `PUBLIC_MIRROR_SHA256SUMS` 当作原始输入包校验单；脱敏副本使用公共镜像校验单。

## 停止边界

- 若以上地址全部只返回工具内部 `Cache miss`，停止读取并报告 `READ_CHANNEL_UNAVAILABLE`，不要猜测正文。
- 没有出现明确的 `bubblewrap is unavailable` 和 `no system bwrap was found` 时，不得启用 bwrap fallback。
- 不索取 API key、GitHub token、Keychain 或生产凭据来绕过抓取失败。
