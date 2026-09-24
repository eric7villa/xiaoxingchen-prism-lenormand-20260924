# 新引擎 S02–S07 详细总计划

状态：DESIGN_CANDIDATE_READY_FOR_CODEX_REVIEW 的候选材料；最终封存结果以 STATE/CHECKS 为准。本轮只产生离线设计文件和归档，产品代码/资料批准/真实运行/CI/部署均未执行。

## 总体选择

复用既有 S01 的需求与缺口，B 的 Lenormand 专项图纸和 C 的资料候选/来源限制，不重做 S00/S01，也不重新挖掘 C。main 与 D 分别按固定提交绑定，D 未并入 main。只对指定历史误映射、13项schema差异以及实际消费链断点进行局部设计纠偏。

统一主链见 SPEC_CN 与 CROSS_SYSTEM_ADAPTERS：真实输入/三门/确认/authority → Tarot R1与有向R2 或 LN COMPOSE → 两通道真实研究 → 主判断与可控方案 → 隔离无工具审查 → 原子受控交付。资料批准、调用授权、开发许可和发布许可独立，任一存在都不自动授予其他许可。

## 可交付规模与入口

56项任务、22个单一owner接口、184条稳定需求记录和8项本批控制义务。根验收矩阵290条记录＝230条本轮独立正反用例＋44条复用B的成对对照记录＋16个浏览器场景；这些是设计，不是290次通过。六个模块各自检查点保留；所有原S01/B/C文件逐字节保留，输入完整ZIP亦随累计包保留。

| 目录/文件 | 用途 |
|---|---|
| SPEC_CN、CROSS_SYSTEM_ADAPTERS、HASH_CODEC_V2 | 系统行为、跨系调用和精确身份字节合同 |
| TASKS、tasks/ | 文件/符号级任务、原文/hash、主/D证据、正反命令、退出回滚 |
| INTERFACE_CONTRACTS | producer/consumer/字段/状态/权限失败、必要性、兼容与单一owner |
| DEPENDENCY_DAG、FILE_OWNERSHIP | 126条边、212条写路径、18条共享写面及profile排程 |
| REQUIREMENT_IMPLEMENTATION_TRACE | 每项需求的任务/验收或不需新行为理由，候选保持未批 |
| ACCEPTANCE_MATRIX、CICD_AND_RELEASE_PLAN | 分层验收、真实证据、CI/CD与回滚方案 |
| OWNER_DECISIONS、GAP_REGISTER | 真正待裁决和精确外部缺件，只冻结受影响部分 |
| prior/、checkpoints/、inputs/ | 原成果、模块冻结点与可移植固定输入 |

## 实施波次与责任

当前不执行以下波次。获单独许可后，先核真实origin/HEAD/dirty/AGENTS及任务scope；不能把本包快照当最新已合并树。进入波次前执行目标卡/反方卡与对应失败用例，记录实际红/绿而不是预先声称复现。

波次的正式并行表是 DEPENDENCY_DAG.profiles.*.parallel_waves。可读顺序为：安全入场/事实/确认合同及输入源身份 → approved reader/lifecycle与核心/LN支持 → frozen operation与Mentor多候选 → 两通道wire账本/可信宿主 → caller-chain及隔离审查/交付 → 新入口/session/公共结果 → 独立环境实测、人工语义与浏览器 → 最后才是另批发布。具体跨模块顺序服从DAG，不按阶段号码强行串行。

同文件由 FILE_OWNERSHIP.file_integration_owner 统一写入；task owner负责语义和审查，其他模块是贡献者，不同时改同一路径。TASKS.depends_on 是完整图的便捷并集，包含条件边；调度必须读 dependency_edges.kind/profiles，不能把所有候选功能当硬前置。每个profile仅保留所选系统/可选层边，并重新建立该profile的共享写面串行顺序。

## 最低可验收路径与后置项

Tarot最低路径需要已批准核心证据及至少一条真实批准Mentor，实际主链、真实研究规则、隔离审查、数据库控制及产品安全/浏览器验收。两个具名canary单独跟踪；旧60全验、281、全部BookT不是最低前置。缺少任何真实批准材料，只冻结相应语义验收/运行，纯工程仍可在明确synthetic scope推进。

LN最低路径使用批准36牌catalog与三牌方法/支持图；带同样的安全、保留期、研究与审查交付，不等Mentor、Tarot或五/九牌。五牌/九牌各自资料与方法批准，互不锁死；三牌无授权时只允许明确的结构预览，不能偷用Tarot解释。

可后置：完整BookT、Consultation Q-3、新24/旧48逐条人工批准、LN五/九、旧PHP同步、Site2/Card后续边界、发布启用。后置不等于删除需求，相关任务、接口、验收和解锁条件已给出。

## 后续授权实施的工作量估算

以下单位为人时，正常/保守两档；不是本次对话时间估计，不是日历交付承诺。假设熟悉代码的实施者、既有工具链可用、独立owner理想可用；排除等待审批、数据采集、配额、环境配置和缺失历史证据。关键路径按任务工时与DAG计算，未模拟同一人的多任务资源争用，不能直接除以团队人数作为发布日期。

| 范围 | 任务 | 总工作量正常/保守 | DAG关键路径工作时正常/保守 |
| MIN_TAROT | 41 | 448/850 | 198/372 |
| MIN_LN_THREE | 37 | 402/758 | 206/388 |
| FULL_DESIGN | 56 | 572/1086 | 206/388 |

MIN profile是完整最小验收设计工作，不包含 S05-T09 发布执行；所有profile实际运行状态仍NOT_RUN。FULL_DESIGN包含可后置功能的任务设计，不表示须一次部署所有功能。

## 本轮明确停线点

Consultation时点Q-3，以及实际研究grant的计量单位/物理wire预算数值需owner批准；推荐/备选已给，不全局等待。真实Provider离线协议资料、当前远端失败原始JUnit、生产环境/备份恢复/部署许可、已批准资料清单缺件按GAP逐项处理。不得把C的DONE、旧报告APPLIED、CI设计或固定hash变成相应批准。

当前先交Codex：核根overlay、56项写面、全部需求追踪、两系统最小图、安全正反、资料依赖隔离以及最终seal。Codex工程认可后，爸爸再按实施、数据、模型、环境、部署分别授予有限scope。到此停止；不自动开新会话、启动D/E、恢复Prism或实施任何任务。
