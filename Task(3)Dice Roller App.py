import tkinter as tk
from tkinter import Label, Button, OptionMenu
import random

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller App")
        self.master.geometry("300x200")

        self.label_select_dice = Label(master, text="Select the number of dice:",fg="red",font="arial 20 bold")
        self.label_select_dice.pack(pady=10)

        self.num_dice_options = [1, 2, 3, 4, 5,6]
        self.selected_num_dice = tk.IntVar()
        self.selected_num_dice.set(self.num_dice_options[0])

        self.dropdown_num_dice = OptionMenu(master, self.selected_num_dice, *self.num_dice_options)
        self.dropdown_num_dice.pack(pady=10)

        self.roll_button = Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def roll_dice(self):
        num_dice = self.selected_num_dice.get()
        dice_results = [random.randint(1, 6) for _ in range(num_dice)]
        result_text = f"Result: {dice_results}"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
