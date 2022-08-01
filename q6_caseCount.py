str = input("Enter the string : ")
countUpper = 0
countLower = 0

for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        countUpper += 1

    elif (ord(i)>=97 and ord(i)<=122):
        countLower += 1


print("No. of Upper case Characters  ", countUpper)
print("No. of Lower case Characters  ", countLower)


