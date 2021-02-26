import json 

def extract_keys(obj):
    for key, value in obj.items():
        if isinstance(value, dict) or isinstance(value, list):
            yield key
            yield from extract_keys(value)
        else:
            yield key
        
j_file = open("en-GB.json")
json_data = json.load(j_file)

keys = list(extract_keys(json_data))

with open("keys.json", "w") as json_keys:
    json.dump({key: None for key in keys}, json_keys)

