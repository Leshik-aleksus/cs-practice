names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names: list[str], scores: list[float]) -> str:
    index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[index]:
            index = i
    return names[index]

def average(scores: list[float]) -> float:
    return round(sum(scores)/len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    paired = [(i, names[i], scores[i]) for i in range(len(names))]
    paired.sort(key=lambda x:(-x[2],x[0]))
    return [name for _, name, _ in paired]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    return [names[i] for i in range(len(names)) if scores[i] > avg]