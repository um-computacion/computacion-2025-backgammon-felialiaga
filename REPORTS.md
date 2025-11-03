# Automated Reports
## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
cli/CLI.py                115     13    89%   83, 89, 91, 97, 99, 108-111, 114, 116, 154, 157-158
cli/__init__.py             0      0   100%
core/Board.py              82      2    98%   132-133
core/Checker.py            30      0   100%
core/Dice.py               29      1    97%   31
core/Game.py               82      8    90%   41, 74, 78-84, 95
core/Player.py              8      0   100%
core/__init__.py            0      0   100%
pygame_ui/__init__.py       0      0   100%
tests/__init__.py           0      0   100%
tests/test_board.py       200     10    95%   179, 225-226, 244-245, 254-255, 286-287, 315
tests/test_checker.py      73      1    99%   93
tests/test_cli.py         108      1    99%   138
tests/test_dice.py         48      1    98%   61
tests/test_game.py        183      1    99%   283
tests/test_player.py       24      1    96%   34
-----------------------------------------------------
TOTAL                     982     39    96%

```
## Pylint Report
```text
=== Running Pylint on core ===
************* Module computacion-2025-backgammon-felialiaga.core.Dice
core/Dice.py:41:0: C0304: Final newline missing (missing-final-newline)
core/Dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/Dice.py:1:0: C0103: Module name "Dice" doesn't conform to snake_case naming style (invalid-name)
core/Dice.py:3:0: C0115: Missing class docstring (missing-class-docstring)
core/Dice.py:9:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Dice.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Dice.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Dice.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Dice.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Dice.py:40:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module computacion-2025-backgammon-felialiaga.core.Game
core/Game.py:111:0: C0304: Final newline missing (missing-final-newline)
core/Game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/Game.py:1:0: C0103: Module name "Game" doesn't conform to snake_case naming style (invalid-name)
core/Game.py:1:0: E0401: Unable to import 'core.Board' (import-error)
core/Game.py:2:0: E0401: Unable to import 'core.Player' (import-error)
core/Game.py:3:0: E0401: Unable to import 'core.Dice' (import-error)
core/Game.py:5:0: C0115: Missing class docstring (missing-class-docstring)
core/Game.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:70:11: R1714: Consider merging these comparisons with 'in' by using 'destino in (25, 0)'. Use a set instead if elements are hashable. (consider-using-in)
core/Game.py:43:4: R0911: Too many return statements (7/6) (too-many-return-statements)
core/Game.py:92:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:98:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:101:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:104:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Game.py:107:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module computacion-2025-backgammon-felialiaga.core.Board
core/Board.py:6:52: C0303: Trailing whitespace (trailing-whitespace)
core/Board.py:7:37: C0303: Trailing whitespace (trailing-whitespace)
core/Board.py:8:38: C0303: Trailing whitespace (trailing-whitespace)
core/Board.py:133:0: C0304: Final newline missing (missing-final-newline)
core/Board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/Board.py:1:0: C0103: Module name "Board" doesn't conform to snake_case naming style (invalid-name)
core/Board.py:1:0: E0401: Unable to import 'core.Checker' (import-error)
core/Board.py:3:0: C0115: Missing class docstring (missing-class-docstring)
core/Board.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:27:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:27:4: C2401: Function name "añadir_ficha" contains a non-ASCII character, consider renaming it. (non-ascii-name)
core/Board.py:31:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:54:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:61:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:64:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Board.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module computacion-2025-backgammon-felialiaga.core.exceptions
core/exceptions.py:17:0: C0304: Final newline missing (missing-final-newline)
core/exceptions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/exceptions.py:1:0: C0115: Missing class docstring (missing-class-docstring)
core/exceptions.py:4:0: C0115: Missing class docstring (missing-class-docstring)
core/exceptions.py:7:0: C0115: Missing class docstring (missing-class-docstring)
core/exceptions.py:10:0: C0115: Missing class docstring (missing-class-docstring)
core/exceptions.py:13:0: C0115: Missing class docstring (missing-class-docstring)
core/exceptions.py:16:0: C0115: Missing class docstring (missing-class-docstring)
************* Module computacion-2025-backgammon-felialiaga.core.Player
core/Player.py:15:0: C0304: Final newline missing (missing-final-newline)
core/Player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/Player.py:1:0: C0103: Module name "Player" doesn't conform to snake_case naming style (invalid-name)
core/Player.py:3:0: C0115: Missing class docstring (missing-class-docstring)
core/Player.py:11:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Player.py:14:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module computacion-2025-backgammon-felialiaga.core.Checker
core/Checker.py:10:0: C0303: Trailing whitespace (trailing-whitespace)
core/Checker.py:11:34: C0303: Trailing whitespace (trailing-whitespace)
core/Checker.py:12:33: C0303: Trailing whitespace (trailing-whitespace)
core/Checker.py:13:32: C0303: Trailing whitespace (trailing-whitespace)
core/Checker.py:49:0: C0304: Final newline missing (missing-final-newline)
core/Checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/Checker.py:1:0: C0103: Module name "Checker" doesn't conform to snake_case naming style (invalid-name)
core/Checker.py:2:0: C0115: Missing class docstring (missing-class-docstring)
core/Checker.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Checker.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Checker.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Checker.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Checker.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Checker.py:33:4: C0116: Missing function or method docstring (missing-function-docstring)
core/Checker.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 6.05/10


=== Running Pylint on Tests ===
************* Module Tests
Tests:1:0: F0001: No module named Tests (fatal)

```
