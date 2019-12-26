password_counter = 0
possible_passwords = []

a = 271973

def double(a_list):
    a_list = [int(x) for x in str(a_list)]
    counter = 0
    if a_list[0] == a_list[1] and a_list[1] != a_list[2]:
        return True
    if a_list[1] == a_list[2] and a_list[2] != a_list[3] and a_list[0] != a_list[1]:
        return True
    if a_list[2] == a_list[3] and a_list[3] != a_list[4] and a_list[1] != a_list[2]:
        return True
    if a_list[3] == a_list[4] and a_list[4] != a_list[5] and a_list[2] != a_list[3]:
        return True
    if a_list[4] == a_list[5] and a_list[3] != a_list[4]:
        return True
    else:
        return False
            
        
def the_same_func(element):
    temp_list = [int(x) for x in str(element)]
    counter = 0
    while counter < (len(temp_list)):
        if temp_list[counter]== temp_list[counter+1]:
            if counter < (len(temp_list)-2):
                if temp_list[counter]== temp_list[counter+2] and double(temp_list) == False:
                    return False
            else:
                return True
        counter += 1
    else:
        return False

def increasing_func(element):
    temp_list = [int(x) for x in str(element)]
    counter = 0
    while counter < (len(temp_list)-1):
        if temp_list[counter+1] < temp_list[counter]:
            return False
        counter +=1
    return True

while a < 785962:
    possible_passwords.append(a)
    a+=1
    
passwords=[]

for pos_pas in possible_passwords:
    if double(pos_pas) and increasing_func(pos_pas):
        password_counter += 1
        passwords.append(pos_pas)
        
print(password_counter)
#print(passwords)