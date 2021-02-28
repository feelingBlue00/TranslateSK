import json

def extract_values(obj):
    for value in obj.values():
        if (isinstance(value, list)):
            for i in value:
                yield i
        elif (isinstance(value, dict)):
            yield from extract_values(value)
        else:
            yield value

j_file = open("../json/en-GB.json")
json_data = json.load(j_file)

values = list(extract_values(json_data))

with open("../json/values.json", "w") as json_values:
    json.dump({values: None for values in values}, json_values)
