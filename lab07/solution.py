import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if not values or len(values) % width != 0:
        return []
    
    array = np.asarray(values).reshape(-1, width)
    return array.tolist()


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:

    if not matrix:
        return []
    
    array = np.asarray(matrix)
    subarray = array[np.ix_(rows, columns)]
    return subarray.tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    
    array = np.asarray(matrix)
    means = array.mean(axis=0)
    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    
    array = np.asarray(matrix)
    col = array[:, column]
    range_val = col.max() - col.min()
    return round(float(range_val), 6)
