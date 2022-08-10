from itertools import combinations
import math

n = 3000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False        

def solution(nums):
    answer = 0
    for case in combinations(nums,3):
        s = sum(case)
        if s in primes:
            answer += 1
    
    return answer