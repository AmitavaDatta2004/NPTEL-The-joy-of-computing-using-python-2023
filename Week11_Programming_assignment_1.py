def factors(n):
    """
    Compute the set of factors of n
			
    Argument:
        n: integer
    Return:
        factors_of_n: set
    """
    factor_set = set()
    for i in range(1, n + 1):
        if n % i == 0:
            factor_set.add(i)
    return factor_set

def common_factors(a, b):
    """
    Compute the set of common factors of a and b

    Arguments:
        a, b: integers
    Return:
        factors_common: set
    """
    factors_a = factors(a)
    factors_b = factors(b)
    return factors_a.intersection(factors_b)

def factors_upto(n):
    """
    Get the factors up to n 
	
    Argument:
        n: integer
    Return:
        result: dict (keys: integers, values: sets)
    """
    factor_dict = {}
    for i in range(1, n + 1):
        factor_dict[i] = factors(i)
    return factor_dict
