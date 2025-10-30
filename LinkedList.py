#My version of a linked list

#Define linked list class
class LinkedList:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

MainList = [None] * 100

def InitializeList():
    global startpointer, nullpointer, freepointer, currentpointer
    nullpointer, startpointer = -1, -1
    freepointer, currentpointer = 0, 0

"""InitializeList()
temp = input()
num = input()
MainList[currentpointer] = LinkedList(temp, num)
print(MainList[0].data , MainList[0].pointer)"""

def insert(dataitem):
    global startpointer, nullpointer, freepointer, currentpointer
    if freepointer < len(MainList):
        NewNode = LinkedList(dataitem, nullpointer)
        if startpointer == nullpointer:
            currentpointer = freepointer
            MainList[currentpointer] = NewNode
            startpointer = freepointer
            freepointer += 1
        else:
            currentpointer = startpointer
            while currentpointer != nullpointer:
                previouspointer = currentpointer
                currentpointer = MainList[currentpointer].pointer
            MainList[previouspointer].pointer = freepointer
            MainList[freepointer] = NewNode
            freepointer +=1

def view():
    global startpointer, nullpointer, freepointer, currentpointer
    if startpointer == nullpointer:
        print("List is empty!")
    else:
        currentpointer = startpointer
        while currentpointer != nullpointer:
            print(f"Data: {MainList[currentpointer].data} , Pointer: {MainList[currentpointer].pointer}")
            currentpointer = MainList[currentpointer].pointer
InitializeList()
for i in range(5):
    temp = input("Enter first Data: ")
    insert(temp)
view()           