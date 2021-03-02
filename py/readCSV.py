import json
import pandas as pd

def readCSV():
    df = pd.read_csv("../TranslateSheet1 - Copy.csv")
    matrix2 = df[df.columns[0]].to_numpy()
    csv_key = matrix2.tolist()
#    print(csv_key)