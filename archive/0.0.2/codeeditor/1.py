import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

open_files = []

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        text.delete("1.0", tk.END)
        with open(file, "r") as f:
            text.insert(tk.END, f.read())
        open_files.append((file, text))  # Add the opened file to the list

def save_as():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text.get("1.0", tk.END))

def save_all():
    for file, text_widget in open_files:
        with open(file, "w") as f:
            f.write(text_widget.get("1.0", tk.END))

def update_file_list(directory):
    file_list.delete(*file_list.get_children())
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            file_list.insert("", "end", values=(item,))

def on_folder_select(event):
    selected_item = file_list.selection()
    if selected_item:
        selected_item_text = file_list.item(selected_item[0])["values"][0]
        update_file_list(os.path.join(current_directory, selected_item_text))

root = tk.Tk()
root.title("Code Editor with File List")

# Create a Treeview widget for displaying files
file_list = ttk.Treeview(root, columns=("Files",), show="tree")
file_list.heading("#0", text="Files")
file_list.pack(side=tk.LEFT, fill=tk.Y)

file_list.bind("<Double-1>", on_folder_select)

text = tk.Text(root, wrap="none")
text.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file),
file_menu.add_command(label="Save All", command=save_all)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

current_directory = os.getcwd()
update_file_list(current_directory)

root.mainloop()
