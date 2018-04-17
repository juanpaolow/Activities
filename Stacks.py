class ImStack:
    def __init__(self):
        print "LIST MANIPULATION USING STACK"
        self.items = input("\nEnter a list of strings:")
        self.items = list(self.items)

    def sort(self):
        return sorted(self.items)

    def reverse(self):
        return self.items[::-1]

    def isEmpty(self):
        return self.items == []

    def insert(self,value,item):
        return  self.items.insert(value,item)

    def push(self, item):
        return self.items.append(item)

    def append(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    aub = ImStack()
    def qt():

        rey = 0
        print ("\n1. SORT THE LIST \n2. REVERSE THE LIST \n3. ADD AN ITEM \n4. INSERT AN ITEM \n5. GET THE SIZE \n6. COUNT THE PALINDROME")
        x = input("\nChoose the action you want: ")
        if x == 1:
            print "SORTED VERSION: ",aub.sort()
        elif x == 2:
            rey1 = []
            while aub.isEmpty() == False:
                rey1.append(aub.peek())
                aub.pop()
            print "REVERSED VERSION:", rey1
            return 0

        elif x == 3:
            au = input("\tEnter the word you wanna add: ")
            aub.push(au)
            print "\t",aub.items
        elif x == 4:
            au = input("\tInsert: ")
            br = input("\tIndex: ")
            aub.insert(br, au)
            print "\t",aub.items
        elif x == 5:
            print "SIZE:",aub.size()
        elif x == 6:
            while aub.isEmpty() == False:
                if aub.peek() == aub.peek()[::-1]:
                    rey += 1
                aub.pop()
            print "TOTAL PALINDROME: ", rey
            return 0


        return qt()
    qt()