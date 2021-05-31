from bottle import request
import numpy as np


def extract_matrix_from_request_params(params):
    size = int(params.get("matrix_size"))
    keys = list(map(lambda x: int(x.replace("matrix_cell_", "")), filter(lambda x: "matrix_cell" in x, params.keys())))
    mat = np.zeros((size, size), dtype=bool)
    for key in keys:
        row = key // size
        cell = key % size
        mat[row][cell] = True
    mat = mat.T + mat
    return np.array(mat, dtype=int)
