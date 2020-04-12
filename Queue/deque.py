
class Deque(object):
  def __init__(self):
    self.items = list()

  def size(self):
    return len(self.items)

  def isEmpty(self):
    return self.items is list()

  def addFront(self, item):
    """
    O(1)
    :param item:
    :return:
    """
    self.items.append(item)

  def addRear(self, item):
    """
    O(n)
    :param item:
    :return:
    """
    self.items.insert(0, item)

  def removeFront(self):
    """
    O(1)
    :return:
    """
    return self.items.pop()

  def removeRear(self):
    """
    O(n)
    :return:
    """
    return self.items.pop(0)


# d=Deque()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(True)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.removeRear())
# print(d.removeFront())