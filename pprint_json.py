import json
import sys


def load_data(filepath):
    fjson = open(filepath,"r")
    return json.loads(fjson.read())


def pretty_print_json(data): 
    print(json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False))

def main():
    if len(sys.argv) == 1:
        print("Please provide path to json file ")
        sys.exit(1)
    else:
        dirpath = sys.argv[1]
        print('The directory is :{}'.format(dirpath))
        jdata = load_data(filepath=dirpath) 
        pretty_print_json(data=jdata)


if __name__ == '__main__': 
    main()
