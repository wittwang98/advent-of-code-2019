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

zero_list = []
for c in layer_list:
    counter = 0
    for d in c:
        if int(d) == 0:
            counter += 1
    zero_list.append(counter)
    
print(zero_list)

sorted_zero_list = sorted(zero_list)
layer_index = 0
for e in zero_list:
    if sorted_zero_list[0] == e:
        layer_index = zero_list.index(e)
ones = 0
twos = 0
for f in layer_list[layer_index]:
    if int(f) == 1:
        ones += 1
    elif int(f) == 2:
        twos += 1
print(ones*twos)