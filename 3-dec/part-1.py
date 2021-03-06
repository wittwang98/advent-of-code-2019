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
    for a in wire:
        u = number_extract(a)
        if str(a).startswith("R"):
            counter = 0
            while counter < u:
                counter += 1
                x = x+1
                coord_list.append((x,y))
        elif str(a).startswith("L"):
            counter = 0
            while counter < u:
                counter += 1
                x = x-1
                coord_list.append((x,y))
        elif str(a).startswith("U"):
            counter = 0
            while counter < u:
                counter += 1
                y = y+1
                coord_list.append((x,y))
        else:
            counter = 0
            while counter < u:
                counter += 1
                y = y-1
                coord_list.append((x,y))

file_object = open("input.txt", "r")
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

intersections = set(first_coords).intersection(second_coords)

#print(intersections)
distances = []
                    
for d in intersections:
    dist = abs(d[0])+abs(d[1])
    #print(dist)
    distances.append(dist)

distances.sort()

print(distances[0])
