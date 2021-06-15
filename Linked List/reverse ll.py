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
        
def find(head):
    n=int(input("Enter the element to be searched"))
    c=0
    while head:
        if head.data==n:
            return c
        c+=1
        head=head.next
    return -1
            
    
def length(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c

def reversePrint(llist):
    if llist is None or llist.next is None:
        return llist
    smallhead=reversePrint(llist.next)
    curr=smallhead
    while curr.next is not None:
        curr=curr.next
    
    curr.next=llist
    llist.next=None
    
    return smallhead

def ith(head):
    i=int(input("Enter the position"))
    count=0
    while head:
        
       
        if count==i:
            return head.data
            break
        count+=1
        head=head.next
    return -1
        
head=takeInput()
print(display(head))
print(length(head))
#print(ith(head))
#print(find(head))
h=reversePrint(head)
print(display(h))

