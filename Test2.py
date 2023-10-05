
print("start of program")
print("first for loop")
L =  [100, 200, 300, 400, 500]

for x in L:
    print(x,  type(x))
print("end of first for loop")
L = [True, 10, (100, 200), {'a': 1.1, 'b':2.2}, 3.7]

print("second for loop")
for x in L:
    print(x, type(x))
print("end of second for loop")
print("end of program")

