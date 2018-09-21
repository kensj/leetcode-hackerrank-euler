# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        fin = []
        
        return self.addNums(l1, l2, carry, fin)
        
        
    def addNums(self, l1, l2, carry, fin):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2 and not carry:
            return fin
 
        val = 0
        if l1:
            val += l1.val
        if l2:
            val += l2.val
            
        val += carry
        
        if val >= 10:
            fin.append(val-10)
            self.addNums(l1.next if l1 else None, l2.next if l2 else None, 1, fin)
        else:
            fin.append(val)
            self.addNums(l1.next if l1 else None, l2.next if l2 else None, 0, fin)
        return fin