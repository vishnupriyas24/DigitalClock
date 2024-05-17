import tkinter as tk
import time
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)
root = tk.Tk()
root.title("Digital Clock")
clock_label = tk.Label(root, font=('Arial', 50), bg='black', fg='green')
clock_label.pack(padx=20, pady=20)
update_time()
root.mainloop()
