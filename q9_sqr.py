size = int(input("Enter the size : "))
lst = []
for i in range(size):
    val = int(input("ENter the value : "))
    lst.append(val)


def sqr(a):
    return a*a

x = map(sqr, lst)

print(list(x))
