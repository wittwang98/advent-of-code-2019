input_list = []

file = "input.txt"

file_object = open(file, "r")
numbers = (file_object.read())
file_object.close()

number_list = []
for a in numbers:
    number_list.append(a)
    
counter = 0
pic = 25*6
layer_list = []
while pic < len(number_list):
    temp_list = []
    while counter < (pic):
        temp_list.append(number_list[counter])
        counter += 1
    layer_list.append(temp_list)
    pic += 25*6

pixel_counter = 0
pixel_list = []
#print(layer_list)
while pixel_counter < 25*6:
    temp = []
    for b in range(len(layer_list)):
        temp.append(layer_list[b][pixel_counter])
    for c in temp:
        if int(c) != 2:
            if int(c) == 1:
                pixel_list.append("X")
            else:
                pixel_list.append(" ")
            break
    pixel_counter += 1
print(pixel_list)

for p in range(len(pixel_list)):
    print(pixel_list[p], end = "")
    if p%25 == 24:
        print("")