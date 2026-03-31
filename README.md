# Expert System Mini Project (Teaching Version)

## Overview
You will build a simple **rule-based expert system** using **forward chaining**.

### Files Provided
| File | Description | Status |
|------|--------------|---------|
| `engine.py` | Core inference engine | Incomplete (you implement key functions) |
| `kb_loader.py` | Loads JSON knowledge base | Complete |
| `kb/laptop_rules.json` | Sample KB (1 rule only) | Incomplete (you add 9 more) |
| `main.py` | Command-line interface | Incomplete |
| `tests/` | Folder for test cases | Empty |

---

## Your Tasks

1. **Implement the inference logic**
   - Complete `can_fire()`, `run()`, and `conclusions()` in `engine.py`.

2. **Expand the knowledge base**
   - Add at least **9 more rules** to `kb/laptop_rules.json`.

3. **Complete `main.py`**
   - Load rules.
   - Collect user facts.
   - Run inference.
   - Display recommendations and which rules fired.

4. **(Optional) Bonus**
   - Implement explanations: *“Why”* and *“How”* reasoning.
   - Add uncertainty or confidence factors.

---

## Example Run (after completion)

```
Is portability important? (y/n): y
Do you need long battery life? (y/n): y
Is your budget high? (y/n): y

=> Recommendation: premium_ultrabook
=> Explanation: derived from rule 'Premium Ultrabook'
```

---

## Grading Rubric (100 pts)

| Component | Points |
|------------|--------|
| Inference engine (`engine.py`) | 40 |
| Rule base completeness | 20 |
| Correct reasoning output | 20 |
| Code readability & structure | 10 |
| Report / explanation clarity | 10 |

---
