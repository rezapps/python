#!/usr/bin/env python3
# pylint: disable=missing-function-docstring, missing-module-docstring

filename = "items.txt"

with open(filename) as filehandle:
    line = filehandle.readline().strip()

items_as_list = line.split(",")
print(items_as_list)




# add item to the list
items_as_list.append("cup")
print(items_as_list)

# join the list into a string with a comma ","" between every item
list_as_str = ",".join(items_as_list)
print(list_as_str)

# write the line to the file
with open(filename, "w") as filehandle:
    filehandle.write(list_as_str)
