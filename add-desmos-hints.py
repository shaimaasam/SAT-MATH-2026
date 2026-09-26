#!/usr/bin/env python3
"""
Add Desmos hints to questions in modules.ts.

Strategy: for each question we want to add a desmosHint to, find the
solution line (which ends with `,`), then add the desmosHint on the
next line with matching indentation.
"""

import re
from pathlib import Path

MODULES_FILE = Path("/home/z/my-project/src/lib/modules.ts")
content = MODULES_FILE.read_text()

# Format: (lesson_id, question_n, desmos_hint_text)
# Each hint is a single line; we'll wrap it properly.
HINTS = [
    # === Lesson 1.2 — Systems of Linear Equations (11 questions) ===
    ("1.2", 1, "Open Desmos and type $y = 6x + 4$ (rewritten from $6x - y = -4$) in line 1, and $y = 9x + 3$ (from $9x - y = -3$) in line 2. Click the intersection point of the two lines. The $x$-coordinate is $\\frac{1}{3}$ ✓."),
    ("1.2", 2, "Open Desmos and type $x + 2y = 11$ in line 1 (Desmos understands this form directly) and $3x + 3y = 24$ in line 2. Click the intersection point — you'll see coordinates $(5, 3)$. So $x = 5$ ✓."),
    ("1.2", 3, "Open Desmos and type $-3x + 4y = 4$ in line 1 and $4x - 3y = 0.5$ in line 2. Desmos graphs both lines and shows the intersection. Click the intersection point to read the $y$-coordinate: $2.5 = \\frac{5}{2}$ ✓."),
    ("1.2", 4, "Open Desmos and type $9x - 2y = 8$ in line 1 and $2x - 9y = -2.5$ in line 2 (replace $-\\frac{5}{2}$ with $-2.5$). Desmos shows the intersection at $(1, 0.5)$. Click the point to confirm coordinates ✓."),
    ("1.2", 5, "Open Desmos and type $3x + 5y = 17$ in line 1 and $5x + 3y = 23$ in line 2. Click the intersection point — read both coordinates $(x, y)$. Add them up to verify $x + y = 5$ ✓."),
    ("1.2", 6, "Open Desmos and type $x + y = 3$ in line 1 and $x - y = 3$ in line 2. The lines intersect at $(3, 0)$. So $x = 3$ and $2x = 6$ ✓."),
    ("1.2", 11, "Open Desmos and type each option as a system of two equations on separate lines. For option A: $x + 3y = 5$ and $2x + 6y = 9$. The lines are parallel (no intersection). For option C: $x + 2y = 3$ and $2x + 3y = 3$. The lines cross once ✓. For B: $x + 2y = 3$ and $2x + 4y = 6$ — same line (overlap). For D: parallel again."),
    ("1.2", 14, "Open Desmos and type $10x - 2y = 18$ in line 1 and $-60x + 12y = -108$ in line 2. Notice the second line is just $-6$ times the first — the two lines overlap completely. This means infinitely many solutions ✓."),
    ("1.2", 15, "Open Desmos and type $4y - 8x = 36$ in line 1 (rewrite as $y = 2x + 9$) and $y - 2x = 18$ in line 2 (rewrite as $y = 2x + 18$). The lines have the same slope but different $y$-intercepts — parallel, so zero solutions ✓."),
    ("1.2", 22, "Open Desmos: type $s + w = 240$ in line 1 and $9s + 4w = 1600$ in line 2. Click the intersection point. The $w$-coordinate gives minutes walking = $112$ ✓. (Desmos makes this word problem visual.)"),
    ("1.2", 23, "Open Desmos: type $w + b = 360$ in line 1 and $5.3w + 6.4b = 1941$ in line 2. Click the intersection — the $b$-coordinate (bicycling minutes) is $30$ ✓."),

    # === Lesson 1.3 — Inequalities (6 questions) ===
    ("1.3", 7, "Open Desmos and type $4x - 2y > 8$ in line 1. Desmos automatically shades the solution region. Then type each point as $(x, y)$ in separate lines: $(-1, -10)$, $(2, 0)$, $(1, -2)$. The point inside the shaded region is the answer. Only $(-1, -10)$ is in the shaded area ✓."),
    ("1.3", 8, "Open Desmos and type $y > 4x$ in line 1 and $y < -x$ in line 2. The overlapping shaded region is the solution. Test each point: $(-2, -2)$ falls inside both shaded regions ✓."),
    ("1.3", 9, "Open Desmos and type each option: $y \\leq -3x + 1$, $y \\geq -3x + 1$, $y \\geq 3x - 1$, $y \\leq 3x - 1$. Compare the shaded region to the graph shown in the question. The matching one has slope $-3$, $y$-intercept $1$, and shades above the line."),
    ("1.3", 10, "Open Desmos and type $y < -2x + 3$ in line 1 and $y > x - 3$ in line 2. Then plot point $P = (2, -4)$ by typing $(2, -4)$. The point is in the shaded region of inequality I ($y < -2x + 3$) but not inequality II ($y > x - 3$) ✓."),
    ("1.3", 11, "Open Desmos and type $10 - x - y \\geq 4$ (or $x + y \\leq 6$). The shaded region shows all valid $(x, y)$ combinations. This matches the situation: started with 10 mL, poured out $x + y$ mL, kept at least 4 mL ✓."),
    ("1.3", 12, "Open Desmos and type $35b + 160 \\leq 650$ (the correct answer). Desmos shades the valid range of $b$ values. Try $b = 14$: $35(14) + 160 = 650$ ✓ (boundary). For $b = 15$: $35(15) + 160 = 685 > 650$ ✗ (exceeds limit)."),

    # === Lesson 1.4 — Absolute Value (all 6 questions) ===
    ("1.4", 1, "Open Desmos and type $y = |x + 2|$ in line 1 and $y = 9$ in line 2. The graph of $y = |x + 2|$ is a V-shape, and $y = 9$ is a horizontal line. Click both intersection points — they are at $x = 7$ and $x = -11$. The option matching is $7$ ✓."),
    ("1.4", 2, "Open Desmos and type $y = |x - 4|$ in line 1 and $y = 19$ in line 2. The V-shaped graph crosses the horizontal line at two points. Click both — the $x$-coordinates are $23$ and $-15$ ✓."),
    ("1.4", 3, "Open Desmos and type $y = 2|x - 9|$ in line 1 and $y = 20$ in line 2. The V-shape (stretched by 2) crosses the horizontal line at $x = 19$ and $x = -1$. Sum: $19 + (-1) = 18$ ✓."),
    ("1.4", 4, "Open Desmos and type $y = |x - 1|$ in line 1 and $y = 8$ in line 2. The graph shows the V crossing the line at $x = 9$ (where $x - 1 = 8$) and $x = -7$ (where $x - 1 = -8$). So a possible value of $x - 1$ is $-8$ ✓."),
    ("1.4", 5, "Open Desmos and type $y = |x + 2|$ in line 1 and $y = |x - 8|$ in line 2. The two V-shapes cross at exactly one point. Click the intersection — the $x$-coordinate is $3$ ✓."),
    ("1.4", 6, "Open Desmos and type $y = |x + 3|$. The V-shape touches the $x$-axis at exactly one point: $x = -3$. This is the only solution ✓."),

    # === Lesson 1.5 — Linear Functions (7 questions) ===
    ("1.5", 3, "Open Desmos and use the table feature: enter points $(2, 6)$ and $(6, 12)$. Then type $y = \\frac{3}{2}x + 3$ to verify both points lie on this line. The slope $\\frac{12-6}{6-2} = \\frac{3}{2}$ ✓."),
    ("1.5", 4, "Open Desmos and type points $(1, 3)$ and $(5, 15)$ as a table. Then type $y = 3x$ — both points lie on this line. The slope $\\frac{15-3}{5-1} = 3$ and $y$-intercept is $0$ ✓."),
    ("1.5", 7, "Open Desmos and test each option. Type $y = \\frac{1}{2}x + 10$ (option D) and use a slider for $x$. When $x = 20$ (nonsale price), $y = 20$. Half the price ($10$) plus $10$ shipping = $20$ ✓. This matches the sale scenario."),
    ("1.5", 8, "Open Desmos and type $D = 38T + 385000$ with a slider for $T$. At $T = 0$ (present), $D = 385000$ ✓. As $T$ increases, $D$ increases (Moon moves away from Earth) ✓."),
    ("1.5", 16, "Open Desmos and type $\\frac{2x}{3} + \\frac{y}{3} = 1$ (Desmos graphs this directly). To find the $x$-intercept, set $y = 0$: type $y = 0$ in line 2. The intersection gives $x = 1.5$ ✓."),
    ("1.5", 20, "Open Desmos and type $y = \\frac{1}{6}x - 4$. The slope is $\\frac{1}{6}$. Since line $k$ is parallel to line $L$, it has the same slope: $\\frac{1}{6}$ ✓."),
    ("1.5", 22, "Open Desmos and type $y = -2x + 3$ in line 1. The perpendicular line has slope $\\frac{1}{2}$ (negative reciprocal). Type $y = \\frac{1}{2}x + b$ in line 2 and add a slider for $b$. When the line passes through $(-3, 1)$, $b = 2.5$ ✓."),
]

def find_question_block(lesson_id: str, q_n: int, content: str) -> tuple[int, int, str] | None:
    """Find the start and end lines of a question with given n in a lesson.

    Returns (start_line_idx, end_line_idx, indent) or None.
    """
    lines = content.split("\n")
    # Find the lesson module by looking for `id: "1.3",` etc.
    lesson_marker = f'id: "{lesson_id}"'
    lesson_start = None
    for i, line in enumerate(lines):
        if lesson_marker in line:
            lesson_start = i
            break
    if lesson_start is None:
        return None

    # Find `qs: [` after the lesson marker (this is the questions array)
    qs_start = None
    for i in range(lesson_start, min(lesson_start + 100, len(lines))):
        if "qs: [" in lines[i]:
            qs_start = i
            break
    if qs_start is None:
        return None

    # Now find the question with n: q_n
    q_start = None
    for i in range(qs_start, len(lines)):
        # Match `    n: <q_n>,` exactly
        if re.match(rf'^(\s+)n:\s*{q_n}\s*,\s*$', lines[i]):
            q_start = i
            break
    if q_start is None:
        return None

    # Find the indent (from the n: line)
    indent_match = re.match(r'^(\s+)n:', lines[q_start])
    indent = indent_match.group(1)

    # Find end of question: the line with `},` at the same indent level
    # (or `}` followed by comma)
    q_end = None
    for i in range(q_start + 1, len(lines)):
        # Match closing `},` at the same indent
        if re.match(rf'^{re.escape(indent)}\}},?\s*$', lines[i].rstrip()):
            q_end = i
            break
    if q_end is None:
        return None

    return (q_start, q_end, indent)


def has_desmos_hint(q_start: int, q_end: int, lines: list[str]) -> bool:
    """Check if the question already has a desmosHint field."""
    for i in range(q_start, q_end + 1):
        if "desmosHint" in lines[i]:
            return True
    return False


def find_solution_line_end(q_start: int, q_end: int, lines: list[str]) -> int | None:
    """Find the line index where the solution string value ends (the line
    that ends with `,"` or just `",`)."""
    # First find the `solution:` line
    sol_start = None
    for i in range(q_start, q_end + 1):
        if "solution:" in lines[i]:
            sol_start = i
            break
    if sol_start is None:
        return None

    # The solution value may span multiple lines. Find the line that ends
    # the string literal — it ends with `",` or `"` followed by `,`.
    for i in range(sol_start, q_end + 1):
        stripped = lines[i].rstrip()
        # Match: ends with ", (string value ends here)
        if re.search(r'",\s*$', stripped):
            return i
    return q_end  # fallback


def add_desmos_hint(lesson_id: str, q_n: int, hint: str, content: str) -> str:
    """Add a desmosHint to a question. Returns new content."""
    result = find_question_block(lesson_id, q_n, content)
    if result is None:
        print(f"  ⚠ Question {q_n} in lesson {lesson_id} not found")
        return content
    q_start, q_end, indent = result
    lines = content.split("\n")

    if has_desmos_hint(q_start, q_end, lines):
        print(f"  ✓ Q{q_n} in {lesson_id} already has desmosHint — skipping")
        return content

    sol_end = find_solution_line_end(q_start, q_end, lines)
    if sol_end is None:
        print(f"  ⚠ Q{q_n} in {lesson_id}: couldn't find solution end")
        return content

    # Insert the desmosHint line right after sol_end
    # Use the same indent as `solution:` (which is indent + 2 spaces for the value,
    # but the field name uses `indent`)
    new_line = f'{indent}desmosHint:\n{indent}  "{hint}",'
    lines.insert(sol_end + 1, new_line)

    print(f"  ✓ Added desmosHint to Q{q_n} in lesson {lesson_id}")
    return "\n".join(lines)


print("Adding Desmos hints to questions...")
for lesson_id, q_n, hint in HINTS:
    print(f"\n[{lesson_id} Q{q_n}]")
    content = add_desmos_hint(lesson_id, q_n, hint, content)

MODULES_FILE.write_text(content)
print(f"\n✓ Done! Wrote {MODULES_FILE}")
