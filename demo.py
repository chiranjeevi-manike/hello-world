import array as ma
arr_1 = ma.array("b",[1,2,3,4])

print(arr_1)

print(arr_1[0])

print("No. of elements: ",len(arr_1))

print(arr_1[0]+arr_1[3])
print(range(3))

for i in range(len(arr_1)):
    print(arr_1[i], end ="*")

#slicing
arr_2 = ma.array("b",[1,2,3,4,5,6,7,8,0,9])

#print first four elements
print("First four elements:",arr_2[0:3])

# printing from last
print(arr_2[-1:-5])

print(arr_2[5:])

print(arr_2[-4:])

print(arr_2[:7])

arr_2.insert(11, 300)

arr_2[3] = 10



