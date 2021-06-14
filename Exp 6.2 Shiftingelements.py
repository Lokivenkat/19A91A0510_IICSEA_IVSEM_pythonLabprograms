list1 = [int(i) for i in input().split()]
rotations = int(input('Enter the number of Rotations:'))
list1 = (list1[-rotations:] + list1[:-rotations])
print(list1)

#output:
#10 20 30 40 50
#Enter the number of Rotations:1
#[50, 10, 20, 30, 40]
