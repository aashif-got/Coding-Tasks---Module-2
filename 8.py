#Matrix multiplication 
def input_matrix(name):
    row  = int(input(f"Enter the number of rows for {name}:"))
    column = int(input(f"Enter the number of column for {name}: "))
    print ("Enter the elements of {name} row-waise:")

    matrix = []
    for i in range(row):
        row = []
        for j in range(column):
            x = int(input(f"Enter element ({i+1}, {j+1}): "))
            row.append(x)
        matrix.append(row)
    
    return matrix, row, column
def matrix_multiplication(a,b):
    r1,c1 = len(a), len(a[0])
    r2,c2 = len(b), len(a[0])
    if c1 != r2:
        print("Matrix multiplication not possible! Columns of A must equal rows of B.")
        return None
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]
    return result
A, r1, c1 = input_matrix("Matrix A")
B, r2, c2 = input_matrix("Matrix B")

print("\nMatrix A:", A)
print("Matrix B:", B)

res = matrix_multiplication(A, B)
if res:
    print("\nResult (A × B):")
    for row in res:
        print(row)
    



