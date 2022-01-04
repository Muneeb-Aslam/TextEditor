"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  <WRITE YOUR COMPLETE NAME AND SECTION HERE>
""" 

from os import curdir
from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list."""
        self._header = None
        self._trailer = None
        self._current = None
        self._size = 0

    def push(self,item):
        new_node = Node2Way(item)

        if self._header is None:
            self._header=new_node
            self._trailer=self._header
            self._current=self._header
            return
        self._trailer.next=new_node
        new_node.previous=self._trailer
        self._trailer=new_node





    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer





    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list")
        return self._current.getPrevious() !=None




    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        self._current=self._header



        
    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        self._current=self._trailer



    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if self.hasNext():
            self._current=self._current.next
        else:
            raise AttributeError("List has no next item")




    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one iten"""
        if self.hasNext:
            self._current=self._current.previous
        else:
            raise AttributeError("List has no next item")





    def insertAfter(self, item):
        
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        item+="\n"
        new_node = Node2Way(item)

        if self._header is None:
            self._header=new_node
            self._trailer=self._header
            self._current=self._header
            return
        new_node.next = self._current.next
        
        self._current.next = new_node

        new_node.previous = self._current

        if new_node.next:
            new_node.next.previous = new_node
        self._current=new_node

        



    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        item+="\n"
        node=Node2Way(item)

        if self._current==self._header:
            node.next=self._current
            self._current.previous=node
            self._header=node
            self._current=self._header
            return

        node.next=self._current
        self._current.previous.next=node
        node.previous=self._current.previous
        self._current.previous=node
        self._current=node



    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        return self._current.data



    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        str=self._trailer.data
        self._trailer.previous.next=None
        return str



    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            print("list is empty")
            return 
        self._current.data=newItemValue



    def isEmpty(self):
        return self._header==None



    def __len__(self):
        """ Returns the number of items in the list."""
        temp=self._header
        self._size=0
        while temp is not None:
            self._size=self._size+1
            temp=temp.next
        return self._size



    def __str__(self):
        """Includes items from first through last."""
        # replace below
        head=self._header
        string="\n"
        while(head is not None):
            string=string+str(head.data)
            head=head.next
        return string




    def Read_File_Data(self):
        """This function is used to read data from file and insert into the the cursor based list
        """ 
        file=open("textfile.txt","r")
        for i in file:
            self.push(i)
        file.close()
        

if __name__=="__main__":
    pass