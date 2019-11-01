from sys import stdin

# 한 줄 읽어들임.
# 주의사항 : 맨마지막에 보이지 않는 \n(New line) 문자가 포함되어 있음.
mystr =  stdin.readline()
print(mystr)

# 보이지 않는 \n을 없애기 위해 strip()을 사용함.
mystr = stdin.readline().strip()
print(mystr)