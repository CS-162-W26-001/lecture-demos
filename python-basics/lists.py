def create_multiplication_table(rows: int, columns: int) -> list[list[int]]:
    table: list[list[int]] = []

    for i in range(1, rows + 1):
        row: list[int] = []
        for j in range(1, columns + 1):
            row.append(i * j)
        table.append(row)

    print_table(table)

def print_table(table: list[list[int]]) -> None:
    for row in table:
        for column_index in range(len(row)):
            if column_index <  len(row) - 1:
                print(row[column_index], end = ',')
            else:
                print(row[column_index])

def number_range() -> None:
    number: list[int] = []
    for i in range(1, 11):
        number.append(i)

    print("len(number) = ", len(number))
    print(number)

    # for element in number:
    for i in range(len(number)):
        print(number[i])

def main() -> None:
    #number_range()
    create_multiplication_table(4, 5)


if __name__ == "__main__":
    main()
