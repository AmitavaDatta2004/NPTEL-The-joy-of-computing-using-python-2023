def distance(word_1, word_2):   
    """
    calculate the distance between two words
    Argument:
        word1: str
        word2: str
    Return:
        dist: int
    """
    alphabets=("abcdefghijklmnopqrstuvwxyz")
    word_1=str(word_1)
    word_2=str(word_2)
    if len(word_1)==len(word_2):
        distance=0
        for i in range(0,len(word_1) or len(word_2)):
            diff=alphabets.index(word_1[i])-alphabets.index(word_2[i])
            if diff<0:
                diff = (-diff)
            distance=distance+diff
        return distance
    else:
        return -1
