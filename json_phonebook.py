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

data_json = [
    {
     'name': '',
     'last_name': '',
     'phone': '',
     'city': ''
     }
]

def add_dict(lst, dct):
    name = input('Enter name: ')
    last_name = input('Enter last_name: ')
    phone = input('Enter phone: ')
    city = input('Enter city: ')
    new_dict = dct.copy()
    new_dict['name'] = name
    new_dict['last_name'] = last_name
    new_dict['phone'] = phone
    new_dict['city'] = city
    return lst.append(new_dict)

def search_name(name, lst):
    for i in lst:
        if i[name] == name:
            print("Found person")
            print(i)

def search_last_name(last_name, lst):
    for i in lst:
        if i[last_name] == last_name:
            print("Found person")
            print(i)

def search_phone(phone, lst):
    for i in lst:
        if i[phone] == phone:
            print("Found person")
            print(i)