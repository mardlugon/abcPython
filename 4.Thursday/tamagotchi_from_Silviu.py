
import tkinter as tk
from tkinter import messagebox
import time
import random


## Constants (CAPITAL LETTERS ) - convention
I_AM_NOT_HUNGRY = "I am NOT hungry"
I_AM_HUNGRY = "I am hungry"
I_AM_HAPPY = "I am happy now"
DONT_FEED_ME = "Don't feed me"
FEED_ME = "Feed me"

WINDOW_SIZE = 500 

main_window = tk.Tk()

status_label = tk.Label(main_window, text=I_AM_NOT_HUNGRY)
status_label.pack()
# status_label.grid(row=0, column=0)


# feed_button.grid(row=0, column=1)

new_frame = tk.Frame(main_window)
new_frame.pack()


is_hungry = False
is_game_running = True

def give_food():
    global is_game_running
    if not is_game_running:
        return 
    
    print("give_food was called")
    # We only read the global variable
    if is_hungry:
        print("You win")
        stop_time = time.time()
        delta = stop_time - start_time 
        messagebox.showinfo(title="Congrats!", message=f"You win in {delta} seconds")
        status_label.config(text=I_AM_HAPPY)
        feed_button.config(text=DONT_FEED_ME)
        
    else:
        print("You lose")
        messagebox.showerror(title="Uuuu!!", message="You lost my friend!!!")
    is_game_running = False

def show_i_am_hundry():
    global is_hungry
    print("Tamagotchi is hungry")
    status_label.config(text=I_AM_HUNGRY)
    feed_button.config(text=FEED_ME)
    # We can the global variable
    is_hungry = True

feed_button = tk.Button(new_frame, text=DONT_FEED_ME, command=give_food)
feed_button.grid()


main_window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")

status_label.after(3000, show_i_am_hundry)
start_time = time.time()

main_window.mainloop()