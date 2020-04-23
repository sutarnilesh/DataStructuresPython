
"""
The quick sort uses divide and conquer to gain the same advantages as the merge sort,
while not using additional storage.

A quick sort first selects a value, which is called the pivot value. We will simply use the first item in the list.
The role of the pivot value is to assist with splitting the list. The actual position where the
pivot value belongs in the final sorted list, commonly called the split point,
will be used to divide the list for subsequent calls to the quick sort.
"""


def quickSort(alist):
  quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
  if first < last:
    splitpoint = partition(alist, first, last)

    quickSortHelper(alist, first, splitpoint - 1)
    quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
  pivotvalue = alist[first]

  leftmark = first + 1
  rightmark = last

  done = False
  while not done:

    while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
      leftmark = leftmark + 1

    while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
      rightmark = rightmark - 1

    if rightmark < leftmark:
      done = True
    else:
      temp = alist[leftmark]
      alist[leftmark] = alist[rightmark]
      alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
