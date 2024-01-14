import re
import numpy as np

def prepare_side(side: str, variables: dict) -> (np.array, np.array):
    equation_parts = re.split(r"(\+|\-)", side)

    A = None
    b = None    
    sign = 1

    for part in equation_parts:
        if part in '+-':  # Переключение знака
            sign = -1 if part == '-' else 1
            continue
                
        # Подготовка временной переменной для частей выражения
        tmp = None
        for char in part:
            if char != "x":
                tmp = variables[char] if tmp is None else np.dot(tmp, variables[char])
        if "x" in part:
            # Добавление в матрицу коэффициентов
            A = sign * tmp if A is None else A + sign * tmp
        else:
            # Добавление в вектор свободных членов
            b = tmp if b is None else b + sign * tmp

    return (A, b)


def prepare_equation(
        expression: str, 
        matrices: dict, 
        vectors: dict
        ) -> (np.array, np.array):
    
    # Разделение на левую и правую часть относительно знака "="
    left_side, right_side = expression.split('=')

    # Обновление словарей переменных
    variables = {}
    variables.update(matrices)
    variables.update(vectors)

    # Подготовка матрицы коэффициентов и вектора свободных членов
    try:
        A, b = prepare_side(left_side, variables)

        # Обработка правой части уравнения
        if right_side != "0":
            C, d = prepare_side(right_side, variables)
            if C is not None:
                A = np.add(A, -1 * C)
            if b is not None:
                b = np.add(d, -1 * b)
        else:
            b *= -1

        if A is None or b is None:
            return "некорректный ввод"
        else:
            return (A, b)
    except Exception as e:
        return f"некорректный ввод: {e}"
