import yaml
import json

with open(".../en-GB.yml", "r", encoding="utf-8") as yml_in, open("../json/en-GB.json","w") as json_out:
    yml_data = yaml.safe_load(yml_in)
    json.dump(yml_data, json_out)
#    print(yml_data)