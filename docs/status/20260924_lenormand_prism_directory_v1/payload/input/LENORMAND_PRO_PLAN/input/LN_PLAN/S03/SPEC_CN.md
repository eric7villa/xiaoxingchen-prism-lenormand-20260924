# S03 数据、可选知识与雷诺曼专项完整设计候选

状态：DESIGNED_NOT_IMPLEMENTED；不挖掘、不批准、不入库。S01、B、C 原字节在 prior/ 原样保留，修订仅在本阶段设计及总计划。B 13任务/44组对控逐项复用见 B_REUSE_MAP/B_ACCEPTANCE_REUSED；不重复制造牌义或审批体系。

## 1. 唯一权威和流向

原件→SourceVersion→有坐标的提取视图→规范化→Candidate→REVIEW_REQUIRED→既有用户批准→APPROVED_PROJECTION→INDEXED→ACTIVE 是受控链。HOLD回审、REJECTED/SUPERSEDED终态及具体迁移按现有生命周期合同；转换成功、作者DONE、模型一致、synthetic或目录非空均无批准效力。任何内容、scope、方法或候选hash变更产生新版本重审，旧审批不继承。

受信SQL私有读模型仅派生既有release/items/candidate/review/user_approvals事实。projection_id即release_id，snapshot只是绑定这个既有快照的用语，不添同义表。公开MCP维持旧白名单，不允许从public文本反推ID。S03定义语义/过滤合同；S05负责SQL/角色/锁；S02负责模型调用前及交付前再验证，解决pin后撤回。

快照存在与条目是否命中分开。公开仅NO_SNAPSHOT、NO_LAYER_MATCH、NO_APPROVED_EVIDENCE、DISABLED_PROVIDER_OFF。错误hash/越权/数据库故障走受控失败，不伪无命中。系统→牌阵→用途/opaque hint→牌/方向→域/情景→lifecycle→layer→全文八段保持顺序，内存与SQL做parity。召回不是语义准入；unknown domain不让所有SCOPED自动通过，但明确GLOBAL仍可用。

## 2. 来源坐标与治理适配

C原始declared hash、实际脱敏view hash、JSON容器hash、解码content hash和切片hash不可混同。全部坐标声明UTF8_BYTES_HALF_OPEN及独立source/version；离散引文是spans[]，不能用首尾包一个未提供连续段。CRLF/BOM/空白规则保留raw与view双hash和映射；正常化的匹配只证明该规则下片段相符，不证明整个原始文件已在场。

PDF/EPUB/DOCX/Vault/转写仅规划格式适配。ASR局部不确定保原字、定位、原因和待读范围；缺图像不能捏造图意、像素、方向或时间。schema草案是描述模板，不能直接当实例/执行约束。

## 3. 13项差异的确定设计取舍

SCHEMA_RESOLUTION.json逐条继承RF原文锚点，目标为候选V2兼容层：调度数字统一命名空间且不具语义权；修辞替代解释明确路径；上下文失败保留局部队列；句法单值与语用数组分轴；mechanism显式别名；阶段hint由S02解释；721材料池只对指定来源；老师/用户校准/模型/外部/审批物理分层；缺技能与扫描证据保持历史报告；整理源不冒原始；非语义辅助不采用即无安装依赖；五态null与方向UNSPECIFIED独立；探针缺录音不猜事实。任何别名双值冲突停止该条映射，不静默覆盖。

six rhetoric axes、完整因果八槽、分支/适用/反例/迁移界限均保留。没有某槽不能凭模型补原话；有明确因果链也不因缺某英文键被语义否决。可执行schema的版本化、roundtrip、字段差异测试是未来任务；本轮没有修改原schema或三族candidate。

## 4. Mentor最小可靠消费

现D consumer._outcome用matched_results[0]，多条只加trace；这一静态结构不足以兑现多候选语义，改为V2 packet集合和五关系。单条完整仍有效，多条没有投票权。重复去冗余不删出处；互补联合需各自前提；缺条件/上下文局部等待；真实冲突送S02，不按老师/出现次数/输入顺序选赢家。

IC-04 seed来自R1+象征+可空Book T，不来自最后R2现象，解决循环。机制ref必须通过受权registry及可回查映射；模型自由文本不能注册权威。当前来源not-stated不默认ANY或正位。CARD逐卡/方向/域/情景/机制/前提AND；GLOBAL独立方法，只允许明确无牌依赖，不给某张牌补义。两个具名旧目标UPRIGHT_ONLY仅锁目标，不锁所有魔术师/宝剑5课程。

## 5. C成果复用和局部等待

本包C共88候选：旧60、新24、师姐四条（来源两篇），作者40DONE/48PENDING。此数是复审账，不是批准或产品通过数。新24候选与C原输入59046字节hash一致，原始完整TXT见证仍有缺口；与S01旧时“本包未带候选字节”的时点不同，应追加新事实而非篡改旧检查点。

C_DATA_QUEUE保留旧48精确ID和原有source_binding/next actions，未重复挖掘。新旧亲密关系、工作发展、人生阶段、代价/退出专项后续实样必须读完整来源，不从本设计摘要造牌义。师姐NOT_STATED/ASR/缺图独立队列；没有此前双模型初稿则不声称双模型复核。

最小真实Mentor能力至少一个明确获准、机制适用可验证的目标；两具名canary作为专项持续待验。无依赖工程不等旧60/新24/281全部完成。每项真正数据批准由爸爸另批，不由本计划生成。

## 6. Book T不是核心门

复用D admission/consumer路径，补内部身份及S02调用者。普通/四牌分支明确scope，不能混表。R1核心完整、Book T无获准结果时继续；真核心冲突回R1。by_content只用文本hash归并会把相同文字不同身份/范围折叠，未来用复合item/candidate/source键。每项必须SUPPLEMENT_ONLY、不得建立/覆盖core、不可暴露内部标签；普通生活词不因子串误挡。G04 synthetic只验形状不能证明真实课程批准。

## 7. LN三牌最小路径（B合同吸收）

用户三张/实际draw order/明确显示槽→结构几何→获准36目录→分别检索core与method→私有绑定及scope→全组支持图→受控模型→现实研究/独立审查→受控交付。最后三步属S02/S04/S05。不能调用TarotStageExecutor并改名，不能沿RWS/Place/R1-R4解释LN。

目录存在对象不等BOUND；无目录仅结构，有目录未知ref真拒绝不可回退UNBOUND。方法profile的顺序/arity/kind/条件/反例必须真实获准，GLOBAL方法不必绑卡。主张图要含有序整线、两邻接与每成员core的适用支持，不是把三单词拼起来；方法本身也不能替代卡核心。

Matthews结构主干与Rana补充各按实际批准范围消费。无Rana不强求双作者；有Rana不补缺主干。结构非空、计数、模型调用spy成功均不证明作者语义。`require_relation_interpretation_authority`当前恒拒的保护只能在完整权威判定替代后解除，不能先删掉再补证据。

## 8. LN五九牌独立候选

完整几何沿prior/B_LENORMAND/FIVE_NINE_CANDIDATE.md不重写作者规则。五槽为本站现状/助力/阻力兼中轴/隐藏变量/建议，四邻接，两翼能反证中轴；参与数不当语义权重，不新增镜像/时间线。九牌3x3中心4/周围无向集合/三行三列为主干，对角辅助不能单独建立或推翻核心。坐标共享边按曼哈顿距离1，行末跨行和一步对角均非共享边。没有对角方法不全关完整主干。

五/九独立工程与独立资料/运行批准，默认全部关闭。候选模块被测试导入、CI绿、flag=true均不能开放。用户给九张不允许缩成三张。真实入口默认拒绝与完整静态引用检查互补，静态扫描不声称能证明所有动态加载不可达。

## 9. 退出与回滚

新增消费者失败回到关闭受权语义/仅结构预览；不得恢复旧fail-open简化门。撤回任一必要目录/方法/core阻对应当次主张与交付。撤回无关或可空补充可重建独立链并重审，但绝不偷偷换snapshot继续旧工件。保留源、候选、审批和旧工件，不复活SUPERSEDED。所有测试命令为未来授权执行，当前NOT_RUN。
