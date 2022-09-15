import os
import tempfile
import argparse
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='key-value storage')
    parser.add_argument('--key', type=str, help='key')
    parser.add_argument('--value', nargs='?', type=str, help='new value')
    args = parser.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if not os.path.exists(storage_path):
        with open(storage_path, 'w') as f:
            json.dump({}, f)
    with open(storage_path, 'r') as f:
        if os.stat(storage_path).st_size == 0:
            storage = {}
        else:
            storage = json.load(f)

    if args.value is None:
        if args.key in storage.keys():
            print(', '.join(map(str, storage[args.key])))
        else:
            print("")
    else:
        with open(storage_path, 'w') as f:
            if args.value is not None:
                if args.key not in storage.keys():
                    storage[args.key] = []
                storage[args.key].append(args.value)
                f.truncate(0)
                json.dump(storage, f)
