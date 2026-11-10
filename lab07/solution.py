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

