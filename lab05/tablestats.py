def read_rows(lines: list[str]) -> list[dict]:
    header = None
    data_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if header is None:к
            header = [col.strip() for col in line.split(',')]
        else:
            data_lines.append(line)

    if header is None:
        return []

    rows = []
    for line in data_lines:
        fields = [field.strip() for field in line.split(',')]

        if len(fields) != len(header):
            continue

        row = {}
        for i in range(len(header)):
            row[header[i]] = fields[i]

        rows.append(row)

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}

    for row in rows:
        event_type = row.get('тип', '')
        if event_type:
            counts[event_type] = counts.get(event_type, 0) + 1

    return counts
