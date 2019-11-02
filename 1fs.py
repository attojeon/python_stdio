################################################
# 한 줄에 여러 개의 실수가 있는 입력처리
################################################

from sys import stdin

# 한 줄 읽어들임.
# split을 할 경우 strip을 하지 않아도 마지막 라인의 '\n'이 자연히 없어진다.
# 주의사항 : \n이 없어지는 원리를 정확히 이해해야 합니다.
# 문자=>실수로 변환하는 것을 잊지 말 것!!!

mystr =  stdin.readline().split()

for n in mystr:
    print(float(n))
