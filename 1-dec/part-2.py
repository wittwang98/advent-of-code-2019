input_list = []
total_fuel = 0

def readfile(file, input_list):   
    file_object = open(file, "r")
    line = (file_object.readline()).strip()
    while(line):
        input_list.append(line)
        line =(file_object.readline()).strip()
    file_object.close()
    return input_list

def calculate(element):
    result = int((element)/3)-2
    return result

readfile("input.txt", input_list)

for a in input_list:
    required_fuel = calculate(float(a))
    while required_fuel > 0: 
        total_fuel += required_fuel
        required_fuel = calculate(float(required_fuel))

print(total_fuel)