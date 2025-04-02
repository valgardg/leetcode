from collections import defaultdict
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.minVals = defaultdict(list)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == None:
            self.min = val
            self.minVals[val] = [val]
        else:
            if val <= self.min:
                self.minVals[val].append(self.min)
                self.min = val

    def pop(self) -> None:
        popped = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        else:
            if popped == self.min:
                new_min = self.minVals[popped][-1]
                self.min = new_min
                self.minVals[popped].pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Test input
functions = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
arguments = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

# Initialize the object and test the methods
min_stack = None
output = []
for func, arg in zip(functions, arguments):
    print(f"calling {func} with {arg}")
    if func == "MinStack":
        min_stack = MinStack()  # Initialize the stack
        output.append(None)
    elif func == "push":
        min_stack.push(*arg)  # Call push with the provided arguments
        output.append(None)
    elif func == "pop":
        min_stack.pop()  # Call pop with no arguments
        output.append(None)
    elif func == "top":
        output.append(min_stack.top())  # Call top and print the result
    elif func == "getMin":
        output.append(min_stack.getMin())  # Call getMin and print the result
    if min_stack != None:
        print(f"min: {min_stack.min}\nminVals: {min_stack.minVals}\nstack: {min_stack.stack}\n")

print(output)