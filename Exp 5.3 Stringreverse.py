string = input('Enter a String:')
res = len(string.split(' '))
lst = string.split(' ')
new_lst = [i[::-1] for i in lst]
new_string = ' '.join(new_lst)
print(res,end = ' ')
print(new_string)

#output:
#Enter a String:Honesty is the best policy
#5 ytsenoH si eht tseb ycilop
