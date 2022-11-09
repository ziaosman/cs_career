#selection sort
def findSmallest(arr):
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
            return smallest_index
def selectionSort(arr):
    #for every element in the array
    for i in range(len(arr)):
        #find the smallest index
        smallest = findSmallest(arr)
        #add the smallest to a new array
        newAarr.append(arr.pop(smallest))
        return newArr