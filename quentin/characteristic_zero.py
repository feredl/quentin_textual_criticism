import input_processing as inp
from itertools import combinations, permutations
import numpy as np

variants_df = inp.getVariantData()
print(variants_df)
C = variants_df.shape[0]
#print("C")
lessons = list(variants_df.index.values)
lessons_triplets = list(combinations(lessons, 3))

print("TRIPLETS OF LESSONS TO BE CHECKED FOR HAVING AN INTERMEDIATE: ", list(combinations(lessons, 3)))

def trimmed_permutations(triplet_permutation): #type of triplet_permutation is a list of tuples
    return triplet_permutation[0:3]

def triplets_permutations(lessons_triplets): #TODO trim intermediats 
    triplets = []
    for i in lessons_triplets:
        p = trimmed_permutations(list(permutations(i)))
        for j in p:
            triplets.append(j) 
    return triplets 


possible_intermediates = triplets_permutations(lessons_triplets)
print(possible_intermediates)

def common_variants(triplets, variants_df):
    print(len(variants_df.columns))
    

common_variants(possible_intermediates, variants_df)




