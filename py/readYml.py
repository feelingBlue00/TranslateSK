import yaml
import json

# with open(".../en-GB.yml", "r", encoding="utf-8") as yml_in, open("../json/en-GB.json", "w") as json_out:
#     yml_data = yaml.safe_load(yml_in)
#     json.dump(yml_data, json_out)

with open("../en.yml", "r", encoding="utf-8") as yml_en_in, open("../json/en.json", "w") as json_en_out:
    yml_data = yaml.safe_load(yml_en_in)
    json.dump(yml_data, json_en_out)