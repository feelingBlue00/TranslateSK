import json

def getFullKey(obj):
    merge_keys = {}

    def flatten(item, parent_key='', sep="/"):
        if type(item) is dict:
            for key in item:
                flatten(item[key], parent_key + str(key) + sep)

        elif type(item) is list:
            index = 0

            for ele in item:
                flatten(ele, parent_key + str(index) + sep)
                index = index + 1
        else:
            merge_keys[parent_key[:-1]] = item

    flatten(obj)
    return merge_keys

# json_file = open("../json/en-GB.json")
# json_data = json.load(json_file)

# vi_file = open("../json/conTrans.json", encoding='utf-8')
# vi_data = json.load(vi_file)

json_file = open("../json/en.json")
json_data = json.load(json_file)

vi_file = open("../json/enTrans.json", encoding='utf-8')
vi_data = json.load(vi_file)

def setData(obj, conTranslated):

    def replaceData(item, parent_key='', sep="/"):
        if type(item) is dict:
            for key in item:
                if type(item[key]) is str:
                    val = conTranslated[parent_key[:-1] + sep + str(key)]
                    item[key] = val
                else:
                    replaceData(item[key], parent_key + str(key) + sep)

        elif type(item) is list:
            for index, ele in enumerate(item):
                if type(ele) is str:
                    val = conTranslated[parent_key[:-1] + sep + str(index)]
                    item[index] = val
                else:
                    replaceData(ele, parent_key + str(index) + sep)

    replaceData(obj)

setData(json_data, vi_data)

with open("../json/vi.json", "w", encoding='utf-8') as newData:
    json.dump(json_data, newData, ensure_ascii=False)