import input_processing as inp
from itertools import combinations, permutations
import numpy as np

variants_df = inp.getVariantData()
print(variants_df)
C = variants_df.shape[0]
#print("C")
lessons = list(variants_df.index.values)
lessons_triplets = list(combinations(lessons, 3))

print("POSSIBLE LESSONS COMBINATIONS: ", list(combinations(lessons, 3)))

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
print("TRIPLETS OF LESSONS TO BE CHECKED FOR HAVING AN INTERMEDIATE: ", possible_intermediates)

def common_variants(triplets, variants_df):
    counter = 0
    variants_amount = len(variants_df.columns)
    print(variants_amount)
    for el in triplets:
        for i in range(0, 1, variants_amount):
            lesson1 = variants_df.loc[el[0]].iat[i]
            possible_zero = variants_df.loc[el[1]].iat[i]
            lesson2 = variants_df.loc[el[2]].iat[i]
            #print(lesson1, lesson2, possible_zero)
            if (lesson1 == lesson2 & lesson1 != possible_zero):
                triplets.remove(el)
    return triplets

print("CHARACTERISTIC ZEROS:", common_variants(possible_intermediates, variants_df))




