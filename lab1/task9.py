def count_columns_without_zeros(matrix: list[list[int]]) -> int:
    try:
        if not matrix or not matrix[0]:
            raise ValueError("Матрица не должна быть пустой!")

        rows = len(matrix)
        cols = len(matrix[0])

        for row in matrix:
            if len(row) != cols:
                raise ValueError("Матрица должна быть прямоугольной!")

        valid_columns_count = 0

        for j in range(cols):
            has_zero = False
            for i in range(rows):
                if matrix[i][j] == 0:
                    has_zero = True
                    break
            if not has_zero:
                valid_columns_count += 1

        return valid_columns_count

    except TypeError:
        print("Ошибка: элементы матрицы должны быть целыми числами.")
        return 0
    except Exception as e:
        print(f"Ошибка при обработке матрицы: {e}")
        return 0
    finally:
        print("Анализ матрицы завершен.")


if __name__ == "__main__":
    matrix_example = [
        [1, 0, 3, 4],
        [5, 2, 0, 8],
        [9, 6, 7, 2]
    ]

    print("Матрица:")
    for row in matrix_example:
        print(row)

    count = count_columns_without_zeros(matrix_example)
    print(f"Количество столбцов без нулей: {count}")