import os
from cursor_based_list import CursorBasedList 
import cursorBasedListTester
import os 
def menu():
    list=CursorBasedList()
    filename=input("Enter the file to edit..................\n")
    if not (os.path.exists(filename)):
        print("File does not exist\nFile created Successfully...........")
        with open(filename,"w") as file:
            pass
    list.Read_File_Data(filename)
    cursorBasedListTester.testList(list)
    list.Write_Data(filename)

if __name__=="__main__":
    print("\n\n---------------------------------------\t Welcome to Simple Text Editor\t-----------------------------------------------------\n\n")
    menu()
