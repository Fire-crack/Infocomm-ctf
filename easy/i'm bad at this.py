# this code is wrong somehow, please help me fix this!

string = "3322611, 816371"

first_number = int(string[:6]) 
second_number = int(string[8:len(string)])

remainder = second_number // 10

flag = "CTFInfocomm{" + str(first_number * remainder) + "}"
