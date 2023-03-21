import numpy as np
import pandas as pd

def adjacent_lessons(zeros): #list of tuples (characteristic_zeros)
    sorted_unique_lessons = sorted(list(set([lesson for x in zeros for lesson in x])))
    lessons_amount = len(sorted_unique_lessons)
    np_zeros_matrix = np.zeros(shape=(lessons_amount, lessons_amount))
    adjacency_matrix_df = pd.DataFrame(np_zeros_matrix, index = sorted_unique_lessons, columns = sorted_unique_lessons)
    adjacency_matrix_df = fill_in(adjacency_matrix_df, zeros)
    return adjacency_matrix_df

def fill_in(adjacency_matrix_df, zeros):
    for el in zeros:
        adjacency_matrix_df.loc[el[0], el[1]] = 1
        adjacency_matrix_df.loc[el[1], el[0]] = 1  
        adjacency_matrix_df.loc[el[1], el[2]] = 1
        adjacency_matrix_df.loc[el[2], el[1]] = 1
    return adjacency_matrix_df
