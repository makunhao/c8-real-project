#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查单元卡片是否达到"可教"的最低标准。

用法：python3 check_unit.py units/*.md
退出码 1 = 有单元不合格。
"""
import re
import sys
from pathlib import Path

REQUIRED = ["学习目标", "输入", "核心讲解", "练习", "验收标准", "对应技能", "常见错误", "教学提示", "复用说明"]


def check(path):
    text = Path(path).read_text(encoding="utf-8")
    problems = []
    for sec in REQUIRED:
        if not re.search(rf"^#+\s*\d*\.?\s*{re.escape(sec)}", text, re.M):
            problems.append(f"缺章节：{sec}")

    goals = re.findall(r"^\d+\.\s+\S", text, re.M)
    if len(goals) < 3:
        problems.append(f"学习目标只有 {len(goals)} 条，至少 3 条")

    errors = re.search(r"## 7\. 常见错误(.*?)(?=\n## |\Z)", text, re.S)
    if not errors or len(re.findall(r"^\d+\.\s+\S", errors.group(1), re.M)) < 3:
        problems.append("常见错误少于 3 条")

    if "|" not in text:
        problems.append("没有验收标准表")

    core = re.search(r"## 3\. 核心讲解.*?\n(.*?)(?=\n## |\Z)", text, re.S)
    if core:
        body = re.sub(r"\s", "", core.group(1))
        if len(body) > 320:
            problems.append(f"核心讲解 {len(body)} 字，超过 300 字上限，建议拆单元")
    return problems


def main():
    files = sys.argv[1:] or ["units/unit-c4c.md", "units/unit-c6a.md"]
    bad = 0
    for f in files:
        problems = check(f)
        status = "OK" if not problems else "FAIL"
        print(f"[{status}] {f}")
        for p in problems:
            print(f"       - {p}")
        bad += bool(problems)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
