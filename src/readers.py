import numpy as np
import re


def read_matrix(
        input_lines: list, 
        expected_shape: list
        ) -> np.array:
    n, m = expected_shape
    result = []
    for _ in range(m):
        result.append(list(map(complex, input_lines.pop(0).split())))
    return np.array(result, dtype=complex).reshape((m, n))


def read_vector(
        input_lines: list
        ) -> np.array:
    vector = list(map(complex, input_lines.pop(0).strip().split()))
    return np.array(vector, dtype=complex).reshape(-1, 1)


def parse_input(
        input_lines: list
        ) -> (np.array, np.array, np.array):
    expression = input_lines.pop(0)
    matrices = {}
    vectors = {}

    # Ищем заглавные буквы для матриц
    for matrix_name in re.findall(r'[A-Z]', expression):
        if matrix_name not in matrices.keys():
            dims = list(map(int, input_lines.pop(0).split()))
            if len(dims) == 1:
                dims = [dims[0], dims[0]]
            matrices[matrix_name] = read_matrix(input_lines, dims)            

    # Ищем строчные буквы для векторов
    for vector_name in re.findall(r'[a-wyz]', expression):
        if vector_name not in vectors.keys():
            dim = int(input_lines.pop(0))
            vectors[vector_name] = read_vector(input_lines)
            
    return (expression, matrices, vectors)

