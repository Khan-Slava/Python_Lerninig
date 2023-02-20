#1
'''
str1 = ' good morning'
str2 = 'HELLO WORLD'

print(str1.islower())

print(len(str1))

print(str1.upper())

print(str2.lower())

print(str2.title())

str1=str1.lstrip()

print(str1.capitalize())

str1= str1.replace('morning','day')
print(str1)


print(ord('a'))
print(chr(81))
'''
#2
'''
students = []

num_students = int(input("count of students:  "))

for i in range(num_students):
    name = input("input student's name: ")
    class_num = int(input("input student's class: "))
    students.append((name, class_num)) 

sort = sorted(students, key=lambda x: x[1])

for student in sort:
    print(f"{student[0]} - Class {student[1]}")

'''
#3


'''
countLower=0
countUpper=0
first_str = input("input text: ")
for i in range (0,len(first_str)):

    if(first_str[i]).islower():
        countLower+=1

    elif(first_str[i]).isupper():
        countUpper+=1    

if countLower>countUpper:
    final_text = first_str.lower()
else:
    final_text = first_str.upper()

print(countLower)
print(countUpper)
print(final_text)

'''
#4
digit_1=input("input digit_1: ")
digit_2=input("input digit_2: ")

while (digit_1.isdigit()==False or digit_2.isdigit()==False):
    if digit_1.isdigit()==False and digit_2.isdigit()==False:
        digit_1=input("input digit_1: ")
        digit_2=input("input digit_2: ")
    elif digit_1.isdigit()==False:
        digit_1=input("input digit_1: ")
    else:
        digit_2=input("input digit_2: ")


print(float(digit_1)+float(digit_2))
