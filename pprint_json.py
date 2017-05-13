#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys


def load_data(filepath):
	# print(filepath)
	fjson = open(filepath + "source.json","r")
	# data= fjson.read()
	return json.loads(fjson.read())

    


def pretty_print_json(data):
	print(json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False))
	# pprint.pprint(data)
    

def main():
	# print('Please provide directory of JSON files :')
	# print('i.e /home/userdev/\n')
	# script, filename = argv
	dirpath = sys.argv[1]
	print('The directory is :{}'.format(dirpath))

	#dirpath = input('Directory:')
	jdata = load_data(filepath=dirpath)
	#print(jdata)
	pretty_print_json(data=jdata)


if __name__ == '__main__':
	main()


	# i.e dirpath = '/home/adnruss/mydev/'
    
