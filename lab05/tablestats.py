def read_rows(lines: list[str]) -> list[dict]:
    header = None
    data_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if header is None:
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

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row.get('тип') == kind:
            minutes_str = row.get('минуты', '')

            try:)
                minutes_str = minutes_str.replace(',', '.')
                minutes = float(minutes_str)
                total += minutes
            except ValueError:
                continue

    return round(total, 1)


def to_csv(counts: dict) -> str:
    lines = ['тип,количество']

    for event_type in sorted(counts.keys()):
        lines.append(f"{event_type},{counts[event_type]}")

    return '\n'.join(lines) + '\n'
