def insert(L, x):
    """
    insert an element x into a sorted list L

    Arguments:
        L: list
        x: integers
    Return:
        sorted_L: list
    """
    result = L[:]  
    for i in range(len(result)):
        if result[i] >= x:
            result.insert(i, x)
            return result
    result.append(x)  
    return result

