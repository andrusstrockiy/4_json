import json
import sys


def load_json_data(filepath):
    with open(filepath, "r") as jsonfile:
        return json.loads(jsonfile.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


def check_filepath():
    dirpath = ''
    if len(sys.argv) == 1:
        print("Please provide path to json file ")
    else:
        dirpath = sys.argv[1]
        print('The directory is :{}'.format(dirpath))
    return dirpath


def main():
    path = check_filepath()
    if path:
        pretty_print_json(data=load_json_data(path))


if __name__ == '__main__':
    main()
