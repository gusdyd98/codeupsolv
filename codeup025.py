import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a=input()

b=len(a)

for i in range(0,b):
    c=int(a[i])*10**(b-i-1)
    #print('a=%s, b=%d, i=%d, [%d]' % (a,b,i,c))
    print('[%d]' % c)
    if i==b:
        exit()
