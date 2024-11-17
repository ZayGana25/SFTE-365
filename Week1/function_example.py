import traceback as tb 

def function_name(argument_1, argument_2):
    """do math multiplication
    Args:
        argument_1 (int): number 1
        argument_2 (int): number 2
    Returns:
    float: math division value
    """
    
    a = None
    try:
        a = argument_1 / argument_2
    except:
        print('an error occurred')
        tb.print_exc()
    return a

def main():
    print('python functions')
    
    result = function_name(1, 0)
    print(result)
    
if __name__ == '__main__':
    main()