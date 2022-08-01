size = int(input("Enter teh size : "))
lst = []

for i in range(size):
    val = int(input('Enter the value : '))
    lst.append(val)

sum = 0

for j in lst:
    sum += j

print(sum)
