#!/usr/bin/env python3
"""
Add Desmos hints to questions — v4 (precise).
Uses exact lesson boundaries to find questions.
"""
import re
from pathlib import Path

MODULES_FILE = Path("/home/z/my-project/src/lib/modules.ts")
content = MODULES_FILE.read_text()
lines = content.split("\n")

# Find lesson boundaries (line ranges)
# Lesson 1.2 is in const lesson_1_2_questions (lines 98 - first `];` after that)
lesson_ranges = {}

# Lesson 1.2: const lesson_1_2_questions: Question[] = [ ... ];
for i, line in enumerate(lines):
    if "const lesson_1_2_questions" in line:
        # Find the closing `];`
        for j in range(i + 1, len(lines)):
            if re.match(r'^\];\s*$', lines[j]):
                lesson_ranges["1.2"] = (i, j)
                break
        break

# Other lessons: id: "1.X" ... qs: [ ... ]
# The qs array is inline within the module
lesson_ids = ["1.1", "1.3", "1.4", "1.5"]
for lid in lesson_ids:
    lesson_start = None
    for i, line in enumerate(lines):
        if f'id: "{lid}"' in line:
            lesson_start = i
            break
    if lesson_start is None:
        continue
    # Find qs: [ after the lesson_start (within 20 lines)
    qs_start = None
    for i in range(lesson_start, min(lesson_start + 30, len(lines))):
        if "qs: [" in lines[i]:
            qs_start = i
            break
    if qs_start is None:
        continue
    # Find the closing ] of the qs array — it's a line with just `],` or `]`
    # at the same indent as the module
    qs_end = None
    bracket_count = 0
    for i in range(qs_start, len(lines)):
        bracket_count += lines[i].count("[") - lines[i].count("]")
        if bracket_count <= 0 and i > qs_start:
            qs_end = i
            break
    if qs_end is None:
        # fallback: find next `},` at module indent
        for i in range(qs_start + 1, min(qs_start + 200, len(lines))):
            if re.match(r'^      \},\s*$', lines[i]):
                qs_end = i
                break
    lesson_ranges[lid] = (qs_start, qs_end if qs_end else qs_start + 100)

print("Lesson ranges found:")
for lid, (s, e) in lesson_ranges.items():
    print(f"  {lid}: lines {s+1}-{e+1}")

# Hints for each lesson
HINTS = {
    "1.1": [
        (5, "Open Desmos and define a slider for $a$ (any positive value, say $a = 4$). Type $y = 2\\sqrt{2x}$ and $y = a$ in two lines. The intersection point gives the $x$ value. Then compute $2x$ to verify it equals $\\frac{a^{2}}{4}$. For $a = 4$: $2x = \\frac{16}{4} = 4$ ✓."),
        (6, "Open Desmos and assign $p = 25$ (so $25\\%$ of $x = 3$ means $x = 12$). Now test each option by typing them as $f(p)$. Only $\\frac{(100)(3)}{p} = \\frac{300}{25} = 12$ matches ✓. Type each option: $y = \\frac{p}{300}$, $y = \\frac{3p}{100}$, $y = \\frac{300}{p}$, $y = \\frac{3}{p}$ — the one that gives $12$ when $p = 25$ is correct."),
        (16, "Open Desmos and type $y = x^2 + 10 - 91$ (or $y = x^2 - 81$). The graph crosses the $x$-axis at the zeros. Click on each intersection point to see the coordinates. The positive $x$-intercept is $9$ ✓."),
        (17, "Open Desmos and type $y = 3(x/5 + 1/2) + 1$ and $y = 10$ on two lines. The intersection point's $x$-coordinate is the solution for $x$. Once you have $x$, compute $x/5 + 1/2$ to verify the answer is $3$ ✓."),
        (18, "Open Desmos and type $y = \\frac{2x}{3} - 2$ in line 1 and $y = \\frac{x}{3} + 1$ in line 2. Click the intersection point of the two lines — the $x$-coordinate is $9$ ✓. This visualizes why the two expressions are equal when $x = 9$."),
    ],
    "1.2": [
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
    ],
    "1.3": [
        (7, "Open Desmos and type $4x - 2y > 8$ in line 1. Desmos automatically shades the solution region. Then type each point as $(x, y)$ in separate lines: $(-1, -10)$, $(2, 0)$, $(1, -2)$. The point inside the shaded region is the answer. Only $(-1, -10)$ is in the shaded area ✓."),
        (8, "Open Desmos and type $y > 4x$ in line 1 and $y < -x$ in line 2. The overlapping shaded region is the solution. Test each point: $(-2, -2)$ falls inside both shaded regions ✓."),
        (9, "Open Desmos and type each option: $y \\leq -3x + 1$, $y \\geq -3x + 1$, $y \\geq 3x - 1$, $y \\leq 3x - 1$. Compare the shaded region to the graph shown in the question. The matching one has slope $-3$, $y$-intercept $1$, and shades above the line."),
        (10, "Open Desmos and type $y < -2x + 3$ in line 1 and $y > x - 3$ in line 2. Then plot point $P = (2, -4)$ by typing $(2, -4)$. The point is in the shaded region of inequality I ($y < -2x + 3$) but not inequality II ($y > x - 3$) ✓."),
        (11, "Open Desmos and type $10 - x - y \\geq 4$ (or $x + y \\leq 6$). The shaded region shows all valid $(x, y)$ combinations. This matches the situation: started with 10 mL, poured out $x + y$ mL, kept at least 4 mL ✓."),
        (12, "Open Desmos and type $35b + 160 \\leq 650$ (the correct answer). Desmos shades the valid range of $b$ values. Try $b = 14$: $35(14) + 160 = 650$ ✓ (boundary). For $b = 15$: $35(15) + 160 = 685 > 650$ ✗ (exceeds limit)."),
    ],
    "1.4": [
        (1, "Open Desmos and type $y = |x + 2|$ in line 1 and $y = 9$ in line 2. The graph of $y = |x + 2|$ is a V-shape, and $y = 9$ is a horizontal line. Click both intersection points — they are at $x = 7$ and $x = -11$. The option matching is $7$ ✓."),
        (2, "Open Desmos and type $y = |x - 4|$ in line 1 and $y = 19$ in line 2. The V-shaped graph crosses the horizontal line at two points. Click both — the $x$-coordinates are $23$ and $-15$ ✓."),
        (3, "Open Desmos and type $y = 2|x - 9|$ in line 1 and $y = 20$ in line 2. The V-shape (stretched by 2) crosses the horizontal line at $x = 19$ and $x = -1$. Sum: $19 + (-1) = 18$ ✓."),
        (4, "Open Desmos and type $y = |x - 1|$ in line 1 and $y = 8$ in line 2. The graph shows the V crossing the line at $x = 9$ (where $x - 1 = 8$) and $x = -7$ (where $x - 1 = -8$). So a possible value of $x - 1$ is $-8$ ✓."),
        (5, "Open Desmos and type $y = |x + 2|$ in line 1 and $y = |x - 8|$ in line 2. The two V-shapes cross at exactly one point. Click the intersection — the $x$-coordinate is $3$ ✓."),
        (6, "Open Desmos and type $y = |x + 3|$. The V-shape touches the $x$-axis at exactly one point: $x = -3$. This is the only solution ✓."),
    ],
    "1.5": [
        (3, "Open Desmos and use the table feature: enter points $(2, 6)$ and $(6, 12)$. Then type $y = \\frac{3}{2}x + 3$ to verify both points lie on this line. The slope $\\frac{12-6}{6-2} = \\frac{3}{2}$ ✓."),
        (4, "Open Desmos and type points $(1, 3)$ and $(5, 15)$ as a table. Then type $y = 3x$ — both points lie on this line. The slope $\\frac{15-3}{5-1} = 3$ and $y$-intercept is $0$ ✓."),
        (7, "Open Desmos and test each option. Type $y = \\frac{1}{2}x + 10$ (option D) and use a slider for $x$. When $x = 20$ (nonsale price), $y = 20$. Half the price ($10$) plus $10$ shipping = $20$ ✓. This matches the sale scenario."),
        (8, "Open Desmos and type $D = 38T + 385000$ with a slider for $T$. At $T = 0$ (present), $D = 385000$ ✓. As $T$ increases, $D$ increases (Moon moves away from Earth) ✓."),
        (16, "Open Desmos and type $\\frac{2x}{3} + \\frac{y}{3} = 1$ (Desmos graphs this directly). To find the $x$-intercept, set $y = 0$: type $y = 0$ in line 2. The intersection gives $x = 1.5$ ✓."),
        (20, "Open Desmos and type $y = \\frac{1}{6}x - 4$. The slope is $\\frac{1}{6}$. Since line $k$ is parallel to line $L$, it has the same slope: $\\frac{1}{6}$ ✓."),
        (22, "Open Desmos and type $y = -2x + 3$ in line 1. The perpendicular line has slope $\\frac{1}{2}$ (negative reciprocal). Type $y = \\frac{1}{2}x + b$ in line 2 and add a slider for $b$. When the line passes through $(-3, 1)$, $b = 2.5$ ✓."),
    ],
}

# Collect all insertions
insertions = []  # (line_idx, new_lines)
total = 0

for lid, hints in HINTS.items():
    if lid not in lesson_ranges:
        print(f"⚠ Lesson {lid} range not found")
        continue
    range_start, range_end = lesson_ranges[lid]
    print(f"\n=== Lesson {lid} (lines {range_start+1}-{range_end+1}) ===")

    for q_n, hint in hints:
        # Find `n: q_n,` within the lesson range
        q_start = None
        for i in range(range_start, range_end + 1):
            if re.match(rf'^(\s+)n:\s*{q_n}\s*,\s*$', lines[i]):
                q_start = i
                break
        if q_start is None:
            print(f"  ⚠ Q{q_n} not found in lesson {lid}")
            continue

        indent = re.match(r'^(\s+)n:', lines[q_start]).group(1)
        # Find closing `},` at the right indent
        close_indent = indent[:-2] if len(indent) >= 2 else indent
        q_end = None
        for i in range(q_start + 1, range_end + 1):
            if re.match(rf'^{re.escape(close_indent)}\}}\s*,?\s*$', lines[i].rstrip()):
                q_end = i
                break
        if q_end is None:
            print(f"  ⚠ Q{q_n}: couldn't find closing brace")
            continue

        # Check if desmosHint already exists
        already = any(re.match(r'^\s+desmosHint:', lines[i]) for i in range(q_start, q_end + 1))
        if already:
            print(f"  ✓ Q{q_n} already has desmosHint — skipping")
            continue

        # Find solution end
        sol_end = None
        for i in range(q_start, q_end + 1):
            if "solution:" in lines[i]:
                for j in range(i, q_end + 1):
                    if re.search(r'",\s*$', lines[j].rstrip()):
                        sol_end = j
                        break
                break
        if sol_end is None:
            print(f"  ⚠ Q{q_n}: couldn't find solution end")
            continue

        new_line = f'{indent}desmosHint:\n{indent}  "{hint}",'
        insertions.append((sol_end + 1, new_line))
        print(f"  ✓ Q{q_n}: insert after line {sol_end + 1}")
        total += 1

# Apply insertions in reverse order
insertions.sort(key=lambda x: -x[0])
for line_idx, new_line in insertions:
    lines.insert(line_idx, new_line)

content = "\n".join(lines)
MODULES_FILE.write_text(content)
print(f"\n✓ Done! Added {total} Desmos hints total.")
