import yaml
import json

vi_json_file = open("../json/vi.json", encoding="utf-8")
vi_data = json.load(vi_json_file)

with open("../en-vi.yml", "w", encoding="utf-8") as vi_yml:
    yaml.dump(vi_data, vi_yml, allow_unicode=True)