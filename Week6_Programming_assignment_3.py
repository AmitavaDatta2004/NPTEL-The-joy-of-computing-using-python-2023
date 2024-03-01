def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return steps(n-1) + steps(n-2) + steps(n-3)
