import json


items_path = './items.json'


def open_items():
    with open(items_path, "r") as json_data:
        items_data = json_data.read()
        return json.loads(items_data)


def add_to_items(item):
    items = open_items()
    items.append(item)
    with open(items_path, "w") as json_data:
        json.dump(items, json_data, indent=2, sort_keys=True)
    return None


def delete_from_items(item_id):
    items = open_items()
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
    else:
        pass
    with open(items_path, "w") as json_data:
        json.dump(items, json_data, indent=2, sort_keys=True)
