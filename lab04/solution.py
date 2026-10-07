names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names: list[str], scores: list[float]) -> str:
    index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[index]:
            index = i
    return names[index]