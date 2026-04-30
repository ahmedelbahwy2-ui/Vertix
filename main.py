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
    
# --- Plotting Function (Matplotlib) ---
def show_report():
    categories_data = {}

    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cat = row['Category']
                amt = float(row['Amount'])
                categories_data[cat] = categories_data.get(cat, 0) + amt

        if not categories_data:
            messagebox.showinfo("Report", "No data to display!")
            return

        # Prepare data for plotting
        labels = categories_data.keys()
        sizes = categories_data.values()

        plt.figure(figsize=(7, 7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Expenses Distribution by Category")
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found!")
