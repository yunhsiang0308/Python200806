file=open('oppa.jpg','rb')
img=file.read()
file.close()

file=open('bts.jpg','wb')
file.write(img)
file.close()