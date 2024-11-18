import customtkinter as ctk
from modules.constants import FONT, FGCOLOR, BORDERCOLOR

class LabelEntry:
    def __init__(self, master, text, row, column, labelpadx, labelpady, entrypadx, entrypady):
        self.label = ctk.CTkLabel(master, text=text+":", font=FONT)
        self.label.grid(row=row, column=column, padx=labelpadx, pady=labelpady, sticky="ew")

        self.entry = ctk.CTkEntry(master, placeholder_text=text + "...", fg_color=FGCOLOR, corner_radius=2, border_color=BORDERCOLOR, border_width=1)
        self.entry.grid(row=row+1, column=column, padx=entrypadx, pady=entrypady, sticky="ew")

    def get(self):
        return self.entry.get()
