from sys import stdin

# 한 단어를 readline할 때
mystr = stdin.readline()
print(mystr)
print(len(mystr))

# 여러 단어를 readline할 때
print("여러 단어를 입력하세요.(스페이스 포함)")
mystr = stdin.readline()
print(mystr)
print("같은 단어들를 입력하세요.(스페이스 포함)")
mystr = stdin.readline().split()
print(mystr)


