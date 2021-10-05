import json
#
# data_json = [
#     {
#      'name': 'name',
#      'last_name' : "Levitskiy",
#      'phone': "380509001818",
#      'city' : "Kremenchuk"
#      }
# ]
#
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data_json, f, indent=4)

# filename = "json2.json"
f = open("data.json")

try:
    phb = json.load(f)
except json.decoder.JSONDecodeError:
     phb = []
f.close()