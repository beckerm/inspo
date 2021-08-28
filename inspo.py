#!/usr/bin/env python3

# to make executable: chmod 755 inspo.py
# throw inspo.py elements.json and *.txt files into a directory
# add new *.txt files (word lists) and edit elements.json as needed
# to execute: ./inspo.py

import json
import random
import os

json_file = 'elements.json'

if os.path.exists(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
    except Exception as e:
        print(str(e))
        exit(1)
    finally:
        f.close()
else:
    print('Missing ' + json_file)


def inspiration_slurp(filename):
    x = []
    try:
        f = open(filename)
        for line in f:
            x.append(line)
    except Exception as e:
        print(str(e))
        pass
    finally:
        f.close()
    return x


def random_ranger(range_value):
    s = range_value.split('-')
    range_list = range(int(s[0]), int(s[1]) + 1)
    r = random.sample(range_list, 1)
    return int(r[0])


final_result = []


for element in data['elements']:
    if element['enabled'] == 1 and os.path.exists(element['file']):
        o = random_ranger(element['results'])
        inspiration = inspiration_slurp(element['file'])
        a = int(len(inspiration))
        if o > a:
            # number of random elements defined in json is greater than total elements in file - skip it!
            continue
        else:
            results = random.sample(inspiration, o)
            for r in results:
                final_result.append(r)

random.shuffle(final_result)

str_final_result = ' '.join([line.strip() for line in final_result])

print(str_final_result)
