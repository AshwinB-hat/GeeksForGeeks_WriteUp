# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def getMiddle(self,head):
        if(head is None):
            return head
        slow = head
        fast = head.next
        while(fast is not None):
            fast = fast.next 
            if(fast is not None):
                fast = fast.next 
                slow = slow.next
        return slow 
    
    def sortedMerge(self,a,b):
        result = None
        if(a is None):
            return b
        if(b is None):
            return a
        while(a is not None and b is not None):
            if(a.val <= b.val):
                if(result is None):
                    result = a
                    head = result 
                else:
                    result.next = a
                    result = result.next 
                a=a.next
            else:
                if(result is None):
                    result = b
                    head = result
                else:
                    result.next = b
                    result = result.next
                b = b.next
        if(a is not None):
            result.next = a
            result = result.next 
        elif(b is not None):
            result.next = b 
            result = result.next 
        return head
        
    def sortList(self, A):
        if(A is None or A.next is None):
            return A
        
        middle = self.getMiddle(A)
        nextOfMiddle = middle.next 
        middle.next = None
        
        left = self.sortList(A)
        right = self.sortList(nextOfMiddle)
        
        sortedList = self.sortedMerge(left,right)
        
        return sortedList
        
        
        
