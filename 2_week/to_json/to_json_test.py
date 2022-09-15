from to_json import to_json


@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data.__name__)
print(get_data())  # вернёт '{"data": 42}'
