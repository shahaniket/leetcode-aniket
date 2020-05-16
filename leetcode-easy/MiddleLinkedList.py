#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:39:01 2020

@author: anikts
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

    def Middle_Node(self, head):
        slow, fast = head, head
        
        while fast:
            
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break
        
            slow = slow.next
        
        return slow


llist = SLinkedList()
llist.Atbegining(5)
llist.Atbegining(4)
llist.Atbegining(3)
llist.Atbegining(2)
llist.Atbegining(1)
#llist.LListprint()
print(llist.Middle_Node(llist.head).data)