import customtkinter as ctk

LABELFONT = ("Roboto", 14)
BUTTONFONT = ("Roboto", 14, "bold")
ENTRYFGCOLOR = "#E0DFDF"
ENTRYBORDERCOLOR = "#c2c0c0"
BUTTONFGCOLOR = "#98a164"
BUTTONHOVERCOLOR = "#5c613e"
BUTTONTEXTCOLOR = "#FFFFFF"
BUTTONBORDERCOLOR = "#585c45"

def create_label(master, text, row=0, column=0, columnspan=1, padx=0, pady=0, sticky=""):
    label = ctk.CTkLabel(master, text=text+":", font=LABELFONT)
    label.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return label

def create_entry(master, placeholder_text, row=0, column=0, columnspan=1, padx=0, pady=0, sticky=""):
    entry = ctk.CTkEntry(master, placeholder_text=placeholder_text, fg_color=ENTRYFGCOLOR, corner_radius=2, border_color=ENTRYBORDERCOLOR, border_width=1)
    entry.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return entry

def create_button(master, text, command, row=0, column=0, columnspan=1, padx=0, pady=0, sticky=""):
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
