# 交给当前 Codex 的累计详细设计包

先读 MASTER_PLAN_CN.md → SPEC_CN.md → NORMALIZATION_OVERLAY.json → TASKS/INTERFACE_CONTRACTS/DEPENDENCY_DAG/ACCEPTANCE_MATRIX。逐任务 JSON是精确metadata，Markdown为可读展开。根STATE/CHECKS是本轮最终状态；模块STATE是当时冻结状态；prior中的旧PARTIAL/COMPLETE不被本轮改写。

本包根文件为当前统一设计候选。S02–S07模块ZIP各自可恢复到完成当时；后续根overlay才是统一后的调用/测试路径/依赖版本。不得只读取某个模块旧字段而忽略IC-05联合型、test_发现命名、单store及LN最小安全闭合纠偏。

## 输入重建与验证

inputs/ASTRA_A_FINISH_ALL_20260922.zip 是收到的完整原包；先核 INPUT_BINDINGS.input_archive 的字节数/SHA，再安全解包到独立临时目录。其inputs/A_DISPATCH.zip、B_DISPATCH.zip、C_DISPATCH.zip分别解到独立子目录；拒绝绝对/逃逸/重复/symlink，原UTF8中文名未标记时仅无损解码原名字节，不改变正文。路径标签由INPUT_BINDINGS.portable_reconstruction映射，不依赖本轮<external-source-path><local-path>

新根的 `VERIFY_FINAL_PLAN.py --root <解包后A_FINAL_PLAN>` 仅做标准库文件/结构/manifest/模块ZIP检查；不导入产品。`--source-roots <映射JSON>` 可另核source anchors和prior原字节。执行前仍应审读该文件。最终外部ZIP回执/SHA供传输独立校验；包内manifest按规则排除自身与根SHA256SUMS，checksum包含manifest及全部载荷。

prior/A_S01_RECONCILED、prior/B_LENORMAND、prior/C_MENTOR_DATA是原样保留成果，绝非本轮批准。原输入原样留存是为了按需重建/复核，不要求重新做S00/S01/B/C清点或语义挖掘。

## 接收审核清单

先核封存，再核主体/原文绑定；重点审R2机制时序、LN独立原点、Mentor五类策略与两个具名UPRIGHT_ONLY范围、13schema修订兼容、真实wire预算/回执、最小权限与事务撤回、隔离PG/CI证据、新入口confirm/run及两个最小profile。每个硬门必须看正例、反例和误挡，不能只看“fail closed”。

真正待裁决在OWNER_DECISIONS；精确外部/历史缺口在GAP_REGISTER与C_DATA_QUEUE。最小真实语义依赖未批准时可以独立推进无依赖工程，但不能用mock代替批准。全部测试命令NOT_RUN，本包不是启动实施的命令。

本轮到当前Codex审核为止。不得自动进入代码实施、数据入库/批准、模型调用、CI/DB/部署，也不创建D/E或新会话、不恢复旧Prism。后续需要爸爸分面授权scope后才执行对应任务。
