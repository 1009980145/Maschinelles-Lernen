#A2
fo = open("123.txt", "r")
a=list(fo)
words = []
word2=[]
new=[]
for word in a:
     words +=word    
for i in words:
     if ord(i) >=65 and ord(i)<=77:
         b=ord(i)-64+90-13
     elif ord(i) >77 and ord(i)<=90:
         b=ord(i)-13
     elif ord(i) >=97 and ord(i)<=109:
         b=ord(i)-64+90-13
     elif ord(i) >109 and ord(i)<=122:
         b=ord(i)-13
     else:
         b=ord('')
     word2.append(b)
for j in range(len(word2)):
    new.append((chr(word2[j])))
dststr = ''.join(new)
print(dststr)
