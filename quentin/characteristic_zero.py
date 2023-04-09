import input_processing as inp
import itertools
from itertools import combinations, permutations
import numpy as np

def trimmed_permutations(triplet_permutation): 
    length = len(triplet_permutation)
    middle_index = length//2 
    return triplet_permutation[:middle_index]

def triplets_permutations(lessons_triplets): 
    triplets = []
    for i in lessons_triplets:
        p = trimmed_permutations(list(permutations(i)))
        for j in p:
            triplets.append(j) 
    return triplets 

def if_possible_zero(lesson1, lesson2, possible_zero, answer): #dicts 
    counter = 0
    l1 = list(lesson1.values())
    l2 = list(lesson2.values())
    pz = list(possible_zero.values())
    triplet_values = list(zip(l1, l2, pz))
    if (answer == "y"):
        for el in triplet_values:
            if (el[0] == el[1] and el[0] != el[2] and el[2] != 0 and el[1] != 0):
                return False
    if (answer == "n"):
        for el in triplet_values:
            if (el[0] == el[1] and el[0] != el[2]):
                return False
    return True
  

def same_variant_position(lesson1, lesson2):
    counter = 0
    l1 = list(lesson1.values())
    l2 = list(lesson2.values())
    var_tuple = list(zip(l1, l2))
    for el in var_tuple:
        if(el[0] == el[1]):
            counter = counter + 1
    if (counter > 0):
        return True
    else:
        return False 


def find(triplets, variants_df):
    answer = input("Should the program skip columns with zeros in it? y/n > ")
    variants_amount = len(variants_df.columns) 
    zeros = []
    variants_dict = variants_df.to_dict('index')
    for el in triplets:
        lesson1 = str(el[0])
        lesson2 = str(el[2])
        possible_zero = str(el[1])
        l1 = variants_dict.get(lesson1)
        l2 = variants_dict.get(lesson2)
        p_z = variants_dict.get(possible_zero)
        #print(el)
        #print(if_possible_zero(l1, l2, p_z))
        if (same_variant_position(l1, l2) == True and if_possible_zero(l1, l2, p_z, answer) == True):
                zeros.append(el)
                #print(zeros)
                #print(el)
                

    return zeros
