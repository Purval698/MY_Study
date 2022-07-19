numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

lst = list(numbers)

eve_count = 0
odd_count = 0

for i in lst:
    val = i % 2
    if val == 0:
        eve_count += 1
    elif val == 1:
        odd_count += 1

print("Number of even numbers " ,eve_count )

print("Number of odd numbers " , odd_count )
