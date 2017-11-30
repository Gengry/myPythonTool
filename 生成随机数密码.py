import random


n = input('生成密码长度：')

q = input('需要英文字母输入y：')
w = input('需要数字输入y：')
e = input('需要标点符号输入y：')
list = []
if q == 'y':
    list.append(1)
if w == 'y':
    list.append(2)
if e == 'y':
    list.append(3)
if type(n) is type(10):
    n = int(n)
else :
    n = 16

if len(list)==0:
    list.append(1)

while n > 0:
    seed = random.choice(list)
    if seed == 1:
        print(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'),end='')
        n -= 1
    elif seed == 2:
        print(random.choice((0,1,2,3,4,5,6,7,8,9)),end='')
        n -= 1
    elif seed == 3:
        print(random.choice('!@#$%^&*()_+;'),end='')
        n -= 1
print()