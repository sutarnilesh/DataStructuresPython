
class Stack(object):
  def __init__(self):
    self.items = list()

  def size(self):
    return len(self.items)

  def isEmpty(self):
    return self.items == list()

  def push(self, item):
    self.items.append(item)

  # def push(self, item):
  #   self.items.insert(0, item)

  def pop(self):
    return self.items.pop()

  # def pop(self):
  #     return self.items.pop(0)

  def peek(self):
    return self.items[self.size() -1]

  # def peek(self):
  #   return self.items[0]

def revstring(mystr):
  mystack= Stack()
  for ch in mystr:
    mystack.push(ch)

  revstr = ""
  while not mystack.isEmpty():
    revstr = revstr + mystack.pop()
  return revstr


assert(revstring('apple') =='elppa')
assert(revstring('x') == 'x')
assert (revstring('1234567890') == '0987654321')
