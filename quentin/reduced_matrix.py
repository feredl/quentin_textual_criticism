
def check_for_reduction(zeros):
    deuces = []
    new_el = []
    for el in zeros:
        deuces.append((el[0], el[1]))
        deuces.append((el[1], el[2]))
    deuces = list(set(deuces))
    return deuces

def reduction(adjacency_matrix_df, zeros):
    deuces = check_for_reduction(zeros)
    for el_d in deuces:
        for el_t in zeros:
            if(el_d[0] == el_t[0] and el_d[1] == el_t[2] or el_d[0] == el_t[2] and el_d[1] == el_t[0]):
                adjacency_matrix_df.loc[el_d[0], el_d[1]] = 0.0
                adjacency_matrix_df.loc[el_d[1], el_d[0]] = 0.0
    return adjacency_matrix_df
