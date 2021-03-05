1. Create a virtual environment for python
   https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

2. How to read and parse _.yaml, _.yml files
   https://pyyaml.org/wiki/PyYAMLDocumentation

   For YAML 1.2 and above: https://yaml.readthedocs.io/en/latest/

## USAGE

###### Usable if you have yml files

Step 1: Read yaml file using `readYml.py`

```py
with open("...Path to yml file", "r", encoding="utf-8") as yml_in, open("...Path to json file", "w") as json_out:
    yml_data = yaml.safe_load(yml_in)
    json.dump(yml_data, json_out)

```

Step 2: Import recently created json file to Excel Spreadsheet using `= IMPORTJSON()` on Spreadsheet, then download it to your computer, you may use tool as well

##### When you have an Excel file

Step 3: `readFile.py`

Use `pandas` for files reading

```sh
# conda
conda install pandas
```

```sh
# or PyPI
pip install pandas
```

```py
def readExcel():
    df = pd.read_excel("...Path to Excel file")

    key_vi_dict = df.set_index("KEY DATA COLUMN")["DEST LANGUAGE DATA COLUMN"].to_dict()

    return key_vi_dict

with open("...Path to json file for dumping translated data", "w", encoding="utf-8") as viFile:
    json.dump(readExcel(), viFile, ensure_ascii=False)
```

Step 4: Replace original json data values with translated values using `replace.py`

```py
json_file = open("...Path to original json file")
json_data = json.load(json_file)

vi_file = open("...Path to json file with translated values", encoding='utf-8')
vi_data = json.load(vi_file)
```

```py
with open("...Path to json file with replaced values", "w", encoding='utf-8') as newData:
    json.dump(json_data, newData, ensure_ascii=False)
```

##### If you want a yaml file

Step 5: Import data from json to yaml using `writeYml.py`

```py
vi_json_file = open("...Path to json file with replaced values", encoding="utf-8")
vi_data = json.load(vi_json_file)

with open("...Path to dest yml file", "w", encoding="utf-8") as vi_yml:
    yaml.dump(vi_data, vi_yml, allow_unicode=True)
```
