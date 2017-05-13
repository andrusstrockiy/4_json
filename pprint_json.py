#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys


def load_data(filepath):
	fjson = open(filepath,"r")
	return json.loads(fjson.read())

    

def pretty_print_json(data):
	print(json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False))
	# pprint.pprint(data)
    

def main():
	dirpath = sys.argv[1]
	print('The directory is :{}'.format(dirpath))
	jdata = load_data(filepath=dirpath)
	pretty_print_json(data=jdata)


if __name__ == '__main__':
	main()
    
