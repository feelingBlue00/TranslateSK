import json
import googletrans
from googletrans import Translator

values_file = open("../json/values.json")
values_data = json.load(values_file)

translator = Translator()

translations = {}

for value in values_data:
    translations[value] = translator.translate(value, dest='vi').text

with open("../json/trans.json", "w", encoding='utf8') as tf:
    json.dump(translations, tf, ensure_ascii=False) 

# result = translator.translate('안녕하세요.', dest='ja')
# print(result)

