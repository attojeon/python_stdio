################################################
# 두 줄에 다음과 같은 형식의 입력
# 1 라인 : 5(다음 라인에 등장하는 수의 갯수)
# 2 라인 : 11 22 33 44 55
################################################

from sys import stdin

# 한 줄 읽어들임.
# 문자열을 strip 하고, split 한다.
# 주의사항 : 맨마지막에 보이지 않는 \n(New line) 문자가 포함되어 있음.
# 문자=>정수로 변환하는 것을 잊지 말 것!!!

n = int( stdin.readline().strip() )
ns  = [ int(x) for x in stdin.readline().strip().split()]


print(n)
print(ns)

# 위 ns가 어렵다면 다음과 같은 코드로 쉽게 할 수도 있음.
print("##################################")
arr = stdin.readline().strip().split()
arr_ns = []
for x in arr:
    arr_ns.append(int( x) )
print(arr_ns)