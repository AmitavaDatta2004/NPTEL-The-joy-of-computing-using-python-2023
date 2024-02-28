def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def parse_input():
    n = int(input())
    A = [list(map(int, input().split(','))) for _ in range(n)]
    B = [list(map(int, input().split(','))) for _ in range(n)]
    return A, B

def main():
    A, B = parse_input()
    result = matrix_multiply(A, B)
    for row in result:
        print(','.join(map(str, row)) )

if __name__ == "__main__":
    main()
