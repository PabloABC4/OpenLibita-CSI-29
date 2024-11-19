import customtkinter as ctk
from modules.constants import *

class LabelEntry:
    def __init__(self, master, text, row, column, labelpadx, labelpady, entrypadx, entrypady):
        self.label = ctk.CTkLabel(master, text=text+":", font=LABELFONT)
        self.label.grid(row=row, column=column, padx=labelpadx, pady=labelpady, sticky="ew")

        self.entry = ctk.CTkEntry(master, placeholder_text=text + "...", fg_color=ENTRYFGCOLOR, corner_radius=2, border_color=ENTRYBORDERCOLOR, border_width=1)
        self.entry.grid(row=row+1, column=column, padx=entrypadx, pady=entrypady, sticky="ew")

    def get(self):
        return self.entry.get()

def create_button(master, text, command, row=0, column=0, columnspan=1, padx=0, pady=0, sticky="ew"):
    button = ctk.CTkButton(
        master,
        text=text,
        font=BUTTONFONT,
        fg_color=BUTTONFGCOLOR,
        hover_color=BUTTONHOVERCOLOR,
        text_color=BUTTONTEXTCOLOR,
        corner_radius=2,
        border_width=1,
        border_color=BUTTONBORDERCOLOR,
        command=command
    )
    button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return button
