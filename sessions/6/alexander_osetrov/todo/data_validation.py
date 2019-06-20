import requests
from jsonschema import validate


schema = {
     "type": "object",
     "properties": {
         "completed": {"type": "boolean"},
         "id": {"type": "string"},
         "order": {"type": "number"},
         "title": {"type": "string"}
     }
}


def validate_item(item):
    validate(instance=item, schema=schema)


invalid_1 = {
    "completed": False,
    "title": "Invalid order type",
    "order": "1"
}

invalid_2 = {
    "completed": False,
    "title": 123,
    "order": 1
}

invalid_3 = {
    "completed": "False",
    "title": "Invalid completed type",
    "order": 1
}


# requests.post("http://127.0.0.1:5001/api/items", json=invalid_1)
