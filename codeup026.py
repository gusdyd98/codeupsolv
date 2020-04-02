import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a=input()

h=int(a.split(':')[0])
m=int(a.split(':')[1])
s=int(a.split(':')[2])

print('%d' % m)
