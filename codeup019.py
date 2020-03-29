import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a=input()

hh=int(a.split('.')[0])
mm=int(a.split('.')[1])
ss=int(a.split('.')[2])

print('%04d.%02d.%02d' % (hh,mm,ss))