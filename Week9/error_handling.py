
import os
os.system("clear")
import traceback as tb


def math_division(a, b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        c = a/b
    except:
        tb.print_exc()
    finally:
        pass
    return c

    


def main():
    print("Error Handling in Python")
    
 
    a = 1
    b = 0
    if b == 0:
        raise ValueError("b should not be a 0, can't divide by 0.")   
        exit()
    c = math_division(a, b)
    print(c)
    
    
if __name__ == '__main__':
    main()