import tkinter as tk

window = tk.Tk()
window.title("Hello Guys")

width, height, x, y = 300, 600, 100, 150

SCREEN_WIDTH = window.winfo_screenwidth()
x = SCREEN_WIDTH//2

window.geometry (f"{width}x{height}+{x}+{y}")

print(window)

label = tk.Label(window, text="Two more days of fun")
label.pack()
label1 = tk.Label(window, text="or thre more days ")
label1.pack()

counter = 0

def count():
    global counter
    print("Button was pushed")
    counter += 1
    print(f"Pushed: {counter}")


button = tk.Button(window, text="Push me", command=count)
button.pack()

window.mainloop()