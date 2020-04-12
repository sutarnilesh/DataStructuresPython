
from LinkedList.unordered_linkedlist import Node
#from .unordered_linkedlist import Node

class OrderedList(object):
  def __init__(self):
    self.head = None

  def search(self, item):
    current = self.head
    found = False
    stop = False

    while current and (not found) and (not stop):
      if current.getData() == item:
        found = True
      else:
        if current.getData() > item:
          stop = True
        else:
          current = current.getNext()
    return found

  def add(self, item):
    current = self.head
    previous = None
    stop = False

    while current and (not stop):
      if current.getData() > item:
        stop = True
      else:
        previous = current
        current =current.getNext()

    temp = Node(item)
    if previous is None:
      temp.setNext(self.head)
      self.head = temp
    else:
      temp.setNext(current)
      previous.setNext(temp)

  def isEmpty(self):
    return self.head is None

  def size(self):
    current = self.head
    count = 0
    while (current):
      count += 1
      current = current.getNext()

    return count

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))


