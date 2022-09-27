from curses.ascii import islower
def solution(s):
    answer = ''
    s = s.split(' ')
    # print(s)

    for i, word in enumerate(s):
        # if islower(str(word[0])):
        s[i] = word.lower()
        s[i] = word.capitalize()
    return ' '.join(s)
