threshold = float(input())
n = int(input())

total = n
errors = 0
over = 0

sum_temp = 0.0
count_valid = 0
max_temp = None

for _ in range(n):
    record = input()
    if record == "error":
        errors += 1
    else:
        temp = float(record)
        sum_temp += temp
        count_valid += 1
        if max_temp is None or temp > max_temp:
            max_temp = temp
        if temp > threshold:
            over += 1
