"""
Instead of searching the list in sequence, a binary search will start by examining the middle item.
If that item is the one we are searching for, we are done. If it is not the correct item,
we can use the ordered nature of the list to eliminate half of the remaining items.
If the item we are searching for is greater than the middle item, we know that the entire lower half
of the list as well as the middle item can be eliminated from further consideration.
The item, if it is in the list, must be in the upper half.

The number of comparisons necessary to get to this point is i where n/2^i=1. Solving for i gives us i=logn
The binary search is O(logn )
"""


def binarySearch(alist, item):
  if len(alist) == 0:
      return False
  else:
      midpoint = len(alist)//2
      if alist[midpoint] == item:
        return True
      else:
        if item<alist[midpoint]:
          return binarySearch(alist[:midpoint], item)
        else:
          return binarySearch(alist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))