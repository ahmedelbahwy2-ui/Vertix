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
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number in the amount field!")
        return

    with open(FILE_NAME, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])

    messagebox.showinfo("Success", f"{description} added successfully!")
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# --- Matplotlib Graph Function ---
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
        plt.title("Expense Distribution by Category")
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found!")

# --- User Interface ---
initialize_file()
root = tk.Tk()
root.title("Vertix - Expense Tracker")
root.geometry("500x550")

tk.Label(root, text="Vertix Expense Manager", font=("Arial", 16, "bold"), fg="darkblue").pack(pady=10)

tk.Label(root, text="Name :", font=("Arial", 10)).pack(pady=5)
desc_entry = tk.Entry(root, width=40)
desc_entry.pack()

tk.Label(root, text="Amount:", font=("Arial", 10)).pack(pady=5)
amount_entry = tk.Entry(root, width=40)
amount_entry.pack()

tk.Label(root, text="Category:", font=("Arial", 10)).pack(pady=5)
category_var = tk.StringVar(root)
category_var.set("Food")
categories = ["Study", "Food", "Transportation", "Entertainment", "Other"]
category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.pack()

add_button = tk.Button(root, text="Add", bg="#28a745", fg="white", width=25, height=2, font=("Arial", 10, "bold"), command=add_expense)
add_button.pack(pady=20)

# Bind the report button to the new function (command=show_report)
report_button = tk.Button(root, text="Show Report", bg="#007bff", fg="white", width=25, height=2, font=("Arial", 10, "bold"), command=show_report)
report_button.pack(pady=5)

tk.Label(root, text="Project by: Vertix Team", font=("Arial", 8, "italic")).pack(side="bottom", pady=10)

root.mainloop()
