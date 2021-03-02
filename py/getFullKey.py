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

json_file = open("../json/en-GB.json")
json_data = json.load(json_file)

with open("../concat.json", "w") as conFile:
    json.dump((getFullKey(json_data)), conFile)

#print(getFullKey(json_data, '', "/"))