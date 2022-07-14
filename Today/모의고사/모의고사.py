answers = [1,2,3,4,5]

pattern=['12345','21232425','3311224455']

def solution(answers):
    answer = []
    n = len(answers)
    examinees = [0] * len(pattern)
    sizes = []
    for i in range(len(pattern)):
        sizes.append(len(pattern[i]))
    for i in range(n):
        for j in range(0,len(pattern)):
            if (answers[i] == int(pattern[j][i % sizes[j]])):
                examinees[j] += 1
    twistedFate = max(examinees)
    for i in range(len(pattern)):
        if (twistedFate == examinees[i]):
            answer.append(i + 1)
    return answer

solution(answers)