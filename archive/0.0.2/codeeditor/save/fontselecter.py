import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme="clearlooks")  # Örnek bir tema adı

def change_theme():
    new_theme = theme_combobox.get()  # Tema adını alın
    root.set_theme(new_theme)  # Tema adını ayarlayın

theme_combobox = ttk.Combobox(root, values=root.get_themes())
theme_combobox.pack()
theme_button = ttk.Button(root, text="Tema Değiştir", command=change_theme)
theme_button.pack()
