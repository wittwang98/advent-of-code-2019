from copy import deepcopy
input_list = []

file_object = open("input1.txt", "r")
line = file_object.readline().strip()

while(line):
    elements = line.split(")")
    element = (elements[0], elements[1])
    input_list.append(element)
    line =file_object.readline().strip()
file_object.close()

print(input_list)

orbit = 0

def search_for_orbits(search_for_list, orbit):
    temp_list = []
    for a in search_for_list:
        for b in input_list:
            if a == b[0]:
                temp_list.append(b[1])
        internal = search_for_orbits(temp_list, orbit)
    if len(temp_list) == 0:
        orbit = deepcopy(orbit) + orbit
        return []
    else:
        orbit += orbit+len(temp_list)
        return temp_list

search_list = search_for_orbits(["COM"], orbit)
print(search_list)
orbits = 0
while len(search_list) >0:
    orbits = len(search_list) + orbits
    search_list = search_for_orbits(search_list, orbit)
    print(search_list)

    
print(orbits)
print(orbit)