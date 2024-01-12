# Ргр №2 по линейной алгебре

<img src="https://img.shields.io/badge/GIT-black?style=for-the-badge&logo=GIT&logoColor=F05032"/>
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
<img src="https://img.shields.io/badge/numpy-black?style=for-the-badge&logo=numpy&logoColor=white"/>

# Введение
Выполнили:
- Яснов Михаил Р3117
- Вердиев Фада Р3117

Поток: ЛИН АЛГ ПИиКТ 15.3

# Особенности  
- Работает с комплексными числами 
- Работает со сложением 
- Реализовано решение СЛАУ методом Гаусса
- Читает матрицы из файла


## Запуск проекта

Клонируем репозиторий
```bash  
git clone git@github.com:mike-yasnov/linalg-rgr2.git
```

Переходим в репозиторий
```bash  
cd linalg-rgr2
```

Создаем виртуальное окужение & устанавливаем зависимости
```bash  
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Запустить
```bash  
python main.py
```
# Пример входных данных 
### !!! Комментарии при вводе нобходимо убрать (см пример в файле [input.txt](https://github.com/mike-yasnov/linalg-rgr2/blob/main/input.txt)) !!!
```
Ac+Bc+Dx \\ Само выражение
2 2 \\ Размерность матрицы A
1 2
3 4
2 2 \\ Размерность матрицы B
7 8
9 10
2 2 \\ Размерность матрицы D
13 14
15 16
2 \\ Вектор c
5 6
```

# Структура проекта

```
linalg-rgr2
│
├── main.py - Основной файл 
├── input.txt - Входные данные
│
└── src
    ├── readers.py - Чтение файла
    ├── solvers.py - Решение СЛАУ
    └── utils.py - Предобработка данных
```