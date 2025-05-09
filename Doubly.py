
class Node:
    def _init_(self, data):
        self.data= data
        self.next=None
        self.prev=None

node1=Node(15)
node2=Node(20)
node3=Node(25)
node4=Node(30)

node1.next=node2
node2.prev=node1

node2.next=node3
node3.prev=node2

node3.next=node4
node4.prev=node3

print("Traversing forward:\n")
currentNode=node1
while currentNode:
    print(currentNode.data, end="->")
    currentNode= currentNode.next
print("None")

print("Traversing backwards:\n")
currentNode=node4
while currentNode:
    print(currentNode.data, end="->")
    currentNode=currentNode.prev
print("None")