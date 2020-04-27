
"""
Balanced parentheses means that each opening/general symbol has a corresponding closing symbol and
the pairs of parentheses are properly nested
"""
from datastructures.Stack.stack import Stack

def parChecker(symbolString):
  s = Stack()
  balanced = True
  index = 0
  length = len(symbolString)
  while index < length and balanced:
      symbol = symbolString[index]
      if symbol in '([{':
        s.push(symbol)
      else:
        if s.isEmpty():
          balanced = False
        else:
          top = s.pop()
          if not matches(top, symbol):
            balanced = False
      index += 1

  if balanced and s.isEmpty():
    return True
  else:
    return False


def matches(opensymbol, closesymbol):
  opens = '([{'
  closers = ')]}'

  return opens.index(opensymbol) == closers.index(closesymbol)

print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))