def shortBubbleSort(alist):
  """
  Compare adjacent elements and exchange those are out of order
  The O(n2) complexity
  :param alist:
  :return:
  """
  exchanges = True
  passnum = len(alist) - 1
  while passnum > 0 and exchanges:
    exchanges = False
    for i in range(passnum):
      if alist[i] > alist[i + 1]:
        exchanges = True
        temp = alist[i]
        alist[i] = alist[i + 1]
        alist[i + 1] = temp
    passnum = passnum - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)