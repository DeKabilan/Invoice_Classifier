from text_extraction import *

def cosinesim(array1 , array2):

#--------------Intitializing Hashmap---------------
    hash1 = {}
    hash2 = {}

#-------------Taking Word Count of Array_1-------------
    for word in array1:
        words = word.lower()
        if words in hash1:
            hash1[words] +=1
        else:
            hash1[words] = 1

#-------------Taking Word Count of Array_2-------------
    for word in array2:
        words = word.lower()
        if words in hash2:
            hash2[words] +=1
        else:
            hash2[words] = 1

#-------------Calculating the Numerator in Cosine_Similarity--------
    numerator= 0
    for key in hash1:
        if key in hash2:
            numerator=hash1[key]*hash2[key]+numerator

#-------------Calculating the First part of the Denominator------------
    part1=0
    for key in hash1:
        part1=hash1[key]**2+part1
    part1=part1**0.5

#-------------Calculating the Second part of the Denominator----------------
    part2 = 0
    for key in hash2:
        part2=hash2[key]**2+part2
    part2=part2**0.5

#-------------Calculating Denominator------------------------------
    denominator = part1*part2

#------------Return the Cosine similarity--------------
    return numerator/denominator



