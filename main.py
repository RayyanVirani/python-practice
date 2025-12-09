
class Queue:
    def __init__(self):
        self.QueueArray = []
        for x in range(100):
            self.QueueArray.append(-1)
        self.HeadPointer = -1
        self.TailPointer = 0
TheQueue = Queue()

AQueue = Queue()


def ReturnAllData(TheQueue):
    for i in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        AllData = str(TheQueue.QueueArray[i]) + " "
        return AllData

def Enqueue(TheQueue, TheData):
    if TheQueue.HeadPointer == -1:
        TheQueue.QueueArray[TheQueue.TailPointer] = TheData
        TheQueue.HeadPointer = 0
        TheQueue.TailPointer = TheQueue.TailPointer + 1
        return 1, TheQueue
    elif TheQueue.TailPointer > 99:
        return -1, TheQueue
    else:
        TheQueue.QueueArray[TheQueue.TailPointer] = TheData
        TheQueue.TailPointer = TheQueue.TailPointer + 1
        return 1, TheQueue
    
for i in range(10):
    while True:   
            try:
                for i in range(10):
                    userinput = int(input("Enter an integer number with a value of 0 or greater: "))
                    if userinput >= 0:
                        print(userinput)
                        if Enqueue(TheQueue, userinput) == -1:
                            print("The Queue is Full")
                            break
                        else:
                            print("Item has been added to Queue.")
                            break
                    else:
                        userinput = str(userinput)       
            except ValueError:
                print("Please Enter a Valid integer number of 0 or above")

print(ReturnAllData(TheQueue))