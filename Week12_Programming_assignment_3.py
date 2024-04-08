def std_dev(X):
    """
    Compute the standard deviation
    
    Argument:
        X: list of integers
    Return:
        sigma: float
    """
    n = len(X)
    X_mean = sum(X) / n
    variance = sum((x - X_mean)**2 for x in X) / (n - 1)
    return variance**0.5
