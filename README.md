# LeetCode Solutions

A collection of my accepted LeetCode solutions, organized by topic.

- **Language:** Python (primary)
- **Problems Solved:** 150+
- **Topics Covered:**
  - Arrays & Strings
  - Hash Maps
  - Two Pointers / Sliding Window
  - Trees & Graphs
  - Dynamic Programming
  - Backtracking
  - Greedy
  - Binary Search

## Structure

```
LeetCode/
├── Sliding Window/
│   └── 1004. Max Consecutive Ones III/
│       ├── 1004. Max Consecutive Ones III.py
│       └── 1004. Max Consecutive Ones III.md
├── Tree/
│   └── 236. Lowest Common Ancestor of a Binary Tree/
│       ├── 236. Lowest Common Ancestor of a Binary Tree.py
│       └── 236. Lowest Common Ancestor of a Binary Tree.md
└── ...
```

Each problem gets its own subfolder named `<problem-number>. <Problem Title>`, placed under the single topic folder that best matches its core technique (e.g. a problem tagged both `Array` and `Sliding Window` lands under `Sliding Window`, since that's the more specific, technique-defining tag). Inside each subfolder:

- `<problem-number>. <Problem Title>.<ext>` — my latest accepted submission
- `<problem-number>. <Problem Title>.md` — problem statement, difficulty, the chosen folder topic, and the full list of LeetCode topic tags

## How this repo is maintained

Solutions were bulk-exported using a custom Python script (`leetcode_export.py`) that pulls accepted submissions directly from LeetCode's API, picks the single most relevant topic for each problem from its full tag list using a priority ranking (specific techniques like `Sliding Window` or `Dynamic Programming` outrank generic tags like `Array` or `Math`), and writes the solution and a README into that topic's folder.

## Why this repo exists

Tracking DSA practice for placement preparation, and keeping a public record of consistent problem-solving over time.


## Extension for firefox:
[Firefox Addon](https://addons.mozilla.org/en-US/firefox/addon/leethub-v4-by-fizzy444/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)
