def survival(T):
    """
    Determine if the organism will survive or not
    
    Argument:
        T: integer
    Return:
        result: bool
    """
    for x in range(6):
        for y in range(6):
            if f(x, y) <= T:
                return True
    return False

def f(x, y):
    return 30 + x**2 + y**2 - 3*x - 4*y
