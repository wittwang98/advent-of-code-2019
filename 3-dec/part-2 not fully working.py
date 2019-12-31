input_list=[]
first_wire = []
second_wire= []

first_coords=[]
second_coords=[]

def number_extract(string):
    return int(string[1:])

def trace_cable(wire, coord_list):
    x = 0
    y = 0
    s = 0
    for a in wire:
        u = number_extract(a)
        if str(a).startswith("R"):
            counter = 0
            while counter < u:
                counter += 1
                x = x+1
                s = s+1
                coord_list.append((x,y,s))
        elif str(a).startswith("L"):
            counter = 0
            while counter < u:
                counter += 1
                x = x-1
                s = s+1
                coord_list.append((x,y,s))
        elif str(a).startswith("U"):
            counter = 0
            while counter < u:
                counter += 1
                y = y+1
                s = s+1
                coord_list.append((x,y,s))
        else:
            counter = 0
            while counter < u:
                counter += 1
                y = y-1
                s = s+1
                coord_list.append((x,y,s))

file_object = open("input1.txt", "r")
line = (file_object.readline()).strip()

while(line):
    input_list.append(line)
    line =(file_object.readline()).strip()
file_object.close()

first_wire=(input_list[0].split(","))
second_wire=(input_list[1].split(","))

trace_cable(first_wire, first_coords)
print("first_trace")
trace_cable(second_wire, second_coords)
print("second_trace")

first_wire_intersections = []
second_wire_intersections = []

for d in first_coords:
    temp = int(first_coords.index(d))
    if temp%100 == 0:
        print(str(temp/len(first_coords)*100)+ "%")
    for e in second_coords:
        if e[0] == d[0] and e[1] == d[1]:
            first_wire_intersections.append(e)
            second_wire_intersections.append(d)

print(first_wire_intersections)
print(second_wire_intersections)
      
counter = 0
distances = []
while counter < (len(first_wire_intersections)-1):
    dist = first_wire_intersections[counter][2]+ second_wire_intersections[counter][2] 
    distances.append(dist)
    counter += 1
print(distances)

print(distances[0])
