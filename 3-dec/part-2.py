input_list=[]
first_wire = []
second_wire= []

first_coords=[]
second_coords=[]
first_step_list = []
second_step_list = []

def number_extract(string):
    return int(string[1:])

def trace_cable(wire, coord_list, step_list):
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
                coord_list.append((x,y))
                step_list.append(s)
        elif str(a).startswith("L"):
            counter = 0
            while counter < u:
                counter += 1
                x = x-1
                s = s+1
                coord_list.append((x,y))
                step_list.append(s)
        elif str(a).startswith("U"):
            counter = 0
            while counter < u:
                counter += 1
                y = y+1
                s = s+1
                coord_list.append((x,y))
                step_list.append(s)
        else:
            counter = 0
            while counter < u:
                counter += 1
                y = y-1
                s = s+1
                coord_list.append((x,y))
                step_list.append(s)

file_object = open("input.txt", "r")
line = (file_object.readline()).strip()

while(line):
    input_list.append(line)
    line =(file_object.readline()).strip()
file_object.close()

first_wire=(input_list[0].split(","))
second_wire=(input_list[1].split(","))

trace_cable(first_wire, first_coords, first_step_list)
print("first_trace")
trace_cable(second_wire, second_coords, second_step_list)
print("second_trace")


print(len(first_step_list))
print(len(second_step_list))

intersections = set(first_coords).intersection(second_coords)
print(type(intersections))

intersections = list(intersections)
print(len(intersections))
print(intersections)

first_index_list = []
second_index_list = []
counter = 0
while counter < len(intersections)-1:
    print("hej")
    for a in first_coords:
        if a[0] == intersections[counter][0]:
            for b in first_coords:
                if b[1] == intersections[counter][1]:
                    first_index_list.append(first_coords.index((a[0],b[1])))#first_index_list.append(first_coords.index(b))
                    break
    counter += 1
    
counter = 0
while counter < len(intersections)-1:
    print("hej")
    for a in second_coords:
        if a[0] == intersections[counter][0]:
            for b in second_coords:
                if b[1] == intersections[counter][1]:
                    second_index_list.append(second_coords.index((a[0],b[1])))#second_coords.index(b)
                    break
    counter += 1

final_second_index_list =  []
last_val = 0
for c in second_index_list:
    if c != last_val:
        final_second_index_list.append(c)
    last_val = c

final_first_index_list =  []
last_val = 0
for c in first_index_list:
    if c != last_val:
        final_first_index_list.append(c)
    last_val = c
    
print(first_step_list)
        
print(final_first_index_list)
print( "="*40)
print(final_second_index_list)

step_list1 = []
step_list2 = []
final_step_list = []
for a in final_first_index_list:
    step_list1.append(first_step_list[a])

for a in final_second_index_list:
    step_list2.append(second_step_list[a])

for a in range(len(step_list1)):
    final_step_list.append(step_list1[a]+step_list2[a])

final_step_list.sort()

print(final_step_list[0])