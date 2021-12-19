# hangman
import string
from tkinter import *
from tkinter import messagebox
import random


word_bank = ["dog", "tiffany", "python", "home", "orange"]


def new_game():
    global hint_word
    global word
    global lives
    lives = 7
    word = random.choice(word_bank)
    hint_word = "".join("*" * len(word))  # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
    hintLbl.set(hint_word)  # set output of hint with *
    return word.upper()


def guess(event):
    global word
    global hint_word
    global lives
    lives_output.set("You Have " + str(lives) + " Left")
    guessed_letters = []  # empty set for used letters
    word_letters = list(word)  # make word as set
    if lives > 0:
        letter_guess = enter.get()
        if letter_guess.isalpha() and len(letter_guess) == 1:  # entry is letter and length 1
            #  .isalpha() checks True False a letter from alphabet
            if letter_guess not in word_letters:
                lives -= 1  # lose life for wrong guess
                guessed_letters.append(letter_guess)  # add guess letter to guessed letters bank
                enter.delete(0, END)
                lives_output.set("You Have " + str(lives) + " Left")
            else:  # guess in word
                guessed_letters.append(letter_guess)  # add guessed letter to guessed letters bank
                word_as_list = list(hint_word)  # convert word from string to list so can index letters
                # need to find all indices where guess occur in word... use list comprehension
                # call enumerate on word to get index and letter at index
                # for each iteration if corresponding letter = guess
                indices = [i for i, letter in enumerate(word) if letter == letter_guess]
                for index in indices:  # for loop over indices to replace each * at index with letter_guessed
                    word_as_list[index] = letter_guess
                hint_word = ''.join(word_as_list)  # update word hint, .join() will remove ""
                hintLbl.set(hint_word)
                enter.delete(0, END)

            if "*" not in hint_word:  # win game
                hintLbl.set("You Win!")
                quit()

            if lives == 0:  # lose game
                hintLbl.set("Game Over, You Lose")
                quit()

def quit():
    msg = messagebox.askyesno("Quit", "Do You Want To Quit?")
    if msg:
        root.destroy()

root = Tk()
root.title("Hangman")
root.configure(width=500, height=550, bg="black")

f0 = Frame(root, bg="black")  # ---- hint
f0.pack(fill="both", expand=True)
f1 = Frame(root, bg="black")
f1.pack(fill="both", expand=True)
f2 = Frame(root, bg="black")
f2.pack(fill="both", expand=True)
f3 = Frame(root, bg="black")
f3.pack(fill="both", expand=True)
f4 = Frame(root, bg="black")
f4.pack(fill="both", expand=True)

# hangman
title_lbl = Label(f0, font=("verdana", 20, "bold", "italic"), anchor="center", relief=FLAT, border=15,
                  bg="#5DADE2", text="--- HANGMAN ---")
title_lbl.pack(fill="both", expand=True, padx=25, pady=5)

# ---- hint
hintLbl = StringVar()
hint_lbl = Label(f1, font=("verdana", 28, "bold"), anchor="center", relief=SUNKEN, border=15,
                 bg="#5DADE2", textvariable=hintLbl)
hint_lbl.pack(fill="both", expand=True, padx=40, pady=5)

# enter
guessed_letter = StringVar()
enter = Entry(f2, font=("verdana", 22), relief=RIDGE, border=15, justify="center",
              bg="#744697", textvariable=guessed_letter)
enter.pack(fill="both", expand=True, padx=60, pady=5)
enter.bind('<Return>', guess)
enter.focus()

# lives left
lives_output = StringVar()
lbl = Label(f3, font=("verdana", 14), anchor="center", relief=FLAT, border=15,
            bg="#5DADE2", textvariable=lives_output)
lbl.pack(fill="both", expand=True, padx=20, pady=5)

# new game and quit buttons
new_btn = Button(f4, font=("verdana", 12), anchor="center", relief=RAISED, border=10,
                 bg="#5DADE2", text="New Game", command=new_game)
new_btn.pack(side=LEFT, fill="both", expand=True, padx=15, pady=5)

quit_btn = Button(f4, font=("verdana", 12), anchor="center", relief=RAISED, border=10,
                  bg="#5DADE2", text="Quit", command=quit)
quit_btn.pack(side=LEFT, fill="both", expand=True, padx=15, pady=5)


root.mainloop()
