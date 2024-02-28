def final(n, moves):
    """
    Compute the final position
    
    Argument:
        n: int
        moves: string
    Return:
        (x, y): tuple
    """
    n=int(n)
    moves=str(moves)
    x_coordinate=1
    y_coordinate=1
    
    for move in range(len(moves)):
        if moves[move]=="N" and y_coordinate<n:
            y_coordinate=y_coordinate+1
        elif moves[move]=="E" and x_coordinate<n:
            x_coordinate=x_coordinate+1
        elif moves[move]=="W" and x_coordinate>1:
            x_coordinate=x_coordinate-1
        elif moves[move]=="S" and y_coordinate>1:
            y_coordinate=y_coordinate-1
    return (x_coordinate,y_coordinate)
