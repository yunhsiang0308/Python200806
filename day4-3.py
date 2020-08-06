import os.path
d={}
def buildMenu():
    print('歡迎進入系統')
    print('###################')
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢系統')
    print('4.離開系統')
    
if os.path.isfile('scores.txt'):
    fo=open('scores.txt','r')
    print('old file')
else:
    fo=open('scores.txt','w')
    print('new file')
while True:
    buildMenu()
    x=int(input('請輸入選項:'))
    if x==1:
        while True:
            a=input('請輸入名字(按0退出):')
            if a=='0':
                break
            if a not in d:
                b=input('請輸你的成績:')
                d[a]=b
            
    if x==2:
        print(d)  
    if x==3:
         while True:
            a=input('請輸你的名字(按0退出):')
            if a=='0':
                break
            print(a,'的成績是',d[a])              
    if x==4:
        break

fo=open('scores.txt','w')
for k,v in d.items():
    fo.write(k)
    fo.write(':')
    fo.write(v)
    fo.write('\n')
fo.close()
 
#for row in fo.readline():
#    k=data[0]
#    v=data[1]
#    d[k]=v
    
#print(d)


    
