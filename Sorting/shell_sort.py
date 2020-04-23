
"""
Breaks the original list into no. of smaller sublists, each of which is sorted using Insertion sort.
The unique way that these sublists are chosen is the key to the shell sort. Instead of breaking the list
into sublists of contiguous items, the shell sort uses an increment i, sometimes called the gap,
to create a sublist by choosing all items that are i items apart.
"""


def shellSort(alist):
  sublistcount = len(alist)//2
  while(sublistcount > 0):
    for startposition in range(sublistcount):
      gapInsertionSort(alist, startposition, sublistcount)

    print("After increments of size", sublistcount,
          "The list is", alist)

    sublistcount = sublistcount // 2


def gapInsertionSort(alist, start,gap):
  for i in range(start+gap, len(alist), gap):
    currentvalue = alist[i]
    position = i

    while position >= gap and alist[position - gap] > currentvalue:
      alist[position] = alist[position - gap]
      position = position - gap

    alist[position] = currentvalue


alist = [54,26,93,17,77,31,44,55,20]
alist = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
shellSort(alist)
print(alist)
