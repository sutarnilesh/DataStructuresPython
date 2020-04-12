from Queue.deque import Deque

def palinchecker(aString):
  chardeque = Deque()
  for ch in aString:
    chardeque.addRear(ch)

  stillEqual = True

  while chardeque.size() > 1 and stillEqual:
    first = chardeque.removeFront()
    last = chardeque.removeRear()
    if first != last:
      stillEqual = False

  return stillEqual

print(palinchecker("lsdkjfskf"))
print(palinchecker("radar"))