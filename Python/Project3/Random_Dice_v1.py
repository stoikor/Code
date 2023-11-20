import random
from sys import argv

d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d12 = [1,2,3,4,5,6,7,8,9,10,11,12,]
d10 = [1,2,3,4,5,6,7,8,9,10]
d8 = [1,2,3,4,5,6,7,8]
d6 = [1,2,3,4,5,6]
d4 = [1,2,3,4]

if len(argv) >=2:
    dice = argv[1]

    if dice == "d20":
        print(random.choice(d20))
    elif dice == "d12":
        print(random.choice(d12))
    elif dice == "d10":
        print(random.choice(d10))  
    elif dice == "d8":
        print(random.choice(d8))
    elif dice == "d6":
        print(random.choice(d6))
    elif dice == "d4":
        print(random.choice(d4))             
    else:
        print("Not a valid argument, please select dice : d20/d12/d10/d8/d6/d4")
else:
    print("Choose and type an argument : d20/d12/d10/d8/d6/d4")        