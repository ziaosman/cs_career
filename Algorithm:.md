Algorithm:
- Set of rules a computer follows to solves a problem, perform a calculation, or process data. 

Big O Notation:
- Runtime of algorithm is expressed in Big O
- N represents number of operations, it defines the growth of operations of an alogirhtm and not the speed in a unit
- Establishes the worst case scenario
- O(log n) - log time, ex: binary search
- O(n) - linear time, ex: simple search
- O(n * log n) - fast sorting algorithms, ex: quick sort
- O(n^2) - slow sorting alogrithm, ex: selection sort
- O(n!) - factorial time, ex: traveling salesperson

Chapter 2: Sort

Memory: refers to location of short term data

Arrays:
- Elements are stored next to eachother in memory (contigously)
- Solutions to this: reserving extra slots in memory (con you might not use them and you may need even more than the extra slots you reserved) 

Linked Lists:
- Elements can be stored anywhere in memory
- Each item stores the address of the next item in the list, hence the word "linked"
- If there is space in memory, there is space for a linkedlist because the addresses in memory do not have to be contigious like with arrays
- Cons: to read the last item of a linked list you have to parse through each item to get the right address, for arrays you don't have this issue because each item is stored contigiously so you can access the address of each element easily

Pros vs Cons
- Arrays allow for faster reads (random access)
- Linked Lists are great for inserts because elements can be stored anywhere in memory (sequential access)


Terminology:
Index = position of an element, "20 is at index 1"

Big O Notation
        Reading Insert
Arrays  O(1)    O(n)
List    O(n)    O(1)

Insertions and Deletions are more efficient with Lists because you just have to change what an element points to where as for an array you have to shift all the elements and ensure there is enough ordered space in memory
        Array   Lists
Read    O(1)    O(n)
Inserts O(n)    O(1)
Delete  O(n)    O(1)