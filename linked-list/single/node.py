#Node Class

class Node:
    #constructor
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;

    #method for setting the data field of the Node
    def setData(self,data):
        self.data = data
    #method for getting the data field of the Node
    def getData(self):
        return self.data
    #method for setting the next field of the Node
    def setNext(self,next):
        self.next = next
    #method for getting the next field of the Node
    def getNext(self):
        return self.next
    #return true if the node points to another node
    def hasNext(self):
        return self.next != None

#Linkedlist class

class LinkedList:
    #constructor
    def __init__(self):
        self.head = None

    # inserting the node at the begining
    def insertAtStart(self,data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

        # self.length +=1

    # insert at end

    def insertAtEnd(self,data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode

    # insert at any position
    def insertBetween(self,previousNode,data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode

    #print linked list

    def printLinkedList(self):
        tmp = self.head
        while(tmp):
            print(tmp.data, end=' ')
            tmp = tmp.next



############################################
#   Invocation section                     #
############################################


if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)                # create the head node
    node2 = Node(2)
    List.head.setNext(node2)           # head node's next --> node2
    node3 = Node(3)
    node2.setNext(node3)               # node2's next --> node3
    List.insertAtStart(4)              # node4's next --> head-node --> node2 --> node3
    List.insertBetween(node2, 5)       # node2's next --> node5
    List.insertAtEnd(6)
    List.printLinkedList()
    print()

    List.printLinkedList()
    print()







