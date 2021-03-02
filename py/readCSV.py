import json
import pandas as pd

def readCSV():
    df = pd.read_csv("../TranslateSheet1 - Copy.csv")
    keys = df[df.columns[0]].to_numpy()
    vi = df[df.column[2]].to_numpy()
    csv_key = keys.tolist()
    csv_vi = vi.tolist()
    print(csv_key + ": " + csv_vi)