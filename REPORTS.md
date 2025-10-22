# Automated Reports
## Coverage Report
```text
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
cli/__init__.py            0      0   100%
core/Board.py            143    120    16%   12-16, 20-28, 32-71, 74, 78-81, 84-87, 90-93, 97-100, 104-105, 123-130, 134-143, 153-172, 177-180, 187-196, 200-250, 257-258
core/Checker.py           10      6    40%   7, 10, 14-19
core/Dice.py              32      9    72%   10-20, 51
core/Player.py            30      5    83%   10-13, 34, 38
core/__init__.py           0      0   100%
core/exceptions.py         8      0   100%
tests/__init__.py          0      0   100%
tests/test_board.py        2      0   100%
tests/test_cli.py          1      0   100%
tests/test_dice.py        26      1    96%   46
tests/test_game.py         1      0   100%
tests/test_player.py      30      1    97%   52
----------------------------------------------------
TOTAL                    283    142    50%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
