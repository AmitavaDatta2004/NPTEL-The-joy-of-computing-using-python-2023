def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        result_row = [elem * scalar for elem in row]
        result.append(result_row)
    return result

def parse_input():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    scalar = int(input())
    return matrix, scalar

def print_matrix(matrix):
    for row in matrix:
        print(*row)

def main():
    matrix, scalar = parse_input()
    scaled_matrix = scalar_multiply(matrix, scalar)
    print_matrix(scaled_matrix)

if __name__ == "__main__":
    main()

    
