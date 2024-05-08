import tkinter as tk
import os


def show_files():
    folder_path = entry.get()
    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        listbox.delete(0, tk.END)
        for file in files:
            listbox.insert(tk.END, file)
    else:
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, "Invalid directory. Please enter a valid path.")


root = tk.Tk()
root.title("File Browser")

entry = tk.Entry(root, width=50)
entry.pack(pady=20)

button = tk.Button(root, text="Display Files", command=show_files)
button.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

root.mainloop()
