def pearson(X, Y):
    n = len(X)
    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_XX = sum(x**2 for x in X)
    sum_YY = sum(y**2 for y in Y)
    sum_XY = sum(x*y for x, y in zip(X, Y))
    numerator = n*sum_XY - sum_X*sum_Y
    denominator = (n*sum_XX - sum_X**2) * (n*sum_YY - sum_Y**2)
    return numerator / denominator**0.5
