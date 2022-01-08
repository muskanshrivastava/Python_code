from os import system

system('cls')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def createNode(self,value):
        newNode = Node(value)
        self.head = newNode
        
    def beginInsert(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head.next
            self.head = newNode        

    def lastInsert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node

        temp = self.head

        while temp.next != None:
            temp = temp.next
            temp.next = node


    def middleInsert(self,value,loc):
        node = Node(value)
        if self.head == None:
            self.head = node

        temp = self.head
        counter = 1
        while counter < loc:
            temp = temp.next
            counter += 1

        node.next = temp.next
        temp.next = node
        # display(node)

    def searchElement(self,ele):
        temp = self.head
        counter = 1
        while temp.data != ele:
            temp = temp.next
            counter += 1
        print("\nElement {temp.data} is found at node {counter}")

    def display(self):
        if self.head == None:
            print("\nList is empty")
        else:
            temp = self.head
            while temp.next != None:
                print(temp.data, end= ' ')


if __name__ == '__main__':

    operationList = [ 'Create Node',
                    'Insert at beginning',
                    'Insert at middle',
                    'Insert at last',
                    'search element',
                    'display linkedlist' ]
                    
    nodeObj = linkedList()

    for index,item in enumerate(operationList):
        print(index + 1,item)

    while True:
        option = int(input("Select option to perform operations : "))

        if option == 1:
            value = input("Enter value to be inserted : ")
            nodeObj.createNode(value)

        elif option == 2:
            value = input("Enter value to be inserted at beginning : ")
            nodeObj.beginInsert(value)
            nodeObj.display()

        elif option == 3:
            value = input("Enter value to be inserted at middle : ")
            location = input("Enter the location on that value to be inserted : ")
            nodeObj.middleInsert(value,location)

        elif option == 4:
            value = input("Enter value to be inserted at last : ")
            nodeObj.lastInsert(value)

        elif option == 5:
            value = input("Enter value to be searched : ")
            nodeObj.searchElement(value)

        elif option == 6:
            nodeObj.display()

        option = input("Do you want to perform more operations [y/n] : ")
        
        if option in ['Y','y'] :
            continue
        else:
            # exit()
            break

    