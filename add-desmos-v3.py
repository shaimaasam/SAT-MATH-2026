#!/usr/bin/env python3
"""
Add Desmos hints to questions — v3 (robust).
Finds questions by their `n:` field anywhere in the file, then inserts
desmosHint after the solution line.
"""
import re
from pathlib import Path

MODULES_FILE = Path("/home/z/my-project/src/lib/modules.ts")
content = MODULES_FILE.read_text()
lines = content.split("\n")

# (q_n, desmos_hint) — q_n is the question number
HINTS_1_2 = [
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

# Lesson 1.3 — Inequalities (q_n 7-16)
HINTS_1_3 = [
    (7, "Open Desmos and type $4x - 2y > 8$ in line 1. Desmos automatically shades the solution region. Then type each point as $(x, y)$ in separate lines: $(-1, -10)$, $(2, 0)$, $(1, -2)$. The point inside the shaded region is the answer. Only $(-1, -10)$ is in the shaded area ✓."),
    (8, "Open Desmos and type $y > 4x$ in line 1 and $y < -x$ in line 2. The overlapping shaded region is the solution. Test each point: $(-2, -2)$ falls inside both shaded regions ✓."),
    (9, "Open Desmos and type each option: $y \\leq -3x + 1$, $y \\geq -3x + 1$, $y \\geq 3x - 1$, $y \\leq 3x - 1$. Compare the shaded region to the graph shown in the question. The matching one has slope $-3$, $y$-intercept $1$, and shades above the line."),
    (10, "Open Desmos and type $y < -2x + 3$ in line 1 and $y > x - 3$ in line 2. Then plot point $P = (2, -4)$ by typing $(2, -4)$. The point is in the shaded region of inequality I ($y < -2x + 3$) but not inequality II ($y > x - 3$) ✓."),
    (11, "Open Desmos and type $10 - x - y \\geq 4$ (or $x + y \\leq 6$). The shaded region shows all valid $(x, y)$ combinations. This matches the situation: started with 10 mL, poured out $x + y$ mL, kept at least 4 mL ✓."),
    (12, "Open Desmos and type $35b + 160 \\leq 650$ (the correct answer). Desmos shades the valid range of $b$ values. Try $b = 14$: $35(14) + 160 = 650$ ✓ (boundary). For $b = 15$: $35(15) + 160 = 685 > 650$ ✗ (exceeds limit)."),
]

# Lesson 1.4 — Absolute Value (q_n 1-6)
HINTS_1_4 = [
    (1, "Open Desmos and type $y = |x + 2|$ in line 1 and $y = 9$ in line 2. The graph of $y = |x + 2|$ is a V-shape, and $y = 9$ is a horizontal line. Click both intersection points — they are at $x = 7$ and $x = -11$. The option matching is $7$ ✓."),
    (2, "Open Desmos and type $y = |x - 4|$ in line 1 and $y = 19$ in line 2. The V-shaped graph crosses the horizontal line at two points. Click both — the $x$-coordinates are $23$ and $-15$ ✓."),
    (3, "Open Desmos and type $y = 2|x - 9|$ in line 1 and $y = 20$ in line 2. The V-shape (stretched by 2) crosses the horizontal line at $x = 19$ and $x = -1$. Sum: $19 + (-1) = 18$ ✓."),
    (4, "Open Desmos and type $y = |x - 1|$ in line 1 and $y = 8$ in line 2. The graph shows the V crossing the line at $x = 9$ (where $x - 1 = 8$) and $x = -7$ (where $x - 1 = -8$). So a possible value of $x - 1$ is $-8$ ✓."),
    (5, "Open Desmos and type $y = |x + 2|$ in line 1 and $y = |x - 8|$ in line 2. The two V-shapes cross at exactly one point. Click the intersection — the $x$-coordinate is $3$ ✓."),
    (6, "Open Desmos and type $y = |x + 3|$. The V-shape touches the $x$-axis at exactly one point: $x = -3$. This is the only solution ✓."),
]

# Lesson 1.5 — Linear Functions (q_n 3, 4, 7, 8, 16, 20, 22)
HINTS_1_5 = [
    (3, "Open Desmos and use the table feature: enter points $(2, 6)$ and $(6, 12)$. Then type $y = \\frac{3}{2}x + 3$ to verify both points lie on this line. The slope $\\frac{12-6}{6-2} = \\frac{3}{2}$ ✓."),
    (4, "Open Desmos and type points $(1, 3)$ and $(5, 15)$ as a table. Then type $y = 3x$ — both points lie on this line. The slope $\\frac{15-3}{5-1} = 3$ and $y$-intercept is $0$ ✓."),
    (7, "Open Desmos and test each option. Type $y = \\frac{1}{2}x + 10$ (option D) and use a slider for $x$. When $x = 20$ (nonsale price), $y = 20$. Half the price ($10$) plus $10$ shipping = $20$ ✓. This matches the sale scenario."),
    (8, "Open Desmos and type $D = 38T + 385000$ with a slider for $T$. At $T = 0$ (present), $D = 385000$ ✓. As $T$ increases, $D$ increases (Moon moves away from Earth) ✓."),
    (16, "Open Desmos and type $\\frac{2x}{3} + \\frac{y}{3} = 1$ (Desmos graphs this directly). To find the $x$-intercept, set $y = 0$: type $y = 0$ in line 2. The intersection gives $x = 1.5$ ✓."),
    (20, "Open Desmos and type $y = \\frac{1}{6}x - 4$. The slope is $\\frac{1}{6}$. Since line $k$ is parallel to line $L$, it has the same slope: $\\frac{1}{6}$ ✓."),
    (22, "Open Desmos and type $y = -2x + 3$ in line 1. The perpendicular line has slope $\\frac{1}{2}$ (negative reciprocal). Type $y = \\frac{1}{2}x + b$ in line 2 and add a slider for $b$. When the line passes through $(-3, 1)$, $b = 2.5$ ✓."),
]

ALL_HINTS = {
    "1.2": HINTS_1_2,
    "1.3": HINTS_1_3,
    "1.4": HINTS_1_4,
    "1.5": HINTS_1_5,
}

def find_q_line(q_n: int, start_search: int = 0) -> int | None:
    """Find the line index of `n: q_n,` starting from start_search."""
    for i in range(start_search, len(lines)):
        if re.match(rf'^\s+n:\s*{q_n}\s*,\s*$', lines[i]):
            return i
    return None

def find_closing_brace(q_start: int) -> int | None:
    """Find the closing `},` of the question object."""
    indent = re.match(r'^(\s+)n:', lines[q_start]).group(1)
    # The closing brace is at indent - 2 spaces
    close_indent = indent[:-2] if len(indent) >= 2 else indent
    for i in range(q_start + 1, len(lines)):
        if re.match(rf'^{re.escape(close_indent)}\}}\s*,?\s*$', lines[i].rstrip()):
            return i
    return None

def find_solution_end(q_start: int, q_end: int) -> int | None:
    """Find the line where solution string ends (line ending with `",`)."""
    for i in range(q_start, q_end + 1):
        if "solution:" in lines[i]:
            for j in range(i, q_end + 1):
                if re.search(r'",\s*$', lines[j].rstrip()):
                    return j
            break
    return None

def has_desmos_in_range(q_start: int, q_end: int) -> bool:
    """Check if desmosHint already exists in the question."""
    for i in range(q_start, q_end + 1):
        if re.match(r'^\s+desmosHint:', lines[i]):
            return True
    return False

# Process each lesson
total_added = 0
for lesson_id, hints in ALL_HINTS.items():
    print(f"\n=== Lesson {lesson_id} ===")
    # Find the lesson's id: line to know where to start searching
    lesson_id_line = None
    for i, line in enumerate(lines):
        if f'id: "{lesson_id}"' in line:
            lesson_id_line = i
            break
    if lesson_id_line is None:
        # For lesson 1.2, search from the const declaration
        if lesson_id == "1.2":
            for i, line in enumerate(lines):
                if "const lesson_1_2_questions" in line:
                    lesson_id_line = i
                    break
    if lesson_id_line is None:
        print(f"  ⚠ Lesson {lesson_id} not found")
        continue

    insertions_for_lesson = []
    for q_n, hint in hints:
        # Find the question starting from lesson_id_line
        q_start = find_q_line(q_n, lesson_id_line)
        if q_start is None:
            print(f"  ⚠ Q{q_n} not found in lesson {lesson_id}")
            continue
        q_end = find_closing_brace(q_start)
        if q_end is None:
            print(f"  ⚠ Q{q_n}: couldn't find closing brace")
            continue
        if has_desmos_in_range(q_start, q_end):
            print(f"  ✓ Q{q_n} already has desmosHint — skipping")
            continue
        sol_end = find_solution_end(q_start, q_end)
        if sol_end is None:
            print(f"  ⚠ Q{q_n}: couldn't find solution end")
            continue
        indent = re.match(r'^(\s+)n:', lines[q_start]).group(1)
        new_line = f'{indent}desmosHint:\n{indent}  "{hint}",'
        insertions_for_lesson.append((sol_end + 1, new_line))
        print(f"  ✓ Q{q_n}: will insert after line {sol_end + 1}")
        total_added += 1

    # Apply insertions in reverse order
    insertions_for_lesson.sort(key=lambda x: -x[0])
    for line_idx, new_line in insertions_for_lesson:
        lines.insert(line_idx, new_line)

# Write back
content = "\n".join(lines)
MODULES_FILE.write_text(content)
print(f"\n✓ Done! Added {total_added} Desmos hints total.")
