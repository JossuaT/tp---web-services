# Solution
import json

# Step 1 Read JSON file
with open("../data.json", "r") as file:
    json_data = file.read()

# Step 2 Parse JSON
data = json.loads(json_data)

# Step 3 Extract JSON data into a list of dict
clean_data = []
for people in data:
    people_data = {
        "firstname": people["info"]["firstname"],
        "lastname": people["info"]["lastname"],
        "address": people["info"]["address"]["street"] + people["info"]["address"]["city"] + people["info"]["address"]["zipcode"],
        "age": people["info"]["age"],
        "job": people["job"]
    }
    clean_data.append(people_data)

print(clean_data)