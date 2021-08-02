
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[self.size()-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    def getMin(self):
        return min(self.container)

def NGR(stack:deque,arr:[int],ans:[int]):
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            ans.append(-1)
        elif stack[len(stack)-1]>arr[i] and len(stack)>0:
                ans.append(stack[len(stack)-1])
        elif stack[len(stack)-1]<arr[i] and len(stack)>0:
                while len(stack)>0:
                    if arr[i]<stack[len(stack)-1]:
                        ans.append(stack[len(stack)-1])
                        break
                    stack.pop()
                if len(stack)==0:
                    ans.append(-1)

        stack.append(arr[i])

    return list(reversed(ans))




