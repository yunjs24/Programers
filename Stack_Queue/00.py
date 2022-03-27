#기능개발.py
def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        progresses = [x+y for x,y in zip(progresses, speeds)]
        print(f'prog: {progresses}')
            
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt != 0:
            answer.append(cnt)
    return answer