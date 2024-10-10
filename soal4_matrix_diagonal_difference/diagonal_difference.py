# diagonal_difference.py

def diagonal_difference(matrix):
    n = len(matrix)
    primary_diagonal = 0
    secondary_diagonal = 0
    
    for i in range(n):
        primary_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][n - 1 - i]
    
    difference = primary_diagonal - secondary_diagonal
    return difference

if __name__ == "__main__":
    # Contoh penggunaan
    matrix = [
        [1, 2, 0],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = diagonal_difference(matrix)
    print("Matrix:")
    for row in matrix:
        print(row)
    print(f"Selisih diagonal: {result}")
