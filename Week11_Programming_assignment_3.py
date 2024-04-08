def spiral_iterative(left, right, n):
    """
    An iterative function to compute the x-coordinate of the nth arm of the spiral
 
    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    for i in range(1,n):
      center = (left + right)/2
      if i % 2 :
        left = center
      else:
        right = center
    return center
    
    
def spiral_recursive(left, right, n):
    """
    An recursive function to compute the x-coordinate of the nth arm of the spiral
 
    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    if n == 2:
      return ( left + right )/2
    elif n % 2 == 0:
      return (spiral_recursive(( left + right )/2, right, n-1))
    elif n % 2 == 1:
      return (spiral_recursive(left, ( left + right )/2, n-1))
