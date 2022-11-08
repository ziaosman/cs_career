#binary search
#log n
#takes in an ordered array and outputs null or the position of the searched item 
def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = round((low+high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        #guess is larger than the item
        else: 
            high = mid - 1
    return None
    
my_list = [1,3,5,7,9]
print (binary_search(my_list, 5))
print (binary_search(my_list, 0))