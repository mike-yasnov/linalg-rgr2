import re
import numpy as np 


def prepare_equation(expression: str, matrices: np.array, vectors: np.array) -> (np.array, np.array):
    equation = re.split(r'[\+\=]', expression)

    variables = {}
    variables.update(matrices)
    variables.update(vectors)
    # Подготовка матрицы коэффициентов и вектора свободных членов
    try:
        # Строим матрицу коэффициентов и вектор свободных членов
        A = None
        b = None
        for part in equation:
            tmp = None
            if "x" not in part:
                for char in part:
                    tmp = variables[char] if tmp is None else np.dot(tmp, variables[char])
                b = tmp if b is None else np.add(b, tmp)
            else:
                for char in part:
                    if char != "x":
                        A = variables[char] if A is None else np.dot(A, variables[char])
        
        if A is None or b is None:
            return "некорректный ввод"
        else:
            return (A, b)
    except Exception as e:
        return f"некорректный ввод: {e}"