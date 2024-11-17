import os
import sys
from datetime import date
import traceback as tb

def write_to_file(file_path, file_mode, value):
    """_summary_
    
    args:
        file_path(_type):_description_
        file_mode(_type):_description_
        value(_type):_description_
    """
    try:
        file_object = open(file_path,file_mode)
        file_object.write(value)
        file_object.close()
    except:
        tb.print_exc()
        
def read_from_file():
   pass

def main():
    print("file handiling in python")
    
    # name = input()
    # name = sys.stdin.readline()
    # print(name)
    
    
    file_test = open("/Users/Isaia/Desktop/Bushnell_Computer_Science/SFTE_365_Game_Development/Week4/test.txt","w")
    print("Name of the file: ", file_test.name)
    print("Closed or not: ", file_test.closed)
    print("Opening mode: ", file_test.mode)
    
    
    file_test.write("John Smith.\nThis is good!\n")
    
    
    file_test.close()
    
if __name__ == '__main__':
    main()