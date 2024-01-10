import numpy as np
from numpy.linalg import LinAlgError

def solve(
        A: np.array, 
        b: np.array
        ) -> np.array | str:
    try:
        return np.linalg.solve(A, b)
    except LinAlgError as e:
        if 'Singular matrix' in str(e):
            return "нет решений"
        else:
            return "бесконечное количество решений"
        

def solve_gaussian(
        A: np.array, 
        b: np.array, 
        doPricing: bool = True
        ) -> np.array | str:
    
    n = len(A)
    if b.size != n:
        raise ValueError("Неверный ввод. "+ "A & b.", b.size, n)
    
    for k in range(n-1):
        if doPricing:
            maxindex = abs(A[k:,k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Матрица является единственной.")
            if maxindex != k:
                A[[k,maxindex]] = A[[maxindex, k]]
                b[[k,maxindex]] = b[[maxindex, k]]
        else:
            if A[k, k] == 0:
                raise ValueError("Поворотный элемент равен нулю. Попробуйте установить для doPricing значение True.")
        for row in range(k+1, n):
           multiplier = A[row,k]/A[k,k]
           A[row, k:] = A[row, k:] - multiplier*A[k, k:]
           b[row] = b[row] - multiplier*b[k]
    x = np.zeros(n, dtype=complex)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    return x
