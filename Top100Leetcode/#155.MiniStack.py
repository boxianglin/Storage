#  General Approach
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.min.append(val)
        else:
            self.stack.append(val)
            newMin = min(val, self.min[-1])
            self.min.append(newMin)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


minStack = MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin()); #-3
minStack.pop();
print(minStack.top()); #0
print(minStack.getMin()); #-2

print('-------------')
# Advance Approach
# Using only O(1) time and space for track down the min value
class MinStacks:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None:
        if self.stack == []:
            self.min = val
            self.stack.append(val-self.min) #0
        else:
            diff = val - self.min
            self.min = self.min if diff >= 0 else val # if difference >= 0 min no change
            self.stack.append(diff)

    def pop(self) -> int:
        top_val = self.top()
        diff = self.stack.pop()
        self.min = self.min if diff >= 0 else self.min - diff
        return top_val

    def top(self) -> int:
        diff = self.stack[-1]
        return self.min+diff if diff > 0 else self.min
        #1) because min are update each push, if diff<0, meaning val-prev.min < 0 == val<prev.min,
        #   val will be assign as new.min, so we can just return the min
        #2) diff > 0, simply means val>prev.min => val = prev.min + x, where x = diff accords from push setup

    def getMin(self) -> int:
        return self.min
minStacks = MinStacks()
minStacks.push(-2);
minStacks.push(0);
minStacks.push(-3);
print(minStacks.pop());
print(minStacks.pop());
print(minStacks.pop());
