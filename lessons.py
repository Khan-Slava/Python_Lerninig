age =int(input("input your age: "))
name=str(input("input your Full name: "))
gender=str(input("input your gender(M or F): "))


'''if gender!="M" or gender!="F":
    print(gender)
    while gender!="M" or gender!="F":
        gender=str(input("input your gender(M or F): "))
'''

if gender=='M':
    if age<63:
        retirement=63-age
        print("before retirement: ", retirement)        
else :
    if age<60:
        retirement=60-age
        print("before retirement: ", retirement)