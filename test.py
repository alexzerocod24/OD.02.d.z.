class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("\nОчередь после добавления элементов:", queue.items)
print("Первый элемент очереди:", queue.front())
print("Извлечённый элемент:", queue.dequeue())
print("Очередь после извлечения элемента:", queue.items)