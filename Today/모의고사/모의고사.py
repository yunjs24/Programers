answers = [1,2,3,4,5]

pattern=['12345','21232425','3311224455']

def solution(answers):
    answer = []
    n = len(answers)
    examinees = [0,0,0]
    sizes = [len(pattern[0]),len(pattern[1]),len(pattern[2])]
    for i in range(n):
        for j in range(0,3):
            if (answers[i] == int(pattern[j][i % sizes[j]])):
                examinees[j] += 1
    twistedFate = max(examinees)
    for i in range(3):
        if (twistedFate == examinees[i]):
            answer.append(i + 1)
    return answer

solution(answers)