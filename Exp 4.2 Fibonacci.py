a = 1
b = 2
c = a + b
limit = 4000000
even_sum = 2
while(c <= limit):
	if c % 2 == 0:
		even_sum += c
	a = b
	b = c
	c = a + b
print(even_sum)

#output:
#4613732
