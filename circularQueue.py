class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], " ")
            print()
        else:
            for i in range(self.head, self.k): 
                print(self.queue[i],  " ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], " ")
            print()


obj = MyCircularQueue(8)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(7)
obj.enqueue(8)
obj.enqueue(9)
print("Initial")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()

obj.enqueue(6)
print("After adding new element")
obj.printCQueue()