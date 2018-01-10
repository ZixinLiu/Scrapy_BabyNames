#!/usr/bin/python3
#-*-encoding:utf-8-*-

import os
import json

def get_file_list(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    name_list = []
    for line in lines:
        name_list.append(line.strip())
    return name_list

def load_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(line)
    return data

def get_names(lines):
    names = {}
    for each in lines:
        if len(each) < 3:
            continue
        each = each[10: ]
        each = each[: -4]
        each = each.strip()
        names[each] = True
    return names

def output_names(file_name, lines):
    file = open(file_name, "w")
    for line in lines:
        line = line + os.linesep
        file.write(line)
        file.flush()
    file.close()

if __name__ == "__main__":
    json_file_list_name = os.path.join("output_files", "json_list.txt")
    json_file_list = get_file_list(json_file_list_name)
    names = {}
    for each_json_file in json_file_list:
        data = load_file(os.path.join("output_files", each_json_file))
        name_map = get_names(data)
        for k,v in name_map.items():
            names[k] = True
        print(len(name_map))
    name_list = []
    for k,v in names.items():
        name_list.append(k)
    total_names_file_name = os.path.join("output_files","total_names.txt")
    output_names(total_names_file_name, name_list)
