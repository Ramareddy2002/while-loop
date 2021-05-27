'''while loop program'''

i=int(input('starting value'))
n=int(input('ending value'))
b=int(input('step count value'))
while i<=n:
    print (i)
    i=i+b
print('after while loop the value i is  {}',format(i))
print('after the while loop the value of i is %d belongs to i'%(i))
print('after the while loop the value of i is %d' %(i))




'''
expected out put

starting value 0
ending value 20
step count value 3
0
3
6
9
12
15
18
after while loop the value i is  {} 21
after the while loop the value of i is 21 belongs to i
after the while loop the value of i is 21
'''
