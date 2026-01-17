import json

my_file = "data.json"

def load_data():
    with open (my_file,"r") as file:
        return json.load(file)

def save_data(data):
    with open(my_file,"w") as file:
        return json.dump(data, file, indent = 4)