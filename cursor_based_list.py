"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  <WRITE YOUR COMPLETE NAME AND SECTION HERE>
""" 

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list."""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0


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
        if self.hasNext:
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
        

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        pass

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        pass

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        pass

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        pass

    def isEmpty(self):
        return self._header

    def __len__(self):
        """ Returns the number of items in the list."""
        temp=self._header
        counter=0
        while temp is not None:
            counter+=1
            temp=temp.next
        return counter

    def __str__(self):
        """Includes items from first through last."""
        # replace below
        temp=self._header
        while temp is not None:
            print(str[i]," ")
            temp=temp.next
