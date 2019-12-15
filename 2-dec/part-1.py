input_list = []


def readfile(file, input_list):   
    file_object = open(file, "r")
    numbers = (file_object.read())
    input_list = numbers.split(",")
    file_object.close()
    return input_list

input_list = readfile("input.txt", input_list)
converted_list = []

for a in input_list:
    a = a.strip()
    converted_list.append(int(a))

index = 0

while converted_list[index] != 99:
    if converted_list[index] == 1:
        first_index = converted_list[index+1]
        second_index = converted_list[index+2]
        third_index = converted_list[index+3]
        converted_list[third_index] = converted_list[first_index]+converted_list[second_index]
    elif converted_list[index] ==2:
        first_index = converted_list[index+1]
        second_index = converted_list[index+2]
        third_index = converted_list[index+3]
        converted_list[third_index] = converted_list[first_index]*converted_list[second_index]
    index +=4
print(40*"=")

print(converted_list[0])
