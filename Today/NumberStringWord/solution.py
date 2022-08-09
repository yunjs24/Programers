
def solution(s):
    for i in range(10): 
        s = s.replace(["zero","one","two","three","four","five","six","seven","eight","nine"][i], str(i))
    return int(s)

print(solution("one4seveneight"))