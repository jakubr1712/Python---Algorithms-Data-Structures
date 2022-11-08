def partition(array, left, right):
    pivot = array[right]
    i = left - 1
 
    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[right]) = (array[right], array[i + 1])
 
    return i + 1
 
 
 
def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left, right)
        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)
 
 
data = [12,-4,20,43,-12,0,10]
print("Unsorted Array")
print(data)
 
size = len(data)
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)