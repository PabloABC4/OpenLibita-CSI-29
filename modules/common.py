import tkinter as tk
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

def create_button(master, text, command, row=None, column=None, columnspan=1, padx=0, pady=0, sticky=""):
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
    if row is not None and column is not None:
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return button

class Pagination:
    def __init__(self, master, data, columns, items_per_page, format_func, column_widths=None):
        self.data = data
        self.columns = columns      
        self.items_per_page = items_per_page
        self.current_index = 0
        self.format = format_func
        self.column_widths = column_widths if column_widths else [100] * len(columns)

        for widget in master.winfo_children():
            widget.destroy()

        for i in range(len(columns)):
            master.grid_columnconfigure(i, weight=1)

        self.canvas = tk.Canvas(master)
        self.canvas.grid(row=0, column=0, columnspan=len(self.columns), padx=80, pady=(120, 10), sticky="nsew")

        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        h_scroll = tk.Scrollbar(master, orient="horizontal", command=self.canvas.xview)
        h_scroll.grid(row=1, column=0, columnspan=len(self.columns), padx=80, sticky="ew")
        self.canvas.configure(xscrollcommand=h_scroll.set)

        self.scrollable_frame.bind("<Configure>", self.update_scrollregion)

        self.previous_page_button = create_button(master, "Página Anterior", self.previous_page, row=2, column=0, padx=(80, 5), pady=10, sticky="W")
        self.next_page_button = create_button(master, "Próxima Página", self.next_page, row=2, column=len(self.columns)-1, padx=(5, 80), pady=10, sticky="E")

        self.display()

    def update_scrollregion(self, event): 
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def next_page(self):
        self.current_index += 1
        self.display()

    def previous_page(self):
        self.current_index -= 1
        self.display()

    def display(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for col_index, col in enumerate(self.columns):
            col_label = ctk.CTkLabel(master=self.scrollable_frame, text=col, font=("Roboto", 12, 'bold'))
            col_label.grid(row=0, column=col_index, padx=5, pady=2, sticky='ew')
            self.scrollable_frame.grid_columnconfigure(col_index, weight=1, minsize=self.column_widths[col_index])

        current_page_data = self.data[self.items_per_page * self.current_index: self.items_per_page * (self.current_index + 1)]
        for i, item in enumerate(current_page_data):
            formatted_data = self.format(item)
            for j, value in enumerate(formatted_data):
                value_label = ctk.CTkLabel(master=self.scrollable_frame, text=value)
                value_label.grid(row=i + 1, column=j, padx=5, pady=2)

        self.previous_page_button.configure(state="normal" if self.current_index > 0 else "disabled")
        self.next_page_button.configure(state="normal" if self.items_per_page * (self.current_index + 1) < len(self.data) else "disabled")
