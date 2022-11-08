def swapElements(array,item):
     temp = array[item+1]
     array[item+1]=array[item]
     array[item]=temp

def bubbleSort(array):
    arrayLen=len(array)
    for i in range(arrayLen):
        for j in range(arrayLen):
            if  j < arrayLen-i-1  and array[j] > array[j+1] :
                swapElements(array,j)

array= []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    array.append(ele)
           

bubbleSort(array)

print("after sort:")
print(array)