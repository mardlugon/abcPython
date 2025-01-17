import tkinter as tk

window = tk.Tk()
window.title("Hello Guys")

width, height, x, y = 300, 600, 100, 150

SCREEN_WIDTH = window.winfo_screenwidth()
x = SCREEN_WIDTH//2

window.geometry (f"{width}x{height}+{x}+{y}")

print(window)

window.mainloop()

