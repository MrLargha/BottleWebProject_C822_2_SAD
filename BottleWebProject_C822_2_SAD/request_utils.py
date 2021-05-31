from bottle import request
import numpy as np


def extract_matrix_from_request_params(params):
    keys = list(filter(lambda x: "matrix_cell" in x, params.keys()))
    print(keys)