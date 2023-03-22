import input_processing as inp
import characteristic_zero as ch_zero
import adjacency_matrix
import reduced_matrix
import itertools
from itertools import combinations, permutations
import numpy as np

variants_df = inp.getVariantData()
print(variants_df)
lessons = list(variants_df.index.values)
lessons_triplets = list(combinations(lessons, 3))

print("POSSIBLE LESSONS COMBINATIONS: ", lessons_triplets)

possible_intermediates = ch_zero.triplets_permutations(lessons_triplets)
print("TRIPLETS OF LESSONS TO BE CHECKED FOR HAVING AN INTERMEDIATE: ", possible_intermediates)

zeros = ch_zero.zeros_list(possible_intermediates, variants_df)
print("CHARACTERISTIC ZEROS:", zeros)

adj_m = adjacency_matrix.adjacent_lessons(zeros)
print("ADJACENCY MATRIX:", "\n", adj_m)

red_m = reduced_matrix.reduction(adj_m, zeros)
print("REDUCED MATRIX:", "\n", red_m)



