class Node:
    pass
    
class LinkedList:
    def createNode(self,data):
        node = Node()
        node.data =data
        node.next = None
        return node
    def set_head(self):
        self.head = None
        
    def append(self,data):
        new_node = self.createNode(data)
        
        if self.head is None:
            self.head= new_node
            return
        current =self.head
        
        while current.next:
            current = current.next
        current.next = new_node
        
    def display(self):
        if self.head is None:
            print("List is empty")
            
            return
        current =self.head
        while current:
            print(current.data, end =" -> ")
            current = current.next
        print("None")
        
ll = LinkedList()
ll.set_head() 
ll.append(5)
ll.append(15)
ll.display()

