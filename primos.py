primos = [2]

for i in range(2, 101):
	prime = True
	for j in primos:
		if i%j == 0: 
			prime = False
			break
	if prime:
		print("{} es un numero primo.".format(i) )
		primos.append(i)

print("Lista de numeros primos:\n", primos)
