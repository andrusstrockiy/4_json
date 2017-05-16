import json
import sys


def load_data(filepath):
    """Loads Json file from directory"""
    with open(filepath, "r") as fjson:
        return json.loads(fjson.read())


def pretty_print_json(data):
    """Provides output in pretty print format"""
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


def get_input():
    dirpath = ''
    if len(sys.argv) == 1:
        print("Please provide path to json file ")
    else:
        dirpath = sys.argv[1]
        print('The directory is :{}'.format(dirpath))
    return dirpath


def main():
    path = get_input()
    if path:
        pretty_print_json(data=load_data(path))


if __name__ == '__main__':
    main()
