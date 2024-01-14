import re

def read_matrix(input_lines: list, expected_shape: list) -> list:
    n, m = expected_shape
    result = []
    for _ in range(m):
        result.append([complex(num) for num in input_lines.pop(0).split()])
    return result

def read_vector(input_lines: list) -> list:
    return [complex(num) for num in input_lines.pop(0).strip().split()]

def parse_input(input_lines: list) -> (str, dict, dict):
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
            input_lines.pop(0)  # Previously used to get the dimension of the vector
            vectors[vector_name] = read_vector(input_lines)
            
    return (expression, matrices, vectors)