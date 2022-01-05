"""
File: cursorBasedListTester.py

Menu-driven tester for Cursor-Based List implementation
"""

from os import remove, replace
from cursor_based_list import CursorBasedList


def testList(myList):
    while True:
        print("\n=============================================================================================================================")
        print("Current List:",myList),"\n\n\n"
        if myList.isEmpty():
            print("Empty list")
        else:
            print("\t\t\t\t length:",len(myList), " \t\tCurrent item:", myList.getCurrent())
        print("\nTest Positional List Menu:")
        print("A - insertAfter")
        print("B - insertBefore")
        print("C - getCurrent")
        print("E - isEmpty")
        print("F - First")
        print("L - Last")
        print("N - Next")
        print("P - Previous")
        print("R - Remove")
        print("D - Pop")
        print("G - Replace_Word")
        print("H - Find_Word")
        print("X - Exit Program")
        response = input("Menu Choice? ").upper()
        if response == 'A':
            item = input("Enter the new item to insertAfter: ")
            myList.insertAfter(item)
        elif response == 'B':
            item = input("Enter the new item to insertBefore: ")
            myList.insertBefore(item)
        elif response == 'C':
            item = myList.getCurrent()
            print("The current item in the list is:",item)
        elif response == 'E':
            print("isEmpty returned:", myList.isEmpty())
        elif response == 'F':
            myList.first()
        elif response == 'L':
            myList.last()
        elif response == 'N':
            myList.next()
        elif response == 'P':
            myList.previous()
        elif response == 'R':
            myList.remove()
        elif response == 'U':
            item = input("Enter replacement item: ")
            myList.replace(item)
        elif response == 'D':
            item = myList.pop()
            print("removed item is ", item)
        elif response == 'G':
            str=input("Enter the item ")
            str1=input("Enter the item to be replace  ")
            myList.replace_word(str,str1)
        elif response == 'H':
            str=input("Enter the item ")
            myList.find_word(str)
        elif response == 'X':
            break
        else:
            print("Invalid Menu Choice!")

if __name__=="__main__":
    testList()

