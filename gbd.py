import json
import pprint #for pretty print
csv_file = open('gbd.csv')

item_parents = dict([x.strip().split(',') for x in csv_file])
item_parents.pop('Item') 


def group(item_parents):

    # put all the common children belonging to respective parent
    tree = dict()

    for x, y in item_parents.items():
        if y not in tree.keys():
            tree[y] = [x]
        else:
            tree[y].append(x)

    return tree	

def classify(item_parents):

    # Group the raw csv list into a dict, i.e. tree structure

    tree = group(item_parents)

    # All the keys in the grouped tree
    allKeys = list(tree.keys())

    # Start making the classification tree
    for key, value in tree.items():
        for i in range(len(value)):
            if value[i] in tree.keys():
                allKeys.remove(value[i])   # Remove the keys that are in grouped tree
                value[i] = {value[i]: tree[value[i]]}

    return {allKeys[0] : tree[allKeys[0]]}


tree = classify(item_parents)
pprint.pprint(tree)

# Dump the tree into as a json data
json.dump(tree, open("gbd.json", 'w'))
