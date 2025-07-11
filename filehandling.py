#Learning File handling commands

#saving stuff from file to array

list = ["" , "" , ""]

def file_to_array():
    file = open("sample.txt")

    for i in range(3):
        list[i] = file.readline()

    print(list)
    file.close()

def changing_array():
    global list
    for i in range(3):
        print("enter a fruit")
        list[i] = input()
    print(list)    

def array_to_file():
    global list
    file = open("sample.txt", "w")
    for i in range(3):
        file.write(list[i] + "\n")
    file.close()
    file = open("sample.txt", "r")    
    print(file.read())
    file.close() 

file_to_array()
changing_array()
array_to_file()