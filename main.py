class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Стек после добавления элементов:", stack.items)
    print("Верхний элемент стека:", stack.peek())
    print("Извлечённый элемент:", stack.pop())
    print("Стек после извлечения элемента:", stack.items)