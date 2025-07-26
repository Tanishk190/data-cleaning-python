# 🧹 Clean My CSV – Data Cleaning with Pandas & NumPy

A beginner-friendly project that transforms messy, duplicated, and corrupted CSV files into clean, usable datasets with just a few lines of Python code.

---

## 💡 About

**Clean My CSV** is a Python script that:
- 🚫 Removes duplicate rows
- ⚠ Replaces `inf`, `-inf` values with `NaN`
- 🧠 Fills missing numeric values with column-wise mean
- ✅ Outputs a fresh, clean `.csv` ready for analysis!

Perfect for beginners practicing **Pandas** and **NumPy**, or anyone who wants to automate basic CSV data cleaning.

---

## 📁 Input Example (dirty CSV)

| Name   | Age  | Working_Hours | Salary |
|--------|------|----------------|--------|
| Alice  | 25   | 40             | 50000  |
| Bob    | inf  | 38             | 52000  |
| Alice  | 25   | 40             | 50000  |
| Carol  | NaN  | NaN            | 51000  |
| Dave   | 30   | -inf           | 54000  |

---

## 🚀 What It Does

🔁 Removes duplicates  
♾ Converts `inf`, `-inf` → `NaN`  
🧼 Fills `NaN` (in numeric columns) → column mean  

Cleaned output:

| Name   | Age  | Working_Hours | Salary |
|--------|------|----------------|--------|
| Alice  | 25.0 | 40.00          | 50000  |
| Bob    | 26.67| 38.00          | 52000  |
| Carol  | 26.67| 39.00          | 51000  |
| Dave   | 30.0 | 39.00          | 54000  |

---

## 🛠 How to Use

1. Clone the repo
```bash
git clone https://github.com/your-username/clean-my-csv.git
cd clean-my-csv
