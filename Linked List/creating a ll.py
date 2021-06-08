class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeInput():
    s=list(map(int,input("Enter the string").split()))
    head=None
    tail=None
    for ele in s:
        if ele==-1:
            return head
        new=Node(ele)
        if head is None:
            head=new
            tail=new
        else:
            tail.next=new
            tail=new
    return head

def display(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
def length(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c
        
head=takeInput()
print(display(head))
print(length(head))
        
            
        
    
