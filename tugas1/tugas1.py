batas = int(input('masukan batas angka: '))

for x in range(batas):
	print(x + 1, end = '')
	fizz = (x + 1) % 2 == 0
	buzz = (x + 1) % 3 == 0
	
	if fizz and buzz:
		print(' ->FIzzBuzz')
	elif fizz:
		print(' ->Fizz')
	elif buzz:
		print(' ->Buzz')
	else:
		print('')
