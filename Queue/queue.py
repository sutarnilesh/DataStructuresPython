class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    """
    O(n)
    :param item:
    :return:
    """
    self.items.insert(0, item)

  def dequeue(self):
    """
    O(1)
    :return:
    """
    return self.items.pop()

  def size(self):
    return len(self.items)