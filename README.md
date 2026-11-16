# C8 交付包 · 真实项目落地（Project C Proposal）

## 文件

```
C8交付包/
├── README.md
├── 十三_C8_proposal.md        ← 5 部分 Proposal（项目选择/拿来主义/KSTAR/角色/验证）
├── 十三_C8_demo.md            ← 早期验证物清单（5 项，附验证命令）
├── 十三_C8_AAR_W0.md         ← W0 复盘（R̂ vs R）
├── 十三_C8_AI日志.md
├── 十三_C8_拿来说明.md
└── units/
    ├── unit-card-template.md  ← 单元卡片模板
    ├── unit-c4c.md            ← 完整单元（90 分钟）
    ├── unit-c6a.md            ← 完整单元（120 分钟）
    └── check_unit.py          ← 卡片检查器（两个单元均通过）
```

## 一句话

选 Project C（课程生产体系），因为 C1–C10 已经把它的四个零件各做了一遍；Proposal 的 70% 在可运行的 `kstar-os`、`C6A 仪表盘`、`KSTAR 助手` 与两张单元卡片里。

## 验证

```bash
python3 units/check_unit.py units/unit-c4c.md units/unit-c6a.md
# [OK] [OK]
```

## 诚实边界

- 未入选，未开始 8 周执行。
- 没有教师评审、没有学生试用、未部署。
- 单元卡片只有 2 张，不足以证明"可复用"。
