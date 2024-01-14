def solve_gaussian(A: list, b: list, doPricing: bool = True) -> list:
    n = len(A)
    if len(b) != n:
        raise ValueError("Неверный ввод. A & b.", len(b), n)

    for k in range(n - 1):
        if doPricing:
            maxindex = k + max(range(k, n), key=lambda x: abs(A[x][k]))
            if A[maxindex][k] == 0:
                raise ValueError("Матрица является единственной.")
            if maxindex != k:
                A[k], A[maxindex] = A[maxindex], A[k]
                b[k], b[maxindex] = b[maxindex], b[k]
        else:
            if A[k][k] == 0:
                raise ValueError("Поворотный элемент равен нулю. Попробуйте установить для doPricing значение True.")

        for row in range(k + 1, n):
            multiplier = A[row][k] / A[k][k]
            A[row][k:] = [ar - multiplier * ak for ar, ak in zip(A[row][k:], A[k][k:])]
            b[row] = b[row] - multiplier * b[k]

    x = [0] * n
    for k in range(n - 1, -1, -1):
        x[k] = (b[k] - sum(A[k][j] * x[j] for j in range(k + 1, n))) / A[k][k]

    return x
