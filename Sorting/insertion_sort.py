"""
It maintains a sorted sublist. Each new item is inserted back into the previous sublist
such that sorted sublist is one item larger.
"""


def insertionSort(alist):
  for index in range(1, len(alist)):

    currentvalue = alist[index]
    position = index

    while position > 0 and alist[position-1] > currentvalue:
      alist[position] = alist[position-1]
      position = position - 1

    alist[position] = currentvalue

#alist = [54,26,93,17,77,31,44,55,20]
alist = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
insertionSort(alist)
print(alist)