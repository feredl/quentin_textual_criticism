import input_processing as inp
import itertools
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

def triplets_permutations(lessons_triplets): 
    triplets = []
    for i in lessons_triplets:
        p = trimmed_permutations(list(permutations(i)))
        for j in p:
            triplets.append(j) 
    return triplets 


possible_intermediates = triplets_permutations(lessons_triplets)
print("TRIPLETS OF LESSONS TO BE CHECKED FOR HAVING AN INTERMEDIATE: ", possible_intermediates)

def to_dictionary(variants_df):
    return variants_df.to_dict('index')

def if_possible_zero(lesson1, lesson2, possible_zero): #dicts 
    counter = 0
    l1 = list(lesson1.values())
    l2 = list(lesson2.values())
    pz = list(possible_zero.values())
    print(l1, "\n", l2, "\n", pz, "\n" )
    for (el1, el2, el3_pz) in zip(l1, l2, pz):
        if (el1 == el2 & el1 != el3_pz):
            counter = counter + 1
    if (counter > 0):
        return False 
    else:
        return True

def same_variant_position(lesson1, lesson2):
    counter = 0
    l1 = list(lesson1.values())
    l2 = list(lesson2.values())
    for (el1, el2) in zip(l1, l2):
        if(el1 == el2):
            counter = counter + 1
    if (counter > 0):
        return True
    else:
        return False 


def common_variants(triplets, variants_df):
    variants_amount = len(variants_df.columns) 
    print(variants_amount)
    zeros = []
    variants_dict = variants_df.to_dict('index')
    for el in triplets:
        lesson1 = str(el[0])
        lesson2 = str(el[2])
        possible_zero = str(el[1])
        l1 = variants_dict.get(lesson1)
        l2 = variants_dict.get(lesson2)
        p_z = variants_dict.get(possible_zero)
        print(el)
        if (same_variant_position(l1, l2) == True & if_possible_zero(l1, l2, p_z) == True):
                zeros.append(el)
    return zeros

print("CHARACTERISTIC ZEROS:", common_variants(possible_intermediates, variants_df))



