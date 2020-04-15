import C_arith
import time

#Driver
ip =[
	['b', 'a', 'bc'],
	['odd', 'odd', 'even'],
	['base', 'ball', 'games'],
	['send', 'more', 'money']
]
	
for i in ip:
	print('problem:', i)	
	a = time.time()
	v = C_arith.solve(i)
	if v:
		print(f'{len(v)} solution(s) possible')
		for s in v:
			print(s)
	else:
		print('No solution possible')
	print('time taken (sec)', round(time.time()-a, 2))
	print('')
