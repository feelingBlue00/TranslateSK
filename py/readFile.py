import json
import pandas as pd

def readExcel():
    df = pd.read_excel("../TranslateSheet1.xlsx")

    key_vi_dict = df.set_index("KEY")["VI"].to_dict()

    return key_vi_dict

with open("../json/conTrans.json", "w", encoding="utf-8") as viFile:
    json.dump(readExcel(), viFile, ensure_ascii=False)