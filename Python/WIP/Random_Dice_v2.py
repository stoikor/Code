import random
import sys

dice_options = {
    "d20": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "d12": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "d10": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "d8": [1, 2, 3, 4, 5, 6, 7, 8],
    "d6": [1, 2, 3, 4, 5, 6],
    "d4": [1, 2, 3, 4]
}

if len(sys.argv) >= 2:
    dice = sys.argv[1].lower()

    if dice in dice_options:
        print(f"Rolling {dice}: {random.choice(dice_options[dice])}")
    else:
        print("Not a valid argument, please select dice: d20/d12/d10/d8/d6/d4")
else:
    print("Choose and type an argument: d20/d12/d10/d8/d6/d4")