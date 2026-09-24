# Prism 读取顺序

1. `README_CN.md`
2. `DIRECTORY_EXTRACTION_INDEX.json`
3. `payload/COVERAGE_AUDIT_CN.md`、`payload/MATERIAL_COVERAGE.json`、`payload/MISSING_MATERIALS.json`
4. `payload/PROMPT_CN.md`
5. `payload/input/LENORMAND_PRO_PLAN/`（若存在）
6. `payload/input/ASTRA_RETURNS_7/ASTRA_FINAL_ADJUDICATION/attempt_001/README_CN.md`、`FINAL_VERDICT.md`、`DOUBAO_ALIGNMENT_INTEGRATION.md`、`SOURCE_REQUESTS_FINAL.json`
7. 只有任务需要时再读取对应的 `payload/input/ASTRA_RETURNS_7/...` 原始证据；不读取无关 Tarot/Mentor 资料作为 LN 语义。

五项协议：可观察信息、可控制动作、不可用信息/权限、成功量词、最坏失败构造。
