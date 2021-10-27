import json

with open('tests.json', 'r') as f1, open('values.json', 'r') as f2:
    a = json.load(f1)
    b = json.load(f2)


def item_generator(json_input, lookup_key, dict2):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                for it in dict2['values']:
                    if it['id'] == v:
                        json_input['value'] = it['value']
                        print(json_input['value'])
                yield v
            else:
                yield from item_generator(v, lookup_key, dict2)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key, dict2)


for el in item_generator(a, "id", b):
    print(el)
print(a)
with open('report.json', 'w') as f3:
    json.dump(a, f3)