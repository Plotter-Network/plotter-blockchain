from typing import Dict

# The rest of the codebase uses rows everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "plotter": 10 ** 12,  # 1 plotter (PLTR) is 1,000,000,000 rows (1 billion)
    "rows:": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin mojos
}
