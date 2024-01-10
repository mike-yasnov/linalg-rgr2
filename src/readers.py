import numpy as np
import re

def read_matrix(input_lines, expected_shape):
    n, m = expected_shape
    result = []
    for _ in range(m):
        result.append(list(map(complex, input_lines.pop(0).split())))
    return np.array(result, dtype=complex).reshape((m, n))

def read_vector(input_lines, dimension):
    vector = list(map(complex, input_lines.pop(0).strip().split()))
    return np.array(vector, dtype=complex).reshape(-1, 1)

def parse_input(input_lines):
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
            vectors[vector_name] = read_vector(input_lines, (1, dim))
            
    return expression, matrices, vectors

def read_matrix_and_vector(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    expression = lines[0].strip()
    matrices = {}
    vectors = {}

    i = 1
    while i < len(lines):
        line = lines[i].strip()
        if line.isupper():  # Matrix
            dimensions = lines[i+1].strip().split()
            rows = int(dimensions[0])
            cols = int(dimensions[1]) if len(dimensions) > 1 else rows
            matrix = np.array([list(map(complex, lines[i+j+2].strip().split())) for j in range(rows)])
            matrices[line] = matrix
            i += rows + 2
        elif line.islower():  # Vector
            size = int(lines[i+1].strip())
            vector = np.array(list(map(complex, lines[i+2].strip().split())))
            vectors[line] = vector
            i += 3

    return expression, matrices, vectors
