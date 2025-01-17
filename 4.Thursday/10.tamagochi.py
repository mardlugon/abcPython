import tkinter as tk
import time
import random


I_AM_NOT_HUNGRY = "I am NOT hungry"
I_AM_NUNGRY = "I am hungry"
I_AM_HAPPY_NOW = "I am happy now"
DONT_FEED_ME = "Don't feed me"
FEED_ME = "Feed me"

window = tk.Tk()
window.title("Tamagochi")

width, height, x, y = 300, 600, 100, 150

SCREEN_WIDTH = window.winfo_screenwidth()
x = SCREEN_WIDTH//2

window.geometry (f"{width}x{height}+{x}+{y}")

print(window)

status_label = tk.Label(window, text=I_AM_NOT_HUNGRY)
status_label.pack()

counter = 0

is_hungry = False
is_game_running = True


def count():
    global counter
    print("Button was pushed")
    counter += 1
    print(f"Pushed: {counter}")
    give_food()

def give_food():
    global is_game_running
    print("give food was called")
    if is_hungry:
        print("You win")
        stop_time = time.time()
        delta = stop_time - start_time
        messagebox.showinfo(title="Congrats!", message="You win in {delta} seconds")

    else:
        print("You loose")
        messagebox.showerror(title="Uuuu", message="You lost my friend")
    
def show_i_am_houngry():
    global is_hungry
    print("Tamagoci is hungry")
    status_label.config(text=I_AM_NUNGRY)

button = tk.Button(window, text=FEED_ME, command=count, )
button.pack()

status_label.after(3000,)
start_time = time.time()


window.mainloop()