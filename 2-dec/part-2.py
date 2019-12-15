input_list = []
indexing_list = []

def readfile(file, input_list):   
    file_object = open(file, "r")
    numbers = (file_object.read())
    input_list = numbers.split(",")
    file_object.close()
    return input_list

def calculate(converted_list):
    index = 0
    while converted_list[index] != 99:
        first_index = converted_list[index+1]
        second_index = converted_list[index+2]
        third_index = converted_list[index+3]
        if converted_list[index] == 1:
            converted_list[third_index] = converted_list[first_index]+converted_list[second_index]
        elif converted_list[index] ==2:
            converted_list[third_index] = converted_list[first_index]*converted_list[second_index]
        index +=4
    return converted_list[0]
#index creator
for a in range(100):
    for b in range (100):
        indexing_list.append((a, b))

input_list = readfile("input.txt", input_list)
converted_list_blueprint = []

for a in input_list:
    a = a.strip()
    converted_list_blueprint.append(int(a))

counter = 1
converted_list = converted_list_blueprint.copy()
converted_list[1] = indexing_list[counter][0]
converted_list[2] = indexing_list[counter][1]
comparator = calculate(converted_list)
while comparator != 19690720:
    converted_list = converted_list_blueprint.copy()
    converted_list[1] = indexing_list[counter][0]
    converted_list[2] = indexing_list[counter][1]
    comparator = calculate(converted_list)
    counter += 1;
print(indexing_list[counter-1][0]*100+indexing_list[counter-1][1])