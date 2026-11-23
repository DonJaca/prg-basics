
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print(arr[len(arr)-1])
print(arr[0]+arr[len(arr)-1])
print(arr[int(len(arr)/2)])

for index in arr:
    print(index,end=" ")