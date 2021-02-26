import json 

def extract_keys(obj, keys_list):
    keys_list += obj.keys()
    for key, value in obj.items():
        if isinstance(value, dict):
            extract_keys(value, keys_list)
        
j_file = open("en-GB.json")
json_data = json.load(j_file)

keys = []
extract_keys(json_data, keys)
#print({key: None for key in keys})

with open("keys.json", "w") as json_keys:
    json.dump({key: None for key in keys}, json_keys)


