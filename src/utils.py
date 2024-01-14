import re

def dot_product(matrix, vector):
    return [sum(m * v for m, v in zip(matrix_row, vector)) for matrix_row in matrix]

def add_matrices(A, B):
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

def scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]

def prepare_side(side: str, variables: dict):
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
                if tmp is None:
                    tmp = variables[char]
                else:
                    tmp = dot_product(tmp, variables[char])
        if "x" in part:
            # Добавление в матрицу коэффициентов
            tmp = scalar_multiply(tmp, sign)
            A = tmp if A is None else add_matrices(A, tmp)
        else:
            # Добавление в вектор свободных членов
            tmp = [t * sign for t in tmp]
            b = tmp if b is None else [sum(x) for x in zip(b, tmp)]

    return (A, b)


def prepare_equation(expression: str, matrices: dict, vectors: dict):
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
                A = add_matrices(A, scalar_multiply(C, -1))
            if b is not None and d is not None:
                b = [bi - di for bi, di in zip(d, b)]
        else:
            b = [-bi for bi in b]

        if A is None or b is None:
            return "некорректный ввод"
        else:
            return (A, b)
    except Exception as e:
        return f"некорректный ввод: {e}"