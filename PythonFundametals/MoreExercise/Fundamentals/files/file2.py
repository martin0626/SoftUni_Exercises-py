f = open('28044.jpg', 'rb')

f1 = open('MyPic.JPG', 'wb')

for i in f:
    f1.write(i)