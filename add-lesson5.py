#!/usr/bin/env python3
"""
Add Lesson 5 (Exponent and Root) questions to modules.ts.
- Q1-Q5 → Lesson 3.2 (Polynomials)
- Q6-Q14 → Lesson 3.4 (Radicals & Rational Exponents)
Includes Desmos hints for visual questions.
"""
from pathlib import Path

MODULES_FILE = Path("/home/z/my-project/src/lib/modules.ts")
content = MODULES_FILE.read_text()

# === Q1-Q5: Polynomials (Lesson 3.2) ===
POLY_QS = '''        {
          n: 1,
          domain: "Algebra",
          difficulty: "easy",
          text: "Calculate the polynomials $(12x^{4} - 5x + 18 + 6x^{4}) + (13x^{2} + 7x - 9)$.",
          type: "mcq",
          o: [
            "$18x^{4} + 8x^{2} + 25x - 9$",
            "$18x^{8} + 8x^{3} + 25x - 9$",
            "$18x^{8} + 13x^{3} + 2x + 9$",
            "$18x^{4} + 13x^{2} + 2x + 9$",
          ],
          a: "D",
          solution:
            "Combine like terms: $(12x^{4} + 6x^{4}) + 13x^{2} + (-5x + 7x) + (18 - 9) = 18x^{4} + 13x^{2} + 2x + 9$. The answer is D.",
        },
        {
          n: 2,
          domain: "Algebra",
          difficulty: "easy",
          text: "What is the difference between $2x^{2} + 3x - 2$ and $5x^{2} - x - 7$?",
          type: "mcq",
          o: [
            "$-3x^{2} + 4x + 5$",
            "$3x^{2} + 4x + 5$",
            "$7x^{2} + 4x + 9$",
            "$-3x^{2} + 2x + 9$",
          ],
          a: "A",
          solution:
            "Subtract: $(2x^{2} + 3x - 2) - (5x^{2} - x - 7) = 2x^{2} - 5x^{2} + 3x + x - 2 + 7 = -3x^{2} + 4x + 5$. The answer is A.",
        },
        {
          n: 3,
          domain: "Algebra",
          difficulty: "medium",
          text: "Determine $(2x^{5} + 3x^{2}) - (x^{5} - 7x^{2})$.",
          type: "mcq",
          o: [
            "$x^{10} + 10x^{4}$",
            "$x^{5} - 4x^{2}$",
            "$3x^{5} - 4x^{2}$",
            "$x^{5} + 10x^{2}$",
          ],
          a: "D",
          solution:
            "Subtract: $2x^{5} - x^{5} + 3x^{2} + 7x^{2} = x^{5} + 10x^{2}$. The answer is D.",
        },
        {
          n: 4,
          domain: "Algebra",
          difficulty: "medium",
          text: "Which polynomial is equivalent to $(x^{2} + 7)(12x^{3} - 6)$?",
          type: "mcq",
          o: [
            "$12x^{5} + 84x^{3} - 6x^{2} - 42$",
            "$12x^{3} + x^{2} + 1$",
            "$12x^{6} + 84x^{3} - 6x^{2} - 42$",
            "$12x^{6} - 42$",
          ],
          a: "A",
          solution:
            "Use FOIL/distribution: $x^{2} \\cdot 12x^{3} = 12x^{5}$, $x^{2} \\cdot (-6) = -6x^{2}$, $7 \\cdot 12x^{3} = 84x^{3}$, $7 \\cdot (-6) = -42$. Combine: $12x^{5} + 84x^{3} - 6x^{2} - 42$. The answer is A.",
        },
        {
          n: 5,
          domain: "Algebra",
          difficulty: "medium",
          text: "Which expression is equivalent to $2x^{5}(x^{3} + 5x)$?",
          type: "mcq",
          o: [
            "$3x^{8} + 7x^{6}$",
            "$2x^{15} + 10x^{5}$",
            "$2x^{15} + 7x^{5}$",
            "$2x^{8} + 10x^{6}$",
          ],
          a: "D",
          solution:
            "Distribute: $2x^{5} \\cdot x^{3} = 2x^{8}$ and $2x^{5} \\cdot 5x = 10x^{6}$. Combine: $2x^{8} + 10x^{6}$. The answer is D.",
          desmosHint:
            "Open Desmos and type $y = 2x^{5}(x^{3} + 5x)$ in line 1, then type each option (e.g., $y = 2x^{8} + 10x^{6}$) in line 2. If both graphs overlap perfectly, the option is equivalent. Option D overlaps ✓.",
        },'''

# === Q6-Q14: Radicals & Rational Exponents (Lesson 3.4) ===
RAD_QS = '''        {
          n: 6,
          domain: "Algebra",
          difficulty: "medium",
          text: "Simplify the expression $a^{2}b^{3}(a^{4}b^{4})$.",
          type: "mcq",
          o: [
            "$a^{5}b^{12}$",
            "$a^{6}b^{12}$",
            "$a^{6}b^{7}$",
            "$a^{5}b^{7}$",
          ],
          a: "C",
          solution:
            "When multiplying like bases, add exponents: $a^{2} \\cdot a^{4} = a^{6}$ and $b^{3} \\cdot b^{4} = b^{7}$. So the result is $a^{6}b^{7}$. The answer is C.",
        },
        {
          n: 7,
          domain: "Algebra",
          difficulty: "easy",
          text: "Convert the expression $\\sqrt{ab}$, where $a$ and $b$ are positive, into rational exponent notation.",
          type: "mcq",
          o: [
            "$a^{1/2}b$",
            "$ab^{1/2}$",
            "$a^{1/2}b^{1/2}$",
            "$ab^{2}$",
          ],
          a: "C",
          solution:
            "$\\sqrt{ab} = (ab)^{1/2} = a^{1/2} \\cdot b^{1/2} = a^{1/2}b^{1/2}$. The answer is C.",
        },
        {
          n: 8,
          domain: "Algebra",
          difficulty: "medium",
          text: "Which of the expressions is equivalent to $g^{2/5}h^{4/5}$?",
          type: "mcq",
          o: [
            "$\\sqrt[5]{g^{2}h^{4}}$",
            "$\\frac{1}{\\sqrt[4]{g^{5}h^{10}}}$",
            "$\\sqrt[4]{g^{5}h^{2}}$",
            "$\\frac{1}{\\sqrt[5]{g^{4}h^{2}}}$",
          ],
          a: "A",
          solution:
            "Use the rule $x^{m/n} = \\sqrt[n]{x^{m}}$. So $g^{2/5}h^{4/5} = \\sqrt[5]{g^{2}} \\cdot \\sqrt[5]{h^{4}} = \\sqrt[5]{g^{2}h^{4}}$. The answer is A.",
        },
        {
          n: 9,
          domain: "Algebra",
          difficulty: "hard",
          text: "Apply the product rule and power rule to simplify $k^{5/16}(k^{3/2})^{5/8}$ where $k > 0$.",
          type: "mcq",
          o: [
            "$\\sqrt{k}$",
            "$\\sqrt[4]{k^{5}}$",
            "$\\sqrt[8]{k^{5}}$",
            "$\\sqrt[15]{k^{16}}$",
          ],
          a: "B",
          solution:
            "Power rule: $(k^{3/2})^{5/8} = k^{(3/2)(5/8)} = k^{15/16}$. Product rule: $k^{5/16} \\cdot k^{15/16} = k^{(5+15)/16} = k^{20/16} = k^{5/4} = \\sqrt[4]{k^{5}}$. The answer is B.",
          desmosHint:
            "Open Desmos and type $y = k^{5/16} \\cdot (k^{3/2})^{5/8}$ in line 1 (add a slider for $k$). Then type $y = \\sqrt[4]{k^{5}}$ (option B) in line 2. Both graphs overlap perfectly ✓. Try the other options — they won't match.",
        },
        {
          n: 10,
          domain: "Algebra",
          difficulty: "hard",
          text: "Which of the expressions is equivalent to $y^{1/8}(y^{3/4})^{3/2}$?",
          type: "mcq",
          o: [
            "$\\sqrt{y}$",
            "$\\sqrt[4]{y^{5}}$",
            "$\\sqrt[8]{y^{5}}$",
            "$\\sqrt[8]{y^{7}}$",
          ],
          a: "B",
          solution:
            "Power rule: $(y^{3/4})^{3/2} = y^{(3/4)(3/2)} = y^{9/8}$. Product rule: $y^{1/8} \\cdot y^{9/8} = y^{(1+9)/8} = y^{10/8} = y^{5/4} = \\sqrt[4]{y^{5}}$. The answer is B.",
          desmosHint:
            "Open Desmos and type $y = y^{1/8} \\cdot (y^{3/4})^{3/2}$ in line 1 (use a different variable like $t$ for the independent variable). Then type $y = t^{5/4}$ in line 2 — both overlap. Now compare to $\\sqrt[4]{t^{5}} = t^{5/4}$ ✓ (option B).",
        },
        {
          n: 11,
          domain: "Algebra",
          difficulty: "hard",
          text: "Which of the following is equivalent to the expression $(\\sqrt{2q} - \\sqrt{2r})^{2/3}$ where $q > r$ and $r > 0$?",
          type: "mcq",
          o: [
            "$(2q + 2r)^{5}$",
            "$(2q - 2\\sqrt{qr} + 2r)^{1/5}$",
            "$\\sqrt[3]{2q + 2r}$",
            "$\\sqrt[3]{2q - 4\\sqrt{qr} + 2r}$",
          ],
          a: "D",
          solution:
            "First square the binomial: $(\\sqrt{2q} - \\sqrt{2r})^{2} = 2q - 2\\sqrt{4qr} + 2r = 2q - 4\\sqrt{qr} + 2r$. Then apply the $1/3$ power: $(2q - 4\\sqrt{qr} + 2r)^{1/3} = \\sqrt[3]{2q - 4\\sqrt{qr} + 2r}$. The answer is D.",
          desmosHint:
            "Open Desmos and type $y = (\\sqrt{2q} - \\sqrt{2r})^{2/3}$ with sliders for $q$ and $r$ (try $q = 5, r = 2$). Then type $y = \\sqrt[3]{2q - 4\\sqrt{qr} + 2r}$ in line 2. Both graphs overlap perfectly ✓. This visualizes the binomial expansion inside the cube root.",
        },
        {
          n: 12,
          domain: "Algebra",
          difficulty: "hard",
          text: "Which of the following is equivalent to the expression $(2\\sqrt{x} - \\sqrt{y})^{2/5}$ where $x > y$ and $y > 0$?",
          type: "mcq",
          o: [
            "$(4x - y)^{5}$",
            "$(4x - 4\\sqrt{xy} + y)^{1/5}$",
            "$\\sqrt[5]{4x - y}$",
            "$\\sqrt[5]{4x - 4xy + y}$",
          ],
          a: "B",
          solution:
            "Square the binomial: $(2\\sqrt{x} - \\sqrt{y})^{2} = 4x - 4\\sqrt{xy} + y$. Then apply the $1/5$ power: $(4x - 4\\sqrt{xy} + y)^{1/5}$. The answer is B.",
          desmosHint:
            "Open Desmos and type $y = (2\\sqrt{x} - \\sqrt{y})^{2/5}$ with sliders for $x$ and $y$ (try $x = 9, y = 4$). Then type $y = (4x - 4\\sqrt{xy} + y)^{1/5}$ in line 2. Both graphs overlap perfectly ✓.",
        },
        {
          n: 13,
          domain: "Algebra",
          difficulty: "hard",
          text: "If $\\sqrt[3]{a^{2}} = \\sqrt{b}$, $a^{2x} = b^{6}$ where $a$ and $b$ are constants with $a > 1$ and $b > 1$, what is the value of $x$?",
          type: "mcq",
          o: ["$2$", "$3$", "$4$", "$12$"],
          a: "C",
          solution:
            "Rewrite: $\\sqrt[3]{a^{2}} = a^{2/3}$ and $\\sqrt{b} = b^{1/2}$. So $a^{2/3} = b^{1/2}$. Raise to power 6: $a^{4} = b^{3}$. Then $b^{6} = (b^{3})^{2} = (a^{4})^{2} = a^{8}$. So $a^{2x} = a^{8} \\Rightarrow 2x = 8 \\Rightarrow x = 4$. The answer is C.",
          desmosHint:
            "Open Desmos and use a slider for $a$ (try $a = 2$). Compute $b = (a^{2/3})^{2} = a^{4/3}$ (from the first equation). Then verify: $a^{2x} = b^{6} = (a^{4/3})^{6} = a^{8}$, so $2x = 8$ and $x = 4$ ✓. Plot $y = 2^{2x}$ and $y = (2^{4/3})^{6}$ — they're equal when $x = 4$.",
        },
        {
          n: 14,
          domain: "Algebra",
          difficulty: "hard",
          text: "Two numbers, $a$ and $b$, are each greater than zero, and the square root of $a$ is equal to the cubic root of $b$. For what value of $x$ is $a^{(2x-1)}$ equal to $b$?",
          type: "mcq",
          o: ["$1$", "$\\frac{3}{2}$", "$\\frac{5}{4}$", "$3$"],
          a: "C",
          solution:
            "From $\\sqrt{a} = \\sqrt[3]{b}$: $a^{1/2} = b^{1/3}$. Raise to power 6: $a^{3} = b^{2}$, so $b = a^{3/2}$. Set $a^{2x-1} = b = a^{3/2}$. Equate exponents: $2x - 1 = 3/2 \\Rightarrow 2x = 5/2 \\Rightarrow x = 5/4$. The answer is C.",
          desmosHint:
            "Open Desmos and use a slider for $a$ (try $a = 4$). From $\\sqrt{a} = \\sqrt[3]{b}$: $b = a^{3/2}$. Then $a^{2x-1} = a^{3/2}$ means $2x - 1 = 3/2$, so $x = 5/4$ ✓. Plot $y = 4^{2x-1}$ and $y = 4^{3/2} = 8$ — they intersect when $x = 5/4$.",
        },'''

# Replace the empty qs: [] in lesson 3.2
old_32 = '''      strategyBody:
        "Combine like terms. For factoring: look for GCF, then difference of squares (a² − b² = (a+b)(a−b)), perfect-square trinomials, and grouping. The Remainder Theorem gives P(c) = remainder when dividing by (x − c).",
      qs: [],
    },'''

new_32 = '''      strategyBody:
        "Combine like terms. For factoring: look for GCF, then difference of squares (a² − b² = (a+b)(a−b)), perfect-square trinomials, and grouping. The Remainder Theorem gives P(c) = remainder when dividing by (x − c).",
      qs: [
''' + POLY_QS + '''
      ],
    },'''

content = content.replace(old_32, new_32, 1)

# Replace the empty qs: [] in lesson 3.4
old_34 = '''      strategyBody:
        "√(ab) = √a · √b. Rational exponents: a^(m/n) = (ⁿ√a)^m. Always rationalize denominators. For nested radicals, look for perfect-square factors first.",
      qs: [],
    },'''

new_34 = '''      strategyBody:
        "√(ab) = √a · √b. Rational exponents: a^(m/n) = (ⁿ√a)^m. Always rationalize denominators. For nested radicals, look for perfect-square factors first. When multiplying like bases, add exponents; when raising a power to a power, multiply exponents.",
      qs: [
''' + RAD_QS + '''
      ],
    },'''

content = content.replace(old_34, new_34, 1)

# Also update qrange and qcount for both lessons
content = content.replace(
    '''      id: "3.2",
      num: "3.2",
      title: "Polynomials",
      subtitle: "Operations, factoring, and roots of polynomials",
      qrange: "1 – 10",
      qcount: 10,
      timeLimit: 1500,''',
    '''      id: "3.2",
      num: "3.2",
      title: "Polynomials",
      subtitle: "Operations, factoring, and roots of polynomials",
      qrange: "1 – 5",
      qcount: 5,
      timeLimit: 900,''',
    1
)

content = content.replace(
    '''      id: "3.4",
      num: "3.4",
      title: "Radicals & Rational Exponents",
      subtitle: "Simplifying and operating on radicals",
      qrange: "1 – 10",
      qcount: 10,
      timeLimit: 1500,''',
    '''      id: "3.4",
      num: "3.4",
      title: "Radicals & Rational Exponents",
      subtitle: "Simplifying and operating on radicals",
      qrange: "6 – 14",
      qcount: 9,
      timeLimit: 1500,''',
    1
)

MODULES_FILE.write_text(content)
print("✓ Done! Added 14 questions:")
print("  - Lesson 3.2 (Polynomials): 5 questions (Q1-Q5)")
print("  - Lesson 3.4 (Radicals & Rational Exponents): 9 questions (Q6-Q14)")
print("  - Desmos hints included for Q5, Q9, Q10, Q11, Q12, Q13, Q14")
