
def nextbab(bab, word):
   
    for b in bab:
        loc = word.find(b)
        if loc == 0:
            return b
    if loc == -1:
        return ''
        
    
def babable(word):
    bab = ['aya', 'ye', 'woo', 'ma']
    l = len(word)
    prev = ''
    b = ''
    
    while word:
        b = nextbab(bab, word)
        if b == prev or b == '':
            break
        else:
            word = word[len(b):l]
            prev = b        

    if word == '':
        return True
    return False

def solution(babbling):
    answer = 0
    if len(babbling) > 10:
        return 0
    for r in babbling:
        if len(r) > 30:
            return 0
    
    for word in babbling:
        if babable(word):
            answer += 1
        
    return answer


Test = [(["aya", "yee", "u", "maa", 1])]

for i, T in enumerate(Test):
    if solution(T[0]) == T[1]:
        print(f'Test {i+1} : pass')
    else :
        print(f'Test {i+1} : fail')
    
    
