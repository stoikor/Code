import tkinter as tk
import random

dice_options = {
    "d20": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "d12": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "d10": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "d8": [1, 2, 3, 4, 5, 6, 7, 8],
    "d6": [1, 2, 3, 4, 5, 6],
    "d4": [1, 2, 3, 4]
}

def rolld20():
    result_label.config(text=("You Got:") + str(random.choice(dice_options["d20"])))
def rolld12():
    result_label.config(text=("You Got:") + str(random.choice(dice_options["d12"])))
def rolld10():
    result_label.config(text=("You Got:") + str(random.choice(dice_options["d10"])))
def rolld8():
    result_label.config(text=("You Got:") + str(random.choice(dice_options["d8"])))
def rolld6():
    result_label.config(text=("You Got:") + str(random.choice(dice_options["d6"])))
def rolld4():
    result_label.config(text=("You Got:") + str(random.choice(dice_options["d4"])))

root = tk.Tk()
root.title("Dice roller")

label = tk.Label(root, text="Test")
label.pack()

button_d20 = tk.Button(root, text="d20", command=rolld20)
button_d20.pack()
button_d12 = tk.Button(root, text="d12", command=rolld12)
button_d12.pack()
button_d10 = tk.Button(root, text="d10", command=rolld10)
button_d10.pack()
button_d8 = tk.Button(root, text="d8", command=rolld8)
button_d8.pack()
button_d6 = tk.Button(root, text="d6", command=rolld6)
button_d6.pack()
button_d4 = tk.Button(root, text="d4", command=rolld4)
button_d4.pack()

exit = tk.Button(root, text="Close me, daddy", command=root.destroy)
exit.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()