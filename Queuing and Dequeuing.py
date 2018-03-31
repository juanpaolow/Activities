#QUEUING AND DEQUEUING
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

class Queue:
    def __init__(self):
        self.items = (list(range( A, B+1 )))
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]


if __name__ =="__main__":

    A = input("ENTER A LIST OF INTEGERS RANGING\nFROM: ")
    B = input("UP TO: ")
    C = Queue()
    J = 0
    P = (C.size()/2)-1
    PAO = input("CHOICES \n1. DISPLAY ALL EVEN NUMBERS\n2. DISPLAY ALL ODD NUMBERS\nENTER YOUR CHOICE: ")
    if PAO == 1:
        if B %2==0:
            while J <= P:
                C.enqueue(C.peek())
                C.dequeue()
                C.dequeue()
                J+=1
            print "\t",sorted(C.items)
            print "\t",A,"to",B,"contains",len(C.items),"even numbers"
        elif A%2 == 0 and B%2 == 1:
            while J <= P:
                C.dequeue()
                C.enqueue(C.peek())
                C.dequeue()
                J += 1
            print "\t",sorted(C.items)
            print "\t",A, "to", B, "contains", len(C.items), "even numbers"
        elif A%2 == 1and B%2 == 1:
            while J <= P+1:
                C.dequeue()
                C.enqueue(C.peek())
                C.dequeue()
                J += 1
            print "\t",sorted(C.items)
            print "\t",A, "to", B, "contains", len(C.items), "even numbers"

    elif PAO == 2:
        if B %2 == 0:
            while J <= P:
                C.dequeue()
                C.enqueue(C.peek())
                C.dequeue()
                J += 1
            print "\t",sorted(C.items)
            print "\t",A, "to", B, "contains", len(C.items), "even numbers"
        elif A%2 == 0 and B%2 == 1:
            while J <= P:
                C.enqueue(s.peek())
                C.dequeue()
                C.dequeue()
                x += 1
            print "\t",sorted(C.items)
            print "\t",A, "to", B, "contains", len(C.items), "even numbers"
        elif A%2 == 1and B%2 == 1:
            while J <= P:
                C.enqueue(C.peek())
                C.dequeue()
                C.dequeue()
                J += 1
            print "\t",sorted(C.items)
            print "\t",A, "to", B, "contains", len(C.items), "even numbers"