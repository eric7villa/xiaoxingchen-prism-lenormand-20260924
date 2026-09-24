# 局部待裁决与独立批准门

完整机读字段在同名JSON。工程推荐不是裁决，也不赋予运行权限。

## OD-01 Consultation Q-3准确时点

推荐：研究双通道达到真实终态并完成claim适用审查后，在最终R3建议封存前匹配已批准Consultation方法。

备选：R1/R2一致后可仅准备匹配，但方法结论不得成为搜索前提；正式建议仍在研究终态后合并。

理由：避免可选方法预设现实结论；保持核心先行及研究不可被方法代替。

暂行：可选调用关闭，R1/R2→真实研究→R3/R4主链继续。

只影响：S04-T06。解锁：爸爸明确所选时点/范围；具体方法来源另行批准；通过对应正反测试。

## OD-02 logical search/fetch与physical wire计量及数值授权

推荐：新grant显式声明logical SEARCH_FETCH_TRANSACTION上限，同时分别绑定physical wire、fetch、成本及deadline上限；COMM/LEVERAGE共用同reading账本，两个通道分别可重试不复制总额度。

备选：保持逐wire计量，但Tavily的search与每次fetch各计一次，需用新scope重新批准对应额度；不能把旧每leg额度静默扩成更多请求。

理由：现有per-leg reserve和worker retry不是同粒度；身份与真实出站结算必须统一。

暂行：可实现/测试纯离线账本和拒绝路径；无有效单位/数值/profile则不允许真实出站。

只影响：S04-T02, S04-T03, S04-T04, S05-T04, S04-T07。解锁：版本化运行grant明确单位、数值、最大fetch数量/字节、成本、总时长与重试；真实Provider契约离线资料核验后单独批准运行。

## 不应伪装成架构未决项的事实缺口

已批准资料roster、真实Provider契约/受限profile、现行环境/恢复/部署权限、缺失旧JUnit与PHP当前源码都是独立证据/批准门，具体影响面见JSON和GAP_REGISTER。正文缺件或未批准不要求所有工程等待。旧48每项在S03/C_DATA_QUEUE；不开新的资料任务或模型会话。本轮未批准数据、方案实施或上线。
