
class Node(object):
  def __init__(self, initialdata):
    self.data = initialdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next =  newnext

  def __repr__(self):
    return repr(self.data)


class UnorderedList(object):

  def __init__(self):
    self.head = None

  def __repr__(self):
    nodes = list()
    current = self.head
    while current:
      nodes.append(repr(current))
      current = current.getNext()
    return '[' + ','.join(nodes) + ']'

  def isEmpty(self):
    return self.head is None

  def add(self, item):
    tempnode = Node(item)
    tempnode.setNext(self.head)
    self.head = tempnode

  def size(self):
    count = 0
    current = self.head
    while not current is None:
      count += 1
      current = current.getNext()

    return count

  def search(self, item):
    current = self.head
    found = False
    while (not current is None) and (not found):
      if current.getData() is item:
        found = True
      current = current.getNext()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False

    while not current:
      if current.getData() is item:
        found = True
      else:
        previous = current
        current = current.getNext()

    if previous is None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())

  def append(self, item):
    current = self.head
    while not current is None:
      current = current.getNext()
    current.setNext(item)

  def insert(self, position, item):
    newnode = Node(item)
    current = self.head
    previous = None
    found = False
    count = 0
    if position > self.size():
      raise IndexError("List index out of range")
    while not current is None and not found:
      if position is count:
        found = True
      else:
        previous = current
        current = current.getNext()
        count += 1
    if previous is None:
      newnode.setNext(self.head)
      self.head = newnode
    else:
      newnode.setNext(current)
      previous.setNext(newnode)

  def pop(self):
    """
    Delete items from end

    :return:
    """
    previous = None
    current = self.head
    if self.head is None:
      return None
    else:
      while not current.getNext() is None:
        previous = current
        current = current.getNext()
      previous.setNext(current.getNext())
      return current.getData()

  def index(self, node):
    """
    Find the index of node

    :param node:
    :return: index if found otherwise None
    """
    count = 0
    current = self.head
    found = False
    while current and (not found):
      if current.getData() is node.getData():
        found = True
        break
      count += 1
      current = current.getNext()
    if found:
      return count


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
mylist.insert(1, 10)
print("items", mylist)
print("poppeditem =", mylist.pop())
print("items", mylist)
node = Node(31)
print("Index=", mylist.index(node))
print("Search=", mylist.search(31))