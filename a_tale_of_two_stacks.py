class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.reverse_stack = []
    def move(self):
        if len(self.reverse_stack) == 0:
            while len(self.stack)>0:
                self.reverse_stack.append(self.stack[-1])
                self.stack.pop()
    def peek(self):
        self.move()
        return self.reverse_stack[-1]        
    def pop(self):
        self.move()
        self.reverse_stack.pop()
    def put(self, value):
        self.stack.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())