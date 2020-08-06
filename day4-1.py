import os.path

if os.path.isfile('bts.txt'):
    print('file存在')
else:
    print('file不存在')

fo=open('bts.txt','w')
fo.write('We were only seven,')
fo=open('bts.txt','r')
fo.read()
fo=open('bts.txt','a')
fo.write('but we have you Army~')
print(fo)

fo.close()