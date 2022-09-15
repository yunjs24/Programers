from itertools import combinations

def solution(nums): return min([len(set(nums)) , len(nums) / 2])

solution([3,3,3,2,2,4])