import os
import json

folder = "Database"
file = "Data.json"
current_dir = os.path.abspath(__file__)
utils_dir = os.path.dirname(current_dir)
project_dir = os.path.dirname(utils_dir)
data_dir = os.path.join(project_dir, folder)
full_path = os.path.join(data_dir, file)

def total():
    total = 0
    if not os.path.exists(full_path):
        return total
    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
        for transaction in data:
            format_amount = transaction["amount"].replace(".","")
            amount = int(format_amount)
            tipe = transaction["Type"]
            if tipe == "Income":
                total += amount
            else:
                total -= amount
        format_total = f"{total:,}".replace(",",".")
        return format_total
    except json.JSONDecodeError:
        return "0"

def InEx_total():
    inc_total = 0
    ex_total = 0
    if not os.path.exists(full_path):
        format_inc_total= f"{inc_total}"
        format_ex_total= f"{ex_total}"
        return format_inc_total, format_ex_total
    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
        for transaction in data:
            format_amount = transaction["amount"].replace(".","")
            amount = int(format_amount)
            tipe = transaction["Type"]
            if tipe == "Income":
                inc_total += amount
            else:
                ex_total += amount
        format_inc_total = f"{inc_total:,}".replace(",",".")
        format_ex_total = f"{ex_total:,}".replace(",",".")
        return format_inc_total, format_ex_total
    except json.JSONDecodeError:
        format_inc_total= f"{inc_total}"
        format_ex_total= f"{ex_total}"
        return format_inc_total, format_ex_total
        