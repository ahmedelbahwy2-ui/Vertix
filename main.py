import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = 'expenses.csv'

def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])
    except FileExistsError:
        pass

def add_expense():
    description = desc_entry.get()
    amount = amount_entry.get()
    category = category_var.get()
    date = datetime.now().strftime("%Y-%m-%d")

    if not description or not amount:
        messagebox.showwarning("Warning", "Please fill in all fields!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the amount")
        return

    with open(FILE_NAME, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])

    messagebox.showinfo("Success", f"{description} added successfully!")
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
