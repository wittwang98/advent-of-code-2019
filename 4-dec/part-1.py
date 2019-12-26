password_counter = 0
possible_passwords = []

a = 271973

def the_same_func(element):
    temp_list = [int(x) for x in str(element)]
    counter = 0
    while counter < (len(temp_list)-1):
        if temp_list[counter]== temp_list[counter+1]:
            return True
        counter += 1
    return False

def increasing_func(element):
    temp_list = [int(x) for x in str(element)]
    counter = 0
    while counter < (len(temp_list)-1):
        if temp_list[counter+1] < temp_list[counter]:
            return False
        counter +=1
    return True

while a < 785961:
    possible_passwords.append(a)
    a+=1
    
for pos_pas in possible_passwords:
    if the_same_func(pos_pas) and increasing_func(pos_pas):
        password_counter += 1        
print(password_counter)