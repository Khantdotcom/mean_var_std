import numpy as np
def calculate(input):
    if len(input) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        data = np.array(input, dtype=float).reshape(3, 3)
    return {
            'mean': [list(np.mean(data, axis=0)), list(np.mean(data,axis=1)), np.mean(data)],
            'variance': [list(np.var(data, axis=0)), list(np.var(data,axis=1)), np.var(data)],
            'standard deviation': [list(np.std(data, axis=0)), list(np.std(data,axis=1)), np.std(data)],
            'max': [list(np.max(data, axis=0)), list(np.max(data,axis=1)), np.max(data)],
            'min': [list(np.min(data, axis=0)), list(np.min(data,axis=1)), np.min(data)],
            'sum': [list(np.sum(data, axis=0)), list(np.sum(data,axis=1)), np.sum(data)]
        }
