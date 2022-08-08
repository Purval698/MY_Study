
size = int(input("Enter the size : "))
lst = []
for i in range(size):
    val = int(input("ENter the value : "))
    lst.append(val)

def triple(a):
  return 3*(a)

x = map(triple,  lst)

print(x)

print(list(x))