from Stack.stack import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        print(decNumber)
        rem = decNumber % base
        print(rem)
        remstack.push(rem)
        decNumber = decNumber // base
        print("decNumber ", decNumber)
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

#print(baseConverter(25,2))
#print(baseConverter(25,16))
print(baseConverter(256, 16))