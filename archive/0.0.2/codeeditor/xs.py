import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import tkinter.ttk as ttk
import os
from ttkthemes import ThemedTk

themes = ThemedTk().get_themes()

# Tema değiştirici fonksiyon
def change_theme(theme):
    app.set_theme(theme)
    
# ThemedTk ile bir uygulama örneği oluştur
app = ThemedTk()
app.title("Tema Değiştirici")

color = ttk.Style().lookup("TFrame", "background", default="white")
app.configure(bg=color)

background_frame = ttk.Frame(app)
background_frame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

def new_file():
    text.delete("1.0", tk.END)

def open_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        text.delete("1.0", tk.END)
        text.insert("1.0", content)
        
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)

def about():
    messagebox.showinfo("About", "Simple Code Editor\nCreated with Tkinter")

def open_directory():
    global current_directory
    current_directory = filedialog.askdirectory()
    if current_directory:
        update_file_list()

def update_file_list():
    file_listbox.delete(0, tk.END)
    file_list = os.listdir(current_directory)
    for file_name in file_list:
        file_listbox.insert(tk.END, file_name)

def on_file_select(event):
    selected_file = file_listbox.get(file_listbox.curselection())
    if selected_file:
        open_file(os.path.join(current_directory, selected_file))

app.title("OGZ Code Editor")


menu_bar = tk.Menu(app)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
file_menu.add_command(label="Exit", command=app.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

theme_menu = tk.Menu(settings_menu, tearoff=0)
settings_menu.add_cascade(label="Tema Seç", menu=theme_menu)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Kullanılabilir temaları al
themes = app.get_themes()

# Her tema için bir komut ekle
for theme in themes:
    theme_menu.add_command(label=theme, command=lambda t=theme: change_theme(t))

# Birkaç ttk widget'ı ekle
label = ttk.Label(app, text="Üst menü")
label.pack(pady=10)

app.config(menu=menu_bar)

text = scrolledtext.ScrolledText(app, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

current_directory = None

left_frame = tk.Frame(app)

# Sol çerçeveyi yatay olarak değil, sadece dikey olarak doldur
left_frame.pack(side=tk.LEFT, fill=tk.Y)

file_listbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, width=20)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
file_listbox.bind("<Double-Button-1>", on_file_select)

# Butonları sol çerçevenin üst kısmına yerleştir
open_button = tk.Button(left_frame, text="Dizin Aç", command=open_directory)
open_button.pack(side=tk.TOP)

update_file_list_button = tk.Button(left_frame, text="Dosya Listesini Güncelle", command=update_file_list)
update_file_list_button.pack(side=tk.TOP)

app.mainloop()
