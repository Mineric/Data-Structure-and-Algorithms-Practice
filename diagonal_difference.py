import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    exc_num, req_num = repeated_el(s)
    print(exc_num, req_num)
    result = 0

    for i in range(len(exc_num)):
        result += abs(exc_num[i] - req_num[i])

    return result



def repeated_el(arr):
    result = []
    repeated_num = []
    required_num = []
    
    for arrays in arr:
        for elements in arrays:
            result.append(elements)

    for i in result: 
        if result.count(i) > 1:    
            repeated_num.append(i)

    for i in list(dict.fromkeys(repeated_num)):
        repeated_num.remove(i)

    for i in range(1,10):
        if i not in result:
            required_num.append(i)
        

    [exc_num, req_num] = [sorted(repeated_num), required_num]

    return [exc_num, req_num]
    



s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)

  


