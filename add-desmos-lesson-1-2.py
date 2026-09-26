#!/usr/bin/env python3
"""
Add Desmos hints to questions in modules.ts — v2.
Handles both inline qs arrays and the separate lesson_1_2_questions const.
"""

import re
from pathlib import Path

MODULES_FILE = Path("/home/z/my-project/src/lib/modules.ts")
content = MODULES_FILE.read_text()
lines = content.split("\n")

HINTS = [
    # === Lesson 1.2 — Systems of Linear Equations ===
    (1, "Open Desmos and type $y = 6x + 4$ (rewritten from $6x - y = -4$) in line 1, and $y = 9x + 3$ (from $9x - y = -3$) in line 2. Click the intersection point of the two lines. The $x$-coordinate is $\\frac{1}{3}$ ✓."),
    (2, "Open Desmos and type $x + 2y = 11$ in line 1 (Desmos understands this form directly) and $3x + 3y = 24$ in line 2. Click the intersection point — you'll see coordinates $(5, 3)$. So $x = 5$ ✓."),
    (3, "Open Desmos and type $-3x + 4y = 4$ in line 1 and $4x - 3y = 0.5$ in line 2. Desmos graphs both lines and shows the intersection. Click the intersection point to read the $y$-coordinate: $2.5 = \\frac{5}{2}$ ✓."),
    (4, "Open Desmos and type $9x - 2y = 8$ in line 1 and $2x - 9y = -2.5$ in line 2 (replace $-\\frac{5}{2}$ with $-2.5$). Desmos shows the intersection at $(1, 0.5)$. Click the point to confirm coordinates ✓."),
    (5, "Open Desmos and type $3x + 5y = 17$ in line 1 and $5x + 3y = 23$ in line 2. Click the intersection point — read both coordinates $(x, y)$. Add them up to verify $x + y = 5$ ✓."),
    (6, "Open Desmos and type $x + y = 3$ in line 1 and $x - y = 3$ in line 2. The lines intersect at $(3, 0)$. So $x = 3$ and $2x = 6$ ✓."),
    (11, "Open Desmos and type each option as a system of two equations on separate lines. For option A: $x + 3y = 5$ and $2x + 6y = 9$. The lines are parallel (no intersection). For option C: $x + 2y = 3$ and $2x + 3y = 3$. The lines cross once ✓. For B: $x + 2y = 3$ and $2x + 4y = 6$ — same line (overlap). For D: parallel again."),
    (14, "Open Desmos and type $10x - 2y = 18$ in line 1 and $-60x + 12y = -108$ in line 2. Notice the second line is just $-6$ times the first — the two lines overlap completely. This means infinitely many solutions ✓."),
    (15, "Open Desmos and type $4y - 8x = 36$ in line 1 (rewrite as $y = 2x + 9$) and $y - 2x = 18$ in line 2 (rewrite as $y = 2x + 18$). The lines have the same slope but different $y$-intercepts — parallel, so zero solutions ✓."),
    (22, "Open Desmos: type $s + w = 240$ in line 1 and $9s + 4w = 1600$ in line 2. Click the intersection point. The $w$-coordinate gives minutes walking = $112$ ✓. (Desmos makes this word problem visual.)"),
    (23, "Open Desmos: type $w + b = 360$ in line 1 and $5.3w + 6.4b = 1941$ in line 2. Click the intersection — the $b$-coordinate (bicycling minutes) is $30$ ✓."),
]

def find_question_in_lesson_1_2(q_n: int) -> tuple[int, int, str] | None:
    """Find a question in the lesson_1_2_questions const array."""
    # Find `const lesson_1_2_questions: Question[] = [`
    start = None
    for i, line in enumerate(lines):
        if "const lesson_1_2_questions" in line and "[" in line:
            start = i
            break
    if start is None:
        return None
    # Find `n: q_n,` after start
    for i in range(start, len(lines)):
        if re.match(rf'^(\s+)n:\s*{q_n}\s*,\s*$', lines[i]):
            indent = re.match(r'^(\s+)n:', lines[i]).group(1)
            # Find end: line with `},` at same indent level
            for j in range(i + 1, len(lines)):
                if re.match(rf'^{re.escape(indent)}\}}\s*,?\s*$', lines[j].rstrip()):
                    return (i, j, indent)
    return None

def has_desmos(q_start: int, q_end: int) -> bool:
    for i in range(q_start, q_end + 1):
        if "desmosHint" in lines[i]:
            return True
    return False

def find_solution_end(q_start: int, q_end: int) -> int | None:
    """Find the line where the solution string value ends."""
    for i in range(q_start, q_end + 1):
        if "solution:" in lines[i]:
            # Find the closing `",` after this
            for j in range(i, q_end + 1):
                if re.search(r'",\s*$', lines[j].rstrip()):
                    return j
            break
    return None

# Process lesson 1.2
print("=== Lesson 1.2 (Systems of Linear Equations) ===")
insertions = []  # list of (line_idx, new_lines_to_insert)
for q_n, hint in HINTS:
    result = find_question_in_lesson_1_2(q_n)
    if result is None:
        print(f"  ⚠ Q{q_n} not found")
        continue
    q_start, q_end, indent = result
    if has_desmos(q_start, q_end):
        print(f"  ✓ Q{q_n} already has desmosHint — skipping")
        continue
    sol_end = find_solution_end(q_start, q_end)
    if sol_end is None:
        print(f"  ⚠ Q{q_n}: couldn't find solution end")
        continue
    new_line = f'{indent}desmosHint:\n{indent}  "{hint}",'
    insertions.append((sol_end + 1, new_line))
    print(f"  ✓ Q{q_n}: will insert after line {sol_end + 1}")

# Apply insertions in reverse order (so indices don't shift)
insertions.sort(key=lambda x: -x[0])
for line_idx, new_line in insertions:
    lines.insert(line_idx, new_line)

content = "\n".join(lines)
MODULES_FILE.write_text(content)
print(f"\n✓ Wrote {MODULES_FILE}")
print(f"  Added {len(insertions)} Desmos hints to lesson 1.2")
