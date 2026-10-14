from tablestats import read_rows, count_types, total_minutes, to_csv


def main():
    filename = input().strip()

    with open(filename, encoding='utf-8') as table:
        lines = table.readlines()

    rows = read_rows(lines)

    total_records = len(rows)
    counts = count_types(rows)
    unique_types = len(counts)
    error_minutes = total_minutes(rows, 'ошибка')

    print(total_records)
    print(unique_types)
    print(error_minutes)

    with open('summary.csv', 'w', encoding='utf-8') as out:
        out.write(to_csv(counts))


if __name__ == '__main__':
    main()
