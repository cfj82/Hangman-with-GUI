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
    img_lbl.config(image=photos[00])  # placed here for when run will show at start
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
                img_lbl.config(image=photos[lives])  # photo number is same as lives
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
root.geometry('500x350')
root.configure(bg="black")
root.columnconfigure(0, weight=1)

photos = [PhotoImage(file='1.png'),PhotoImage(file="2.png"),PhotoImage(file="3.png"),
          PhotoImage(file="4.png"),PhotoImage(file="5.png"),PhotoImage(file="6.png"),PhotoImage(file="00.png")]

f0 = Frame(root, bg="black")  # ---- hint
f0.pack(expand=True)

# visuals
img_lbl = Label(f0)
img_lbl.grid(row=0, rowspan=4, column=0, sticky='nswe')
img_lbl.config(image=photos[00])  # placed here for when run will show at start

# ---- hint
hintLbl = StringVar()
hint_lbl = Label(f0, font=("verdana", 20, "bold"), anchor="center", relief=SUNKEN, border=15,
                 bg="#5DADE2", textvariable=hintLbl)
hint_lbl.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='nswe')

# enter
guessed_letter = StringVar()
enter = Entry(f0, font=("verdana", 20), relief=RIDGE, border=15, justify="center",
              bg="#744697", textvariable=guessed_letter)
enter.grid(row=2,  column=1, columnspan=2, padx=5, pady=5, sticky='nswe')
enter.bind('<Return>', guess)
enter.focus()

# lives left
lives_output = StringVar()
lbl = Label(f0, font=("verdana", 20), anchor="center", relief=FLAT, border=15,
            bg="#5DADE2", textvariable=lives_output)
lbl.grid(row=3,  column=1, columnspan=2, padx=5, pady=5, sticky='nswe')

# new game and quit buttons
new_btn = Button(f0, font=("verdana", 15), anchor="center", relief=RAISED, border=10,
                 bg="#5DADE2", text="New Game", command=new_game)
new_btn.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')

quit_btn = Button(f0, font=("verdana", 15), anchor="center", relief=RAISED, border=10,
                  bg="#5DADE2", text="Quit", command=quit)
quit_btn.grid(row=0, column=2, padx=5, pady=5, sticky='nswe')


# create menu
my_menu = Menu(root)
root.config(menu = my_menu)

# create options dropdown for menu
option_menu = Menu(my_menu, tearoff=False, background="gray", fg="white")  # tearoff is dotted line.... ugly
my_menu.add_cascade(label="Options", menu = option_menu)  # create drop down for menu
option_menu.add_command(label = "New Game", command = new_game)  # create item for drop down menu
option_menu.add_separator()        # adds line to separate
option_menu.add_command(label = "Quit", command = quit)  # create item for drop down menu


root.mainloop()
