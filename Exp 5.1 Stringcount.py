input_str = input('Enter a string: ')

alphabet_count = {}

for character in input_str:
	alphabet_count[character] = alphabet_count.get(character,0) + 1


for key in sorted(alphabet_count.keys()):
	print('Count of {} is {}'.format(key,alphabet_count[key]))
	
#output:
#Enter a string: Loki venkat
#Count of   is 1
#Count of L is 1
#Count of a is 1
#Count of e is 1
#Count of i is 1
#Count of k is 2
#Count of n is 1
#Count of o is 1
#Count of t is 1
#Count of v is 1
