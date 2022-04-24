import numpy as np


def generate_lof_data(save: bool = True, path: str = './'):

    centers = [((50, 60, 50), 50),
               ((80, 20, 30), 200),
               ((30, 60, 30), 20),
               ((50, 100, 70), 10)]

    distance = 20
    data = None

    for center in centers:
        ax = np.zeros((center[1], len(center[0])))
        for key, axis in enumerate(center[0]):
            rand = np.random.uniform(axis, axis + distance, size=(center[1],))
            ax[:, key] = rand
        data = ax if data is None else np.concatenate((data, ax), axis=0)

    if save:
        np.savetxt(path, data)

    return data