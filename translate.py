import json

import googletrans
from googletrans import Translator

#from extractValues import extract_values
from extractKeys import extract_keys

# j_file = open("test.json")
# json_data = json.load(j_file)

# values = []
# extract_values(json_data, values)

j_file = open("test.json")
json_data = json.load(j_file)

keys = []
extract_keys(json_data, keys)

translator = Translator()

translations = {}

for key in keys:
    translations[key] = translator.translate(key, dest='vi').text

with open("value_test.json", "w") as tf:
    json.dump(translations, tf) 

# result = translator.translate('Hello', dest='ja')
# print(result)

