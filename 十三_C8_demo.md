# C8 早期验证物（Proof of Capability）

> 这不是计划，是已经能打开、能跑的东西。
> 每一项都给出路径与验证命令；不能验证的，明确写"未完成"。

## 1. 可运行仓库：kstar-os

| 项 | 值 |
|---|---|
| 路径 | `C5交付包/repo/kstar-os/` |
| 规模 | 380 行 CLI + 6 个技能 + 9 个测试 |
| 许可 | MIT |
| 提交 | 12 |

验证：

```bash
cd C5交付包/repo/kstar-os
python3 -m unittest discover -s tests -v    # 9/9 OK，5.2s
python3 scripts/kstar.py status             # 五层状态
python3 -m http.server 8000                 # 打开 /web/
```

**它证明了什么**：Agent 的五层架构可运行，技能可调用，数据可积累。
**它没证明什么**：没有真实学生长期使用。

## 2. 数据管线：C6A 提交仪表盘

| 项 | 值 |
|---|---|
| 路径 | `C6A交付包/` |
| 真实数据 | 18 条评审 / 11 名学生 / 8 个挑战 |
| Excel | 7 Sheet，21,780 B |
| 网页 | 单文件 58 KB，离线可用 |
| 扫描器 | 对 `D:/ai+x` 扫出 2 条记录，2 秒内完成 |

验证：

```bash
cd C6A交付包
python3 scripts/parse_reviews.py            # records=18 students=11
python3 scripts/build_excel.py              # 生成 xlsx
python3 scripts/scan_submissions.py D:/ai+x --out data/self_scan.json
```

**它证明了什么**：非结构化文本 → 结构化数据 → 双端展示的完整管线。
**它没证明什么**：没有在全班真实提交目录上跑过。

## 3. 可运行 Web 入口：KSTAR 助手

| 项 | 值 |
|---|---|
| 路径 | `C5交付包/repo/kstar-os/web/index.html` |
| 验证 | Playwright 1440×1000 与 390×844 截图 |
| 无 Key | 检索 + 模板计划可用 |
| 有 Key | 调用 OpenAI 兼容接口生成计划 |

**它证明了什么**：学生可用界面已经存在，不是线框图。
**它没证明什么**：未部署（等 token），没有真实 AI 调用截图。

## 4. 单元卡片（本 Proposal 的新增物）

| 文件 | 状态 |
|---|---|
| `units/unit-card-template.md` | ✅ 模板 |
| `units/unit-c4c.md` | ✅ 完整单元（90 分钟） |
| `units/unit-c6a.md` | ✅ 完整单元（120 分钟） |
| `units/check_unit.py` | ✅ 两个单元检查通过 |

验证：

```bash
cd C8交付包
python3 units/check_unit.py units/unit-c4c.md units/unit-c6a.md
# [OK] [OK]
```

**它证明了什么**：Syllabus → Content 这一段已经有可检查的结构，不是 PPT 里的流程图。

## 5. 技能样例

| 技能 | 路径 | 真实验证 |
|---|---|---|
| submission-audit | `C10交付包/agent-os/memory/L3_skills/submission-audit/` | 对 C10、C6A 实际运行 |
| dashboard-build | 同上 | 生成 C6A 仪表盘，修过一次排序 bug |
| repo-release | 同上 | 对 kstar-os 跑发布检查 |
| content-outline | 同上 | 用于 C7 两篇文章 |

**它证明了什么**：技能不是空壳，有使用记录与迭代。

## 6. 缺口清单（不掩盖）

| 缺口 | 为什么重要 | 何时补 |
|---|---|---|
| 没有真实学生试用 | 可用性无法证明 | Week 8 |
| 未部署上线 | 交付页只有本地版 | token 到位 |
| 没有教师评审 | 内容覆盖度未验证 | Week 2 |
| 只有 2 个单元 | 不能证明"可复用" | Week 1–2 扩到 4 个 |
| 没有对照基线 | 效率提升无法量化 | Week 8 计时对比 |

## 7. 一句话

> 这份验证物里，**代码能跑、检查能过、数据能对上**；
> 缺的是"人用过"的证据——这正是 C8 执行阶段要补的，而不是 Proposal 阶段能编的。
