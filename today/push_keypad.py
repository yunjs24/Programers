


def solution(numbers, hand):
	answer = ''
	curL = 10
	curR = 12
	
	for i, n in enumerate(numbers):
		if n in [1,4,7]:
			answer += 'L'
			curL = n
		elif n in [3,6,9]:
			answer += 'R'
			curR = n
		else:
			if n == 0:
				n = 11

			absL = abs(n - curL)
			absR = abs(n - curR)
		
			if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
				answer += 'R'
				curR = n
			elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
				answer +='L'
				curL = n
			else:
				if hand == 'left':
					answer += 'L'
					curL = n
				else:
					answer += 'R'
					curR = n

	print(numbers, hand)
	return answer

cases = [
			[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"],
			[[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],
			[[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]
		]

for i, case in enumerate(cases):
	print(solution(case[0], case[1]))
