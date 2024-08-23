import tkinter as tk
from tkinter import font, filedialog, messagebox, scrolledtext
import sys

class TextEditor:
    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.root.title("meow")
        self.file_path = None
        self.menu_visible = True

        # Set up text widget
        self.text = scrolledtext.ScrolledText(root, undo=True, wrap=tk.WORD, font=(config['DEFAULT']['font'], int(config['DEFAULT']['size'])))
        self.text.pack(fill=tk.BOTH, expand=1)

        # Set up character counter
        self.status_bar = tk.Label(root, text="Characters: 0", anchor=tk.W, font=("Arial", 10))
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        self.text.bind('<KeyRelease>', self.update_status)

        # Set up menu
        self.setup_menu()
        self.menu_bar = tk.Menu(self.root)
        self.setup_menu()
        self.root.config(menu=self.menu_bar)

        # Bind keyboard shortcuts
        self.bind_shortcuts()

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_command(label="Quit", command=self.root.quit)

        text_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Text", menu=text_menu)
        text_menu.add_command(label="Undo", command=self.text.edit_undo)
        text_menu.add_command(label="Redo", command=self.text.edit_redo)
        text_menu.add_command(label="Bold", command=self.toggle_bold)
        text_menu.add_command(label="Underscore", command=self.toggle_underscore)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About", command=self.show_about)

    def update_line_numbers(self, event=None):
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)
        
        line_count = self.text.index('end-1c').split('.')[0]
        line_numbers_content = "\n".join(str(i) for i in range(1, int(line_count) + 1))
        self.line_numbers.insert(tk.END, line_numbers_content)
        self.line_numbers.config(state=tk.DISABLED)

    def update_status(self, event=None):
        content = self.text.get(1.0, tk.END)
        char_count = len(content) - 1  # Subtract one for the trailing newline
        self.status_bar.config(text=f"Characters: {char_count}")

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("meow | New File")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())
            self.file_path = file_path
            self.root.title(f"meow | {file_path}")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension="",
                                                 filetypes=[("Custom extension", "*.")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get(1.0, tk.END))
            self.file_path = file_path
            self.root.title(f"meow | {file_path}")

    def toggle_bold(self):
        bold_font = font.Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")

        current_tags = self.text.tag_names("sel.first")
        if "bold" in current_tags:
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text.tag_add("bold", "sel.first", "sel.last")
            self.text.tag_configure("bold", font=bold_font)

    def toggle_underscore(self):
        underscore_font = font.Font(self.text, self.text.cget("font"))
        underscore_font.configure(underline=True)

        current_tags = self.text.tag_names("sel.first")
        if "underscore" in current_tags:
            self.text.tag_remove("underscore", "sel.first", "sel.last")
        else:
            self.text.tag_add("underscore", "sel.first", "sel.last")
            self.text.tag_configure("underscore", font=underscore_font)

    def show_about(self):
        messagebox.showinfo("meow", "simple Python text editor")
    
    def toggle_menu_bar(self):
        # Toggle visibility of the menu bar
        if self.menu_visible:
            self.root.config(menu=None)
            self.menu_visible = False
        else:
            self.root.config(menu=self.menu_bar)
            self.menu_visible = True
    
    def find(self, *args):
        self.text.tag_remove('found', '1.0', tk.END)
        target = tk.simpledialog.askstring('Find', 'Search String:')
        if target:
            idx = '1.0'
            while 1:
                idx = self.text.search(target, idx, nocase=1, stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(target))
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text.tag_config('found', foreground='white',    background='blue')


    def bind_shortcuts(self):
        self.root.bind('<Control-n>', lambda event: self.new_file())
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda event: self.save_as_file())
        self.root.bind('<Control-q>', lambda event: self.root.quit())
        self.root.bind('<Control-z>', lambda event: self.text.edit_undo())
        self.root.bind('<Control-Shift-Z>', lambda event: self.text.edit_redo())
        self.root.bind('<Control-b>', lambda event: self.toggle_bold())
        self.root.bind('<Control-u>', lambda event: self.toggle_underscore())
        self.root.bind('<Control-Shift-Q>', lambda event: self.toggle_menu_bar())
        self.root.bind('<Control-f>', lambda event: self.find())

