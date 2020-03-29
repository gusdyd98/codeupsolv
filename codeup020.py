import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

inputdata=input()
print(inputdata.split('-')[0]+inputdata.split('-')[1])