from itertools import permutations, chain
def solution(babbling):
    answer = 0
    if len(babbling) > 10:
        return 0
    for r in babbling:
        if len(r) > 100:
            return 0
    bab = ['aya', 'ye', 'woo', 'ma']
    words = list()
    for i in range(1,5):
        w = []
        for i, case in enumerate(permutations(bab, i)):
            w.append('')
            for b in case:
                w[i] += b
        words.append(w)
    words = list(chain(*words))
    for i in range(0, len(babbling)):
        if babbling[i] in words:
            answer+=1

    return answer
