#Number Guessing Game
'''using some basic , advance modules and funtion or class to create a program called number guessing game .'''

#import python  basic and some advance  libaries
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

#to get random no.
import random

'''A class define to game and some funtion under the class
to start , reset ,submit , play again and main function its called _init_ fuction'''

class Game:
    def __init__(self,Game_master):
        
        self.Game_master= Game_master
        self.Game_master.title("NUMBER GUESSING GAME")                      #the title of game
        self.Game_master.geometry("500x250")                                #size


        self.label=Label(Game_master,text="Enter your name:")               #the cammond for user to enter her name
        self.label.pack(pady=5)

        self.entry_name = Entry(Game_master)
        self.entry_name.pack(pady=5)
        
        self.result_label = Label(Game_master, text="")                          #entry field for user enter name
        self.result_label.pack()
        
        self.start_button = Button(Game_master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)                                     #button to start the game

        self.reset_game()
        
    def start_game(self):
        
        self.player_name = self.entry_name.get()                            #to get player name

        if not self.player_name:
            messagebox.showwarning("Warning", "Please enter your name.")    #warning to user pls enter your name
            return

        self.label.pack_forget()
        self.entry_name.pack_forget()
        self.start_button.pack_forget()

        self.label.config(text=f"Welcome, {self.player_name}!")             #to welcoome user
        self.label.pack(pady=10)

        self.entry_guess = Entry(self.Game_master)                               #entry  field for guessing number
        self.entry_guess.pack(pady=5)

        self.guess_button = Button(self.Game_master, text="Submit Guess", command=self.submit_guess)
        self.guess_button.pack(pady=10)                                     #button for submit guess no.

        
    def reset_game(self):
        self.secret_number = random.randint(1, 100)                         #random number between 1 to 100
        self.attempts = 0
        self.player_name = ""

        
    def submit_guess(self):                                                 #function to show the result of user guess number
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < self.secret_number:
                result_text = "low! Try again."
            elif guess > self.secret_number:
                result_text = "high! Try again."
            else:
                result_text = f"Congratulations, {self.player_name}! You guessed the number in {self.attempts} attempts."
                result_text += "\nDo you want to play again?"

            self.result_label.config(text=result_text)

            if result_text.endswith("Do you want to play again?"):
                self.reset_game()
                self.entry_guess.pack_forget()
                self.guess_button.pack_forget()

                self.play_again_button = Button(self.Game_master, text="Play Again", command=self.play_again)
                self.play_again_button.pack(pady=10)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number.")

            
    def play_again(self):
        self.label_name.pack_forget()
        self.play_again_button.pack_forget()
        
        self.result_label.config(text="")
        
        self.start_button.pack(pady=10)
        self.reset_game()            
if __name__ == "__main__":
    root = tk.Tk()
    
    app =Game(root)
    
    root.mainloop()
    
