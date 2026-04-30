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
