import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


strr=input()

real=strr.split('.')[0]
sosu=strr.split('.')[1]

print(real)
print(sosu)
