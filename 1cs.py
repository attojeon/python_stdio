################################################
# 한 줄에 여러 개의 문자/문자열이 있는 입력처리
################################################

from sys import stdin

# 한 줄 읽어들임.
# 문자열을 strip 하고, split 한다.
# 주의사항 : 맨마지막에 보이지 않는 \n(New line) 문자가 포함되어 있음.

mystr =  stdin.readline().strip().split()

for s in mystr:
    print(s)
