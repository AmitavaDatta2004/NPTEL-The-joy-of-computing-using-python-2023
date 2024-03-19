def two_level_sort(scores):
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j][1] > scores[j+1][1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]

    for i in range(1, len(scores)):
        key = scores[i]
        j = i-1
        while j >= 0 and key[1] == scores[j][1] and key[0] < scores[j][0]:
            scores[j+1] = scores[j]
            j -= 1
        scores[j+1] = key

    return scores
