<div align="center">

# 🚀 Codeforces Journey & Solutions

[![Codeforces Profile](https://img.shields.io/badge/Codeforces-_vishalgupta_-blue?style=for-the-badge&logo=codeforces)](https://codeforces.com/profile/_vishalgupta_)
[![Language](https://img.shields.io/badge/Language-Java-orange?style=for-the-badge&logo=openjdk)](https://www.java.com/)
[![Auto Sync](https://img.shields.io/badge/Sync-GitHub%20Actions-brightgreen?style=for-the-badge&logo=githubactions)](https://github.com/VishalGCode/codeforces-practice-problems/actions)

---

> A living, automated repository documenting my complete competitive programming journey on Codeforces in strict chronological order, organized by rating brackets.

</div>

---

## 📌 Repository Overview

* **Automatic Scraping:** Solutions and metadata are fetched directly via Python scripts using the Codeforces API & GitHub Actions.
* **Rating Organization:** Problem files are grouped into rating brackets (`rating-0800-1000`, `rating-1000-1200`, etc.).
* **Sequential Journey:** Problems are assigned a sequential serial number (`#001`, `#002`, ...) to reflect exact progress over time.

---

## 📊 Directory Structure

```text
codeforces-practice-problems/
├── .github/workflows/   # GitHub Actions automated workflow
├── scripts/             # Python scraping & generator scripts
├── solutions/           # Java solutions categorized by rating bracket
│   ├── rating-0800-1000/
│   └── rating-1000-1200/
└── README.md            # Progress log & index
| 001 | [4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem4A_Watermelon.java) |
| 002 | [2244B - Nikita and Books](https://codeforces.com/problemset/problem/2244/B) | 800 | [Java Solution](solutions/rating-0800-1000/Problem2244B_NikitaandBooks.java) |
| 003 | [1903A - Halloumi Boxes](https://codeforces.com/problemset/problem/1903/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1903A_HalloumiBoxes.java) |
| 004 | [1901A - Line Trip](https://codeforces.com/problemset/problem/1901/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1901A_LineTrip.java) |
| 005 | [2240A - Another Popcount Problem](https://codeforces.com/problemset/problem/2240/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem2240A_AnotherPopcountProblem.java) |
| 006 | [1900A - Cover in Water](https://codeforces.com/problemset/problem/1900/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1900A_CoverinWater.java) |
| 007 | [1899A - Game with Integers](https://codeforces.com/problemset/problem/1899/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1899A_GamewithIntegers.java) |
| 008 | [1896A - Jagged Swaps](https://codeforces.com/problemset/problem/1896/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1896A_JaggedSwaps.java) |
| 009 | [1890A - Doremy's Paint 3](https://codeforces.com/problemset/problem/1890/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1890A_DoremysPaint3.java) |
| 010 | [1881A - Don't Try to Count](https://codeforces.com/problemset/problem/1881/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1881A_DontTrytoCount.java) |
| 011 | [1878A - How Much Does Daytona Cost?](https://codeforces.com/problemset/problem/1878/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1878A_HowMuchDoesDaytonaCost.java) |
| 012 | [1877A - Goals of Victory](https://codeforces.com/problemset/problem/1877/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1877A_GoalsofVictory.java) |
| 013 | [2256A - Three Numbers on the Blackboard](https://codeforces.com/problemset/problem/2256/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem2256A_ThreeNumbersontheBlackboard.java) |
| 014 | [1873C - Target Practice](https://codeforces.com/problemset/problem/1873/C) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1873C_TargetPractice.java) |
| 015 | [1866A - Ambitious Kid](https://codeforces.com/problemset/problem/1866/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1866A_AmbitiousKid.java) |
| 016 | [1862B - Sequence Game](https://codeforces.com/problemset/problem/1862/B) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1862B_SequenceGame.java) |
| 017 | [1859A - United We Stand](https://codeforces.com/problemset/problem/1859/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1859A_UnitedWeStand.java) |
| 018 | [1858A - Buttons](https://codeforces.com/problemset/problem/1858/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1858A_Buttons.java) |
| 019 | [1857A - Array Coloring](https://codeforces.com/problemset/problem/1857/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1857A_ArrayColoring.java) |
| 020 | [1853A - Desorting](https://codeforces.com/problemset/problem/1853/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1853A_Desorting.java) |
| 021 | [1845A - Forbidden Integer](https://codeforces.com/problemset/problem/1845/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1845A_ForbiddenInteger.java) |
| 022 | [1837A - Grasshopper on a Line](https://codeforces.com/problemset/problem/1837/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1837A_GrasshopperonaLine.java) |
| 023 | [1834A - Unit Array](https://codeforces.com/problemset/problem/1834/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1834A_UnitArray.java) |
| 024 | [1831A - Twin Permutations](https://codeforces.com/problemset/problem/1831/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1831A_TwinPermutations.java) |
| 025 | [1829B - Blank Space](https://codeforces.com/problemset/problem/1829/B) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1829B_BlankSpace.java) |
| 026 | [1814A - Coins](https://codeforces.com/problemset/problem/1814/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1814A_Coins.java) |
| 027 | [1806A - Walking Master](https://codeforces.com/problemset/problem/1806/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1806A_WalkingMaster.java) |
| 028 | [1805A - We Need the Zero](https://codeforces.com/problemset/problem/1805/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1805A_WeNeedtheZero.java) |
| 029 | [1791C - Prepend and Append](https://codeforces.com/problemset/problem/1791/C) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1791C_PrependandAppend.java) |
| 030 | [1761A - Two Permutations](https://codeforces.com/problemset/problem/1761/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1761A_TwoPermutations.java) |
| 031 | [1789A - Serval and Mocha's Array](https://codeforces.com/problemset/problem/1789/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1789A_ServalandMochasArray.java) |
| 032 | [1788A - One and Two](https://codeforces.com/problemset/problem/1788/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1788A_OneandTwo.java) |
| 033 | [1783A - Make it Beautiful](https://codeforces.com/problemset/problem/1783/A) | 800 | [Java Solution](solutions/rating-0800-1000/Problem1783A_MakeitBeautiful.java) |
