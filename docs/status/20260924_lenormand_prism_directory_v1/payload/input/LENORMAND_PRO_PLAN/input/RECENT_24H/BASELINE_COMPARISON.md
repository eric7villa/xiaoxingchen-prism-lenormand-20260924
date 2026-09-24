# B 雷诺曼：基线与候选逐字节比较

状态：DESIGNED_NOT_IMPLEMENTED / DESIGN_CANDIDATE_NOT_AUTHORIZED。仅 B 专项；不修改 A，不宣布 S03 完成。所有路径相对于输入包 `ASTRA_B_LENORMAND_DEEP_20260922/`，输出不包含历史项目源码。

## 1. 本次实际核验

输入附件实际文件为 `bc5a3301-cc08-4dbb-b580-8f21f45d2b2a.zip`，SHA-256 为 `4626f0e759c597ed5c4ccb75495dfdf270e251b63fe4438885a80d2794b6e39a`。归档内 1183 个文件，安全路径、重复成员、符号链接及 CRC 检查通过；执行包内已审阅的标准库 `VERIFY_PACKAGE.py` 返回 PASS，核验 1183 文件和 5 组阅读索引。该 PASS 只描述传输与引用闭合。

`INPUT_VERIFICATION.json` 记录本轮重验：S00 输入身份 1097 条全部重绑（base 1060、restart 37），base 收件索引 1057 条通过；两个快照共 663 个文件（main 271、D 392）与包内身份一致。`checkpoint/` 共 58 个文件冻结未改。S00 原 ZIP SHA-256 为 `4a984afd864aa69fab15a42542a8f665e5d8f5b83c241559add59481e80748bd`，28 成员及其封存清单通过。原 V2 ZIP SHA-256 为 `455e9f065c2ee6f1bcc51fb2f804d4380921ab0815735f72bc9e7b445abc55d9`，1060 个文件与 base 逐字节一致，其中 1 个旧 ZIP 文件名按 CP437→UTF-8 恢复后比较。恢复仅用于比较名称，未改原 ZIP。

没有 `.git` 对象、活仓工作树或远端访问；因此只确认包内快照与已提供 commit 身份绑定，**不声称独立取得 Git 对象并证明提交真实性，也不刷新 CI、合并或生产状态**。资料原件身份、批准、可运行性不由 hash 通过推导。

## 2. 四个面，不拼成第五棵上线树

| 面 | 绑定身份 | 本包定位 | 可证明与不可证明 |
|---|---|---|---|
| 主参考 M | `ecdfb895fcbbc3f80cc97269388bc0111bc999e0` | `base/baseline/main/` | 271 个已选文件；未含 LN runtime，不能由此推断线上无任何 LN 服务 |
| D 集成候选 | `dfbb7474a664c6c40feb66ef61eb21099b28ecc9` | `base/baseline/d_candidate/` | 392 个已选文件，含 LN 工程骨架、demo、Tarot stages；存在文件不等于接通 |
| LN 独立候选 L | `fad82e44ae79587adee1f5e3de1c3e4830857698`；声明 base=`6613728c256276482c9d61147f0d48beb7202a54` | `ln_candidate/` 的 15 文件 | 仅变更候选选择集，依赖必须回查 D；不是第三个完整主基线；NOT_APPLIED |
| DS 后续 LN 补丁 P | 声明目标 D；无本轮应用 | `base/candidates/DS_INTEGRATED/patches/0002-lenormand-port.patch` | 对 D 的文本上下文及内存重建 hash 可核；并未应用、执行或合并 |

M/D 的并集为 392 个相对路径：250 个相同、21 个修改、121 个 D 独有。完整逐文件 SHA-256 见 `MAIN_D_FILE_DIFFS.json`。LN 15 文件相对 D 为 **7 修改、3 新增、5 相同**，见 `CANDIDATE_FILE_DIFFS.json`。

修改：`__init__.py`、`contracts.py`、`evidence.py`、`output.py`、`relations.py`、`runtime.py` 和 `tests/sprint48/lenormand/test_ds08_lenormand_runtime.py`。新增：`layout_candidates.py`、`test_ds_lenormand_admission_hardening.py`、`test_ds_lenormand_layout_candidates.py`。相同：`cross_system.py`、`layout.py`、测试 `__init__.py` 及 DS07 两账本。

## 3. 候选增量的准确含义

D 的 LN 准入只具备较早的卡系、全成员覆盖等工程条件。L 新增角色/目的/scope/投影收窄、牌表绑定状态、未知关系显式拒绝、未授权解释门和输出泄漏检查，且五九牌几何单独保存、默认关闭。不能把 D 的旧准入结论泛化成 L 未修复，也不能把 L 的文件存在归功于 D 已实施。

L 的 `LenormandAdmissionPolicy` 默认为不绑定 projection/snapshot，`allowed_relation_kinds=None` 在 `admit_relation_evidence` 中表示允许所有已知关系；`CoreEvidenceGate.is_open` 只检查核心条目非空。`LenormandRuntime.prepare` 记录 UNBOUND 牌表状态，却不把它传进开门条件。结论是 **静态可达的候选合同缺口**；本轮没有运行探针，不宣称生产可利用漏洞。对应 SPEC 的受权消费设计。

L 已正确把辅助角色与建立核心分开；`RetrievalResult` 自身拒绝非 ACTIVE 条目，因此不能再写“任意 HOLD 条目只要字段齐就能走正常 Pydantic 结果进门”。真正剩余问题是调用方构造的 ACTIVE/CORE 布尔值不是独立批准证明，以及门未消费完整来源绑定。

## 4. 补丁核验与不能继承的测试数字

本轮以标准库解析 unified diff，只在内存核对 D 上下文及计算结果 hash，不把重建代码写进任何基线。`LENORMAND.diff` 9 个文件的上下文均匹配 D，重建结果均与 L 对应文件一致。DS `0002` 10 个文件的上下文均匹配 D；其中复用了 L 增量，另增加输出修订与 1 个新测试文件。详见 `PATCH_INSPECTION.json`。

P 的 `output.py` 结果 SHA-256 为 `790f7d1b8fcc01208407db59e10740fd128c1b8ea2db1f12ba30dd9a54d8d816`，L 为 `97c192d3204686ac32982496678ee66c0f954342cef37a637ac76b201e1cb76b`。P 增加键和值扫描、大小写折叠、纯字母 ID 边界匹配及粘连 hash 检查；差异见 `DS_OUTPUT_DELTA_REVIEW.txt`。这些只是未应用补丁里的实现，不能写成当前 D/L 已修。

**合流特别注意**：L 的旧测试 `test_ds08_lenormand_runtime.py:118` 绑定 `domain/reading.py` 哈希 `1ff24750a6f07b66fe9cd531fefee910a7fd7b7671cb1247927ab84e91eff1da`，D 同行绑定 `4fad63f8cb8fdc5bef38a72758e0d791451b0edffcc41ea1dcf0319c30cf5ac3`。该单行差异不在上述两个补丁中。选择 L 文件或 P 补丁两条实施路线时必须明确保留哪一目标树的身份断言，按实际 bytes 重绑；不是删除断言，不是修改生产域以迁就旧测试。

历史 153/164 等是作者报告；本轮全部产品测试为 NOT_RUN。文本上下文匹配不等价于 `git apply --check`、测试通过、合并成功或语义批准。

## 5. 现状判别，不夸大缺口

- **CONFIRMED**：D `demo/catalog.py:60–68` 已有关闭的 `ln-three` slug。因此“整个包没有任何 LN slug”是 FALSE；“缺已批准的 LayoutMode↔slug 及来源方法绑定”仍成立。
- **CONFIRMED**：L 的 `LenormandDeckCatalog` 仅 `catalog_id/contains`，非空对象即被标记 BOUND；`StaticDeckCatalog` 明言 synthetic。故该状态名不能当批准证明。
- **CONFIRMED**：D `mcp/postgres_tools.py` 返回 `PublicRetrievalResult`；L `LenormandEvidencePort.retrieve` 需要 `RetrievalResult`，不能直接互接。公共投影剥离权限字段是有意边界，不应撤销。
- **CONFIRMED**：L 的关系解释校验函数当前恒拒，且 `prepare` 不调用它。存在防线函数不等于实际核心路径受它支配。
- **PARTIALLY_TRUE**：历史“scope 已收窄”在显式参数给出时成立；None 的含义与调用链完整性仍需收紧。`NOT_STATED` 在当前 EvidenceItem 合同只准 Mentor scenario，不应给 LN 新增同义状态来绕路。
- **UNVERIFIED**：两书原件/批准条目数量、真实数据库角色、线上路由、五九牌语义与现网行为。未知数量保持 null，不写 0。

## 6. 合流建议

推荐 Codex 在未来授权批次以实际选定的目标提交为唯一实施底座，先核当前字节，再逐项取 L 的工程增量与 P 的输出修订；不整体覆盖 D，不复制旧测试数字。几何、授权消费、资料接入、输出、运行接线与五九牌开放分批。共享 contract 请求分别交 S02/S03/S04 主人，B 只提交候选设计。
