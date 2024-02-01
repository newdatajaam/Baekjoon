word = list(input())
case = len(word)
word_result = ''
total_word_list = []

for i in range(1,case-1):   # 1번째 글자부터 (단어길이-2)번째 글자까지
  area1 = word[:i]
  area1.reverse() # 리스트 뒤집기
  for j in range(i+1, case):  # i 번째 글자부터 (단이길이-1)번째까지
    area2 = word[i:j]
    area3 = word[j:]
    area2.reverse() # 리스트 뒤집기
    area3.reverse()
    word_result = ''.join(area1 +area2 + area3) # 각 리스트 합치기
    total_word_list.append(word_result)

total_word_list = sorted(total_word_list) # 모든 경우의 단어 조합 모아서 정렬
print(total_word_list[0])   # 가장 알파벳 빠른거 출력