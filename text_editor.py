import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title('Text Editor')
        self.filename = None

        # Create a text box
        self.textbox = tk.Text(self.master)
        self.textbox.pack(expand=True, fill='both')

        # Create a menu
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=self.new_file)
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_command(label='Save As', command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.master.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        # Register the menu in the window
        self.master.config(menu=menubar)

    def new_file(self):
        self.filename = None
        self.textbox.delete(1.0, tk.END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if self.filename:
            with open(self.filename, 'r') as f:
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(1.0, f.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(self.textbox.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(self.textbox.get(1.0, tk.END))

root = tk.Tk()
app = TextEditor(root)
root.mainloop()