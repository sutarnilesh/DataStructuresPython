def selectionSort(alist):
  """

  Find the largest element is each pass and place it in appropriate place.
  The O(n2) complexity
  :param alist:
  :return:
  """
  for fillslot in range(len(alist) - 1, 0, -1):
    positionOfMax = 0
    for location in range(1, fillslot + 1):
      if alist[location] > alist[positionOfMax]:
        positionOfMax = location

    temp = alist[fillslot]
    alist[fillslot] = alist[positionOfMax]
    alist[positionOfMax] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)