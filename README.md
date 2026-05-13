# 💸 Vertix — Smart Expense Tracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Charts-Matplotlib-11557C?style=for-the-badge&logo=matplotlib)
![CSV](https://img.shields.io/badge/Storage-CSV-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**A clean, lightweight desktop app that helps you log expenses, organize them by category, and instantly visualize where your money is going — all in one window.**

</div>

---

## 🖥️ App Preview

```
┌──────────────────────────────────────┐
│       Vertix Expense Manager         │
│                                      │
│  Name :   [_____________________]    │
│  Amount:  [_____________________]    │
│  Category:      [ Food ▾ ]           │
│                                      │
│       [     ➕ Add      ]            │
│       [  📊 Show Report ]            │
│                                      │
│       Project by: Vertix Team        │
└──────────────────────────────────────┘
```
## Photo from the project

(<img width="750" height="866" alt="image" src="https://github.com/user-attachments/assets/a89daed8-c9be-4d1c-b670-1c9bcbee30d4" />)
<img width="1052" height="1161" alt="image" src="https://github.com/user-attachments/assets/7e33b2d6-ad16-48d7-9b56-d870c38dcd7b" />

---

## 📖 What is Vertix?

**Vertix** is a student-built desktop application developed in Python. It was created as part of the **Computer Programming 1** course at **Mansoura National University — Faculty of Engineering (AIE Program)**.

The app solves a real problem for students: **losing track of daily spending**. With Vertix, every expense is logged with an auto-stamped date, sorted into a category, and saved to a local CSV file. At any point, you can hit **"Show Report"** to get an instant pie chart showing exactly how your money is distributed.

No internet. No account. No database. Just open it and start tracking.

---

## ✨ Features

| Feature | Details |
|---|---|
| 📝 **Log Expenses** | Enter a name and amount for any expense in seconds |
| 🗂️ **5 Smart Categories** | Study, Food, Transportation, Entertainment, Other |
| 📅 **Auto Date Stamping** | Every entry is automatically saved with today's date |
| 📊 **Pie Chart Reports** | Visualize your spending distribution with one click |
| 💾 **Persistent Storage** | All data saved to `expenses.csv` — survives app restarts |
| ⚠️ **Input Validation** | Catches empty fields and invalid number formats instantly |

---

## 🗂️ Expense Categories

The app comes with **5 built-in categories** tailored for students:

- 📚 **Study** — Books, stationery, courses, printing
- 🍕 **Food** — Meals, snacks, coffee
- 🚌 **Transportation** — Bus, taxi, fuel
- 🎮 **Entertainment** — Outings, subscriptions, hobbies
- 📦 **Other** — Anything that doesn't fit above

---

## 📂 Data Storage

Every expense is saved as a row in **`expenses.csv`** in the following format:

```
Date,Category,Description,Amount
2025-05-01,Food,Lunch at cafeteria,45.0
2025-05-01,Study,Python textbook,120.0
2025-05-02,Transportation,Bus ticket,10.0
```

The file is created automatically on first launch if it doesn't already exist.

---

## 🛠️ Technologies Used

```python
import tkinter       # Desktop GUI — window, labels, buttons, inputs, dropdown
import matplotlib    # Pie chart generation and display
import csv           # Reading and writing expense data
from datetime import datetime  # Auto-stamping each entry with today's date
```

| Library | Role in Vertix |
|---|---|
| **Tkinter** | Builds the entire GUI — window, form fields, buttons, dropdown menu |
| **Matplotlib** | Renders the pie chart report showing spending by category |
| **CSV Module** | Handles all data persistence — reading and writing `expenses.csv` |
| **datetime** | Automatically records the date for every expense added |

---

## ⚙️ Installation & Setup

### 1. Make Sure Python is Installed

Download Python 3.x from [python.org](https://www.python.org/downloads/) if you haven't already.

### 2. Install Matplotlib

`tkinter`, `csv`, and `datetime` are all built into Python. The only external library you need is:

```bash
pip install matplotlib
```

### 3. Run the App

```bash
python main.py
```

That's it. The app window will open immediately, and `expenses.csv` will be created automatically in the same folder.

---

## 🚀 How to Use

1. **Type a name** for your expense in the *Name* field (e.g., `Lunch`, `Bus ticket`)
2. **Enter the amount** as a number (e.g., `45` or `12.50`)
3. **Select a category** from the dropdown menu
4. Click **Add** — the expense is saved and the fields are cleared
5. Click **Show Report** at any time to see a pie chart of your spending by category

---

## 📁 Project Structure

```
vertix-expense-tracker/
│
├── main.py           # Full application — GUI, logic, charts, file handling
├── expenses.csv      # Auto-generated data file (created on first run)
└── README.md         # Project documentation
```

> All logic lives in a single `main.py` file, keeping the project simple and easy to follow for a Programming 1 course.

---

## 👥 Team Members

1. **Ahmed Mohamed Ramadan Ramadan Abu Al-Maati** (Leader) - ID: [24040801]
2. **Loay Mohamed Ahmed Bahloul** - ID: [24040770]
3. **Sabry Samir Sabry Awad** - ID: [24040362]
4. **Ziad Ahmed Hamida Al-Qasabi** - ID: [24040352]
5. **Daniel Emad Boushra** - ID: [24040347]

---

## 📋 Project Info

| Field | Details |
|---|---|
| **Course** | Computer Programming 1 |
| **University** | Mansoura National University |
| **Faculty** | Faculty of Engineering — AIE Program |

---

<div align="center">

Made with ❤️ by the **Vertix Team**  
Mansoura National University — AIE Program level 100

</div>
