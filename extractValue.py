import json

def extract_values(obj, value_list):
    if (not isinstance(obj.values(), dict) and not isinstance(obj.values(), list)):
        value_list += obj.values()
    for key, value in obj.items():
        if isinstance(value, dict):
            extract_values(value, value_list)

j_file = open("test.json")
json_data = json.load(j_file)

values = []
extract_values(json_data, values)
