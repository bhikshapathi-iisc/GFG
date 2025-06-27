def insert(head, data):
    ptr=Node(data)
    if head == None:
       head=ptr
    else:
        ptr.npx=head
        head=ptr
    return ptr
        
    
def getList(head):
    ans=[]
    while head != None:
        ans.append(head.data)
        head=head.npx
    return ans