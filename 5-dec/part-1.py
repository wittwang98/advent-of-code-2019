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

while int(str(converted_list[index])[-2:]) != 99:
    param_counter = 0
    if int(str(converted_list[index])[-1:]) == 1:
        if len(str(converted_list[index]))<2 or int(str(converted_list[index])[-(2+param_counter):]) == 0:
            first_index = converted_list[index+1]
            second_index = converted_list[index+2]
            third_index = converted_list[index+3]
            converted_list[third_index] = converted_list[first_index]+converted_list[second_index]
    elif int(str(converted_list[index])[-1:]) == 2:
        first_index = converted_list[index+1]
        second_index = converted_list[index+2]
        third_index = converted_list[index+3]
        converted_list[third_index] = converted_list[first_index]*converted_list[second_index]
    elif int(str(converted_list[index])[-1:]) == 3:
        only_index = converted_list[index+1]
        print("Input a single digit")
        input_number = input()
        converted_list[only_index] = int(input_number)
        index +=2
    elif int(str(converted_list[index])[-1:]) == 4:
        only_index = converterd_list[index+1]
        print(converted_list[only_index])
 
print(40*"=")

print(converted_list[0])
