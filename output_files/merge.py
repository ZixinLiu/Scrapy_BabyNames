# import json
# #covert to set later
# names = [] 
# s = set()

# f = open('top_5.json')
# res = json.load(f)
# for i in range(0, len(res)):
# 	names.append(res[i]['name'])
# 	s.update(names)

# print s
# print len(s)

# f1 = open('top_1000.json')
# res = json.load(f1)
# for i in range(0, len(res)):
# 	names.append(res[i]['name'])
# 	s.update(names)

# print s
# print len(s)




# import json
# ds = json.loads(json_data_string) #this contains the json
# unique_stuff = { each['obj_id'] : each for each in ds }.values()


import json
import sys
from collections import OrderedDict


with open("final.json") as json_file:
    L = json.load(json_file)

# L = json.load(sys.stdin, object_pairs_hook=OrderedDict)
seen = OrderedDict()
for d in L:
    oid = d["name"]
    if oid not in seen:
        seen[oid] = d

print len(seen)

with open('final.txt', 'w') as outfile:
    json.dump(seen.values(), outfile, indent=2)



# json.dump(seen.values(), sys.stdout,  indent=2)



