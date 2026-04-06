#problem 1 - stack implementation

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self._data.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self._data[-1]

    def size(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

#test stack
print("=" * 40)
print("Problem 1: Stack")
print("=" * 40)

s = Stack()
for val in [1, 2, 3]:
    s.push(val)
    print(f"Pushed {val}: {s}")

popped = s.pop()
print(f"Popped: {popped}")

print(f"Peek: {s.peek()}")
print(f"Stack: {s}")

#problem 2 - queue implementation

class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self._data.pop(0)

    def peek(self):
        if self.size() == 0:
            return None
        return self._data[0]

    def size(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


#test q
print("\n" + "=" * 40)
print("Problem 2: Queue")
print("=" * 40)

q = Queue()
for val in ['a', 'b', 'c']:
    q.enqueue(val)
    print(f"Enqueued {val}: {q}")

dequeued = q.dequeue()
print(f"Dequeued: {dequeued}")

print(f"Peek: {q.peek()}")
print(f"Queue: {q}")

#problem 3 - palindrome check w/ stack&queue

def is_palindrome(s):
    #lowercase, remove spaces
    cleaned = s.replace(" ", "").lower()

    stack = Stack()
    queue = Queue()

    for ch in cleaned:
        stack.push(ch)
        queue.enqueue(ch)

    while stack.size() > 0:
        if stack.pop() != queue.dequeue():
            return False

    return True


#test palindrome
print("\n" + "=" * 40)
print("Problem 3: Palindrome Check")
print("=" * 40)

test_strings = ["racecar", "A man a plan a canal Panama", "hello"]
for test in test_strings:
    result = is_palindrome(test)
    print(f"'{test}' is a palindrome: {result}")

#problem 4 - tokenizer + stack push/pop preview

def tokenize(expr):
    return expr.split()

#test tokenizer
print("\n" + "=" * 40)
print("Problem 4: Tokenize & Stack Preview")
print("=" * 40)

expression = "( 5 + 6 ) - 1 / 2"
tokens = tokenize(expression)
print(f"Expression: {expression}")
print(f"Tokens: {tokens}")

stack = Stack()
for token in tokens:
    stack.push(token)

pushed_order = ", ".join(tokens)
print(f"Pushed: {pushed_order}")

popped_tokens = []
while stack.size() > 0:
    popped_tokens.append(stack.pop())

print(f"Popped: {', '.join(popped_tokens)}")
