import input_processing as inp
import characteristic_zero
import adjacency_matrix
import reduced_matrix
import visualization
import output
from itertools import combinations, permutations

variants_df = inp.getVariantData()
print(variants_df)
lessons = list(variants_df.index.values)
lessons_triplets = list(combinations(lessons, 3))

possible_intermediates = characteristic_zero.triplets_permutations(lessons_triplets)
print("TRIPLETS OF LESSONS TO BE CHECKED FOR HAVING AN INTERMEDIATE: ")
output.triplets(possible_intermediates)

zeros = characteristic_zero.find(possible_intermediates, variants_df)
print("CHARACTERISTIC ZEROS:")
output.triplets(zeros)

adj_m = adjacency_matrix.adjacent_lessons(zeros)
print("ADJACENCY MATRIX:", "\n", adj_m)

red_m = reduced_matrix.reduction(adj_m, zeros)
print("REDUCED MATRIX:", "\n", red_m)

visualization.draw_graph(red_m)



