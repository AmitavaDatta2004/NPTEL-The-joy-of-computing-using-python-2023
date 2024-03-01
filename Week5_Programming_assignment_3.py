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
    x=1
    y=1
    
    for move in range(len(moves)):
        if moves[move]=="N" and y<n:
            y=y+1
        elif moves[move]=="E" and x<n:
            x=x+1
        elif moves[move]=="W" and x>1:
            x=x-1
        elif moves[move]=="S" and y>1:
            y=y-1
    return (x,y)
