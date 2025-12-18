import json
import os
import uuid
folder = "Database"
file = "Data.json"
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
folder_destination = os.path.join(project_dir, folder)
full_path = os.path.join(folder_destination, file)
os.makedirs(folder_destination, exist_ok=True)

def load_data():
    if not os.path.exists(full_path):
        return []
    else:
        try:
            with open(full_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
        
def save_data(title, date, amount, tipe, category=""):
    data = load_data()
    unique_id = str(uuid.uuid4())
    data_input = {
        "id":unique_id,
        "title":title,
        "date":date,
        "amount":amount,
        "Type":tipe,
        "Category":category
    }
    data.append(data_input)
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)

def delete_data(Id):
    with open(full_path, 'r') as file:
        data= json.load(file)
    new_data= [d for d in data if d.get("id")!=Id]
    with open(full_path, 'w') as file:
        json.dump(new_data, file, indent=4)

def edit_data(Id, title, date, amount, tipe, category):
    data= load_data()
    for d in data:
        if d["id"]==Id:
            d["title"]=title
            d["date"]=date
            d["amount"]=amount
            d["Type"]=tipe
            d["Category"]=category
            break
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)