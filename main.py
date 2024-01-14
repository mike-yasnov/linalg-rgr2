import numpy as np 
from src.readers import parse_input
from src.utils import prepare_equation
from src.solvers import solve, solve_gaussian


def main(file_name: str) -> str:
    with open(file_name, 'r') as file:
        input_lines = file.read().splitlines() + [0]

    expression, matrices, vectors = parse_input(input_lines)
    A, b = prepare_equation(expression, matrices, vectors)
    # Решение СЛАУ
    flag = int(input("Введите способ решения СЛАУ: \n1. Обычный\n2.Гаусс\nВаш вариант ответа: "))
    if flag == 1:
        x = solve(A, b)
    else:
        b = b.reshape(-1)
        x = solve_gaussian(np.copy(A), np.copy(b), doPricing = True)
    if isinstance(x, str):
        return x
    else:
        return '\n'.join(f'x{i+1} = {elem}' for i, elem in enumerate(x))


if __name__ == "__main__":
    file_name = input("Введите путь к файлу: ")
    print(main(file_name))