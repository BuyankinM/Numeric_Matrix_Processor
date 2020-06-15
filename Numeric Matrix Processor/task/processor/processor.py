def read_matrix_from_input(num_str):
    matrix = []
    n, m = [int(d) for d in input(f"Enter size of {num_str} matrix: ").split()]

    print(f"Enter {num_str} matrix:")
    for _ in range(n):
        matrix.append([float(d) if "." in d else int(d) for d in input().split()])

    return matrix, n, m


def print_result(matrix):
    print("The result is:")
    for row in matrix:
        print(" ".join(str(round(d, 3)) for d in row))


def add_matrices():
    matrix1, n1, m1 = read_matrix_from_input("first")
    matrix2, n2, m2 = read_matrix_from_input("second")

    if n1 != n2 or m1 != m2:
        print("The operation cannot be performed.")
    else:
        res_matrix = []
        for i in range(n1):
            row = []
            for j in range(m1):
                row.append(matrix1[i][j] + matrix2[i][j])
            res_matrix.append(row)
        print_result(res_matrix)


def multiply_matrix_by_const():
    matrix, n, m = read_matrix_from_input("first")
    const = int(input(f"Enter constant: "))
    for i in range(n):
        for j in range(m):
            matrix[i][j] *= const
    print_result(matrix)


def multiply_matrices():
    matrix1, n1, m1 = read_matrix_from_input("first")
    matrix2, n2, m2 = read_matrix_from_input("second")

    if m1 != n2:
        print("The operation cannot be performed.")
    else:
        res_matrix = []
        for row in matrix1:
            new_row = []
            for j in range(m2):
                column = [matrix2[ii][j] for ii in range(n2)]
                new_row.append(sum(v1 * v2 for v1, v2 in zip(row, column)))
            res_matrix.append(new_row)
        print_result(res_matrix)


def transpose_matrices():
    print("""\
    1. Main diagonal\
    2. Side diagonal\
    3. Vertical line\
    4. Horizontal line""")

    choice_diag = input("Your choice: ")
    matrix, n, m = read_matrix_from_input("first")

    if choice_diag == "1":
        res_matrix = list(zip(*matrix))
    elif choice_diag == "2":
        res_matrix = list(reversed(list(zip(*reversed(matrix)))))
    elif choice_diag == "3":
        res_matrix = [list(reversed(row)) for row in matrix]
    else:
        res_matrix = list(reversed(matrix))

    print_result(res_matrix)


def calc_cofactor(matrix, i, j):
    new_rows = matrix[:i] + matrix[i+1:]
    new_matrix = [row[:j] + row[j+1:] for row in new_rows]
    return (-1) ** ((j + 1) + (i + 1)) * calc_det_recursive(new_matrix)


def calc_det_recursive(matrix):
    nm = len(matrix)
    if nm == 1:
        return matrix[0][0]
    elif nm == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        res = 0
        i = 0
        for j in range(nm):
            res += calc_cofactor(matrix, i, j) * matrix[i][j]
        return res


def calc_det():
    matrix, n, m = read_matrix_from_input("first")

    if n != m:
        print("The operation cannot be performed.")
    else:
        res = calc_det_recursive(matrix)
        print_result([[res]])


def inverse_matrix():
    matrix, n, m = read_matrix_from_input("first")

    if n != m:
        print("The operation cannot be performed.")
    else:
        detA = calc_det_recursive(matrix)
        if detA == 0:
            print("The operation cannot be performed.")
        else:
            matrix_co = []
            const = 1 / detA
            for i in range(n):
                row_co = []
                for j in range(m):
                    row_co.append(calc_cofactor(matrix, i, j) * const)
                matrix_co.append(row_co)

            res_matrix = list(zip(*matrix_co)) # transpose
            print_result(res_matrix)


while True:
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit""")

    choice = input("Your choice: ")
    if choice == "1":
        add_matrices()
    elif choice == "2":
        multiply_matrix_by_const()
    elif choice == "3":
        multiply_matrices()
    elif choice == "4":
        transpose_matrices()
    elif choice == "5":
        calc_det()
    elif choice == "6":
        inverse_matrix()
    else:
        break

    print()
