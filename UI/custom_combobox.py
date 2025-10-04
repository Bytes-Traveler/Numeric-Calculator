import tkinter as tk
from tkinter import Frame, Listbox, StringVar
import config 

class CustomCombobox(Frame):
    def __init__(self, master, values,width=20):
        super().__init__(master, bg=config.BG_COLOR)

        self.values = values
        self.var = StringVar()
        self.is_open = False

        # Campo de texto simulado
        self.entry = tk.Entry(
            self,
            textvariable=self.var,
            font= config.COMBO_FONT,
            bg=config.ENTRY_BG,
            fg=config.ENTRY_FG,
            insertbackground=config.ENTRY_BG,
            relief='flat',
            width=width
        )
        self.entry.pack(fill='x', padx=2, pady=2)

        # Listbox desplegable
        self.listbox = Listbox(
            self,
            font=config.COMBO_FONT,
            bg=config.BG_COLOR,
            fg=config.ENTRY_FG,
            selectbackground=config.ENTRY_BG,
            selectforeground=config.ENTRY_FG,
            activestyle='none',
            height=5,
            relief='flat',
            borderwidth=0
        )
        for v in values:
            self.listbox.insert('end', v)

        # Eventos
        self.entry.bind('<Button-1>', self.toggle_listbox)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def close_listbox(self):
        self.listbox.pack_forget()
        self.is_open = False

    def toggle_listbox(self, event=None):
        if self.is_open:
            self.close_listbox()
        else:
            self.listbox.pack(fill='x')
            self.is_open = True

    def on_select(self, event=None):
        selection = self.listbox.get(self.listbox.curselection())
        self.var.set(selection)
        self.close_listbox()

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)
