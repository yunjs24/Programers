def getSum(numbers, ops, length):
    ans = 0
    print(length)
    for i in range(0, length):
        print("ops : ", ops[i])
        print("nbr : ", numbers[i])
        if ops[i] == '+':
            ans += numbers[i]
        else:
            ans -= numbers[i]
    return ans

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    
    ops = ['-','+','+','-', '+']
    print(getSum(numbers,ops,length))
#     for i in range(0, 2 ** length):
#         while true:
#             if len(ops) == length and getSum(numbers, ops, length) == target:
#                 answer += 1
            
    
    # print(2 ** length)
    return answer