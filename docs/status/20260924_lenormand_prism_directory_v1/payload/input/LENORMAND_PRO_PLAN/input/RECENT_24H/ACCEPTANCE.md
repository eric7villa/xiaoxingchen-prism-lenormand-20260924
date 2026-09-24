# B 雷诺曼成对验收矩阵

全部用例 NOT_RUN。正控不授予资料批准或运行许可。

每行有好例/坏例，NOT_RUN 指未来测试符号未执行；归档等价检查另记 CHECKS，不能由此宣布产品测试通过。synthetic 只证明结构与权限行为，不证明牌义或真实审批。凡必要门失败，后续模型/研究/写入调用计数应为零；可选层不足只隔离相关主张。命令引用未来新增或改造文件，不是本轮可运行指令。

|ID / 任务|有效正控与过挡对照|真正反例|预期观察|前提|
|---|---|---|---|---|
|AC-B-01 / B-LN-T00|D字节/实际导入根匹配，L/P逐文件登记|用M缺包推断D缺包或导入别的worktree|停止坏批，不修改源码凑hash|另批离线测试；身份核对可读当前包|
|AC-B-02 / B-LN-T00|DS08 hash按实际target审阅重绑|照抄L旧hash或删除断言|差异可追溯，不继承历史测试数|真实目标worktree|
|AC-B-03 / B-LN-T01|三唯一卡和合法排列/显示槽|缺牌/重复/orientation=null/未知键|正控仅结构通过，坏例不补牌，模型0|SYNTHETIC_OFFLINE_ONLY|
|AC-B-04 / B-LN-T01|数组与显示顺序不同但映射明确确认|按数组擅改显示关系或猜slot别名|按规范显示槽组装且保留原事实|synthetic|
|AC-B-05 / B-LN-T01|A→B/B→C，整线与全集分开|B→A冒A→B或ID与members矛盾|区分方向；非法ID拒绝，不生牌义|synthetic|
|AC-B-06 / B-LN-T02|private保身份/public去标识|从public内容反造批准身份|仅单向投影，伪造不能开门|IR-B-LN-01接受；synthetic|
|AC-B-07 / B-LN-T02|release=projection且query/snapshot/hash全一致|只匹配一项或内容hash错|必要绑定全部验证，错非正常no-match|synthetic binding|
|AC-B-08 / B-LN-T03|PG受限角色读批准链完整LN项|MCP读raw/governance或跨Tarot|只读正确结果；越权SQL拒绝无泄漏|临时PG17/角色/迁移另批；NOT_RUN|
|AC-B-09 / B-LN-T03|空ACTIVE快照存在与快照缺失分别返回|零行一律NO_SNAPSHOT或缓存伪ACTIVE|区分NO_LAYER_MATCH/NO_SNAPSHOT与八段过滤|临时PG17|
|AC-B-10 / B-LN-T03|candidate/hash/源版/审批都相符|内容或scope改后复用旧批准|坏例完整性拒绝，生成/交付0|PG17授权测试治理fixture|
|AC-B-11 / B-LN-T03|prepare到交付依赖release有效|prepare后SUPERSEDED被幂等pin掩盖|提交前复核，坏例停而非换snapshot续跑|PG17双连接并发|
|AC-B-12 / B-LN-T03|无关可选来源撤回主干独立且重审|必要目录/方法撤回仍输出原核心|按实际影响面隔离，必要源失效关当次语义|PG17+依赖fixture|
|AC-B-13 / B-LN-T04|36唯一目录和单值别名且来源绑定|35/37/重复/冲突别名或StaticCatalog自授权|结构/授权分开，坏例不能生产BOUND|synthetic工程；真实目录SOURCE_BLOCKED|
|AC-B-14 / B-LN-T04|目录缺失仍允许三槽结构预览|已知目录未知牌退成UNBOUND绕过|缺目录不判牌非法但门闭，真未知ref拒绝|synthetic|
|AC-B-15 / B-LN-T04|新条件词保留candidate待映射|删条件改GLOBAL或synthetic标AUTHOR_TEXT|保信息不批准，绑定完整候选内容|synthetic profile；原文SOURCE_BLOCKED|
|AC-B-16 / B-LN-T05|全受信绑定/目录/方法/三成员支持|非空core或UNBOUND就放行|正控fixture模拟调用1，坏例模型0|synthetic端口；真实运行另批|
|AC-B-17 / B-LN-T05|明确注册关系集合且方法许可|None无限类型或未知关系偷渡核心|未知可选局部隔离不全关，核心不可依赖|synthetic|
|AC-B-18 / B-LN-T05|未知domain可用明确GLOBAL资料|None吞入不明SCOPED资料|保留GLOBAL，仅暂停缺条件主张|synthetic；不改Mentor NOT_STATED|
|AC-B-19 / B-LN-T05|无cards获准方法+三卡分别核心支持|单卡词并集/方法顶核心/仅A+B|区分方法与成员，整组不全不生成|synthetic规则；原书语义SOURCE_BLOCKED|
|AC-B-20 / B-LN-T05|重复去重保出处，互补按主张联合|冲突按item_order/作者投票强选|冲突阻相关必要主张，不静默优先级|synthetic支持图|
|AC-B-21 / B-LN-T05|已准Matthews主干全，Rana可选无匹配|Rana替缺主干或强求每item双作者|不抬补充权/不过挡；具体开放等批准|synthetic；OD-F-01 / OD-F-04|
|AC-B-22 / B-LN-T05|预算内补检拿到必要方法/成员|truncated只一hit开整组或无限重试|确认覆盖；不足明示无获准证据|synthetic repository spy|
|AC-B-23 / B-LN-T06|自然提用户牌无私有身份的判断|card_ref作键词典/混main_judgment|好例过；坏例helper与final都拒|synthetic|
|AC-B-24 / B-LN-T06|普通intent/within，无私有引用|键/值/列表嵌长ID/变大小写/嵌hash|普通词不过挡；泄漏拒绝不简单替换放行|synthetic；P差异重绑|
|AC-B-25 / B-LN-T06|中文正常叙述，短ID未作身份公开|短ID以明确内部字段/引用泄漏|结构映射+边界检查，不子串全禁|synthetic bilingual|
|AC-B-26 / B-LN-T06|预算未知待确认，保留用户两周事实|自由文本编经历或作者案例当用户|结构合格仍审主张/事实，坏例不交付|synthetic reviewer spy；真质量另批|
|AC-B-27 / B-LN-T07|LN受信资料展示文字含workplace/replacement|TAROT/WAITE_RWS用中性描述伪装|好词不误挡，typed体系错拒绝|synthetic|
|AC-B-28 / B-LN-T07|未解析来源留review不入核心|删除身份门来修黑名单过挡|缺身份仅阻受权消费，禁止跨系统兜底|synthetic|
|AC-B-29 / B-LN-T08|LN适配只复用预算/时钟/安全机制|TarotStageExecutor/RWS/固定R1-R4职责|独立LN编排，默认factory仍关闭|IR-B-LN-05；synthetic端口|
|AC-B-30 / B-LN-T08|无网络明确未研究而可核用户事实|provider-off称已查无解或偷偷联网|研究调用0，disabled/failed/no_solution分开|synthetic research spy|
|AC-B-31 / B-LN-T08|有效当次authority/用户议题/inputdigest|过期/撤权/换人沿用旧支持或改输入交付|复核阻断，不重签/不复活终态|共享合同+spy；真库另批|
|AC-B-32 / B-LN-T08|普通关系议题遵守既有安全边界|仅情感词全拒或牌面推断未说危机|真实议题门区分，不读画像/编事实|既有安全回归fixture|
|AC-B-33 / B-LN-T09|五标签四邻接两翼覆盖正确|缺邻接/重复越界槽/截前三张|正控结构过仍关闭，坏例精确拒绝|synthetic five geometry|
|AC-B-34 / B-LN-T09|中轴与两翼联合且非中轴可反证|中心唯一或重复关系充参与次数|计数不等于语义，禁止虚构百分比|synthetic支持图；作者语义SOURCE_BLOCKED|
|AC-B-35 / B-LN-T09|缺可选镜像方法保留四邻接主干|自动镜像/时间因果/本站标签当作者认可|可选不足不全停，缺授权不生语义|synthetic；未源许可|
|AC-B-36 / B-LN-T10|3x3完整12正交边三行三列|(0,4)/(2,3)/(0,8)被标正交|坐标规则覆盖一步对角/跨行/远角|synthetic nine geometry|
|AC-B-37 / B-LN-T10|ring无向集合、外围可限制中心|tuple顺序当顺时针因果链或中心独断|几何不赋义，参与计数不证明权重|synthetic|
|AC-B-38 / B-LN-T10|非对角主干全且无对角许可|对角单独开门或priority改2假装核心|对角仅辅助，缺对角不一刀切|synthetic支持图；方法另批|
|AC-B-39 / B-LN-T10|候选仅测试导入registry关闭|改import写法/动态entrypoint或flag绕局部检查|全src引用+默认拒绝；不宣称静态万能|另批测试；完整目标src|
|AC-B-40 / B-LN-T11|未来单独五牌授权并全前提满足|五牌授权连开九牌或checkpoint当授权|模式独立，当前全部默认关|OD-F-02 / OD-F-03 / OD-F-05及真实源/DB/运行；当前BLOCKED|
|AC-B-41 / B-LN-T11|未来九牌非对角准、对角仍关闭|flag=true越源/目录/运行门或减牌|必要条件缺一不可，可选对角不强开|未来授权；当前BLOCKED|
|AC-B-42 / B-LN-T12|结果逐条记实际scope/NOT_RUN/receipt|历史CI数当本轮PASS或删坏例只留好例|无环境不伪绿，证据分类准确|CI设计/另批执行|
|AC-B-43 / B-LN-T12|写集闭合public不泄漏默认provider-off|改A/原输入/建shadow审批/CI联网部署|越界阻断，回滚仅撤本任务增量|目标diff+CI配置另批测试|
|AC-B-44 / B-LN-T12|manifest排自身/校验单，校验覆盖载荷+manifest|hash自引用/ZIP缺多项/CRC或hash错|重开ZIP逐成员闭合；传输PASS不等产品PASS|标准库归档检查本轮可做；产品测试NOT_RUN|

每行的精确候选测试文件、符号与 NOT_RUN 命令见 ACCEPTANCE.json。
