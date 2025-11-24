def multiply_matrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s

    return C

# приклад:
n = int(input("Введіть n: "))

print("Введіть матрицю A:")
A = [list(map(int, input().split())) for _ in range(n)]

print("Введіть матрицю B:")
B = [list(map(int, input().split())) for _ in range(n)]

print("Добуток матриць:")
C = multiply_matrices(A, B)
for row in C:
    print(row)
