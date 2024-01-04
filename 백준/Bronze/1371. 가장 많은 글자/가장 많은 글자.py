import sys
input_sentence = sys.stdin.read().replace("\n","").replace(' ', '')

dict = {}

for letter in input_sentence:
  if dict.get(letter):
    dict[letter] += 1
  else:
    dict[letter] = 1

answer_list = []
answer = ''
for key, value in dict.items():
  if max(dict.values()) == value:
    answer_list.append(key)

answer_list.sort()
answer = ''.join(answer_list)
print(answer)