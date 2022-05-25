def base_ntok(n, k):  
	ret = ""
	while n > 0:
		ret += str(n % k)
		n = n //  k
	return ''.join(reversed(ret))
 
 
def is_prime(k):
	if k == 2 or k == 3:
		return 1
	if k % 2 == 0 or k < 2:
		return 0
	for i in range(3, int(k ** 0.5) + 1, 2):
		if k % i == 0:
			return 0
	return 1

 
def solution(n, k):
	answer = 0
	k_num = base_ntok(n, k)
	for n in k_num.split('0'):
		if n == "": continue
		if is_prime(int(n)):
			answer += 1
	return answer
