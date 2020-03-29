import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


strr=input()

lenstrr=len(strr)

for i in range(0,lenstrr):
    print('\''+strr[i]+'\'')
    i=i+1
