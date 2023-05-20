# paint can calculator
from math import ceil


def paint_calc(height, width, cover):
    return ceil(height * width / cover)

test_h = int(input("What is the height of the wall (m):\n>> "))
test_w = int(input("What is the width of the wall (m):\n>> "))
coverage = 5

cans_needed = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You require {cans_needed} of paint.")
