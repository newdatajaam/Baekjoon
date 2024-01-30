import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]  # 단어를 리스트로 받음
word_dict = {}

for word in data:
  word_dict[word] = len(word)     # 딕셔너리로 {단어 : 단어 길이}입력 받음

ans = sorted(word_dict.items(), key=lambda x: (x[1],x[0]))

for i in range(len(ans)):
  print(ans[i][0])