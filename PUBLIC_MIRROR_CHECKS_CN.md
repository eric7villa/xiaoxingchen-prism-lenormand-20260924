# 公共镜像检查说明

本镜像对带入的文本做了路径脱敏，因此原 `LENORMAND_PRO_PLAN/PACKAGE_SHA256SUMS` 只保留作历史输入身份，不能用于验证脱敏副本；不要把它的失败解释成源包损坏。

使用仓库根目录的 `PUBLIC_MIRROR_SHA256SUMS` 验证当前公共镜像文件。该校验单覆盖脱敏后的文件，不包含自身。

本文件、`PUBLIC_MIRROR_NOTICE_CN.md` 和 `PUBLIC_SOURCE_IDENTITY.json` 是公共交接控制文件；它们不属于 LN runtime 资料，也不授予资料批准或运行授权。
