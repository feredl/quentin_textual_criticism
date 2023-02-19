import input_processing as inp
from itertools import combinations
import numpy as np

variants_df = inp.getVariantData()
C = variants_df.shape[0]
lessons = list(variants_df.index.values)
lessons_triplets = list(combinations(lessons, 3))

#print("TRIPLETS OF LESSONS TO BE CHECKED FOR HAVING AN INTERMEDIATE: ", list(combinations(lessons, 3)))
