# 1076번 저항
color_list = []

#곱은 어차피 10의 제곱 형태로 나오기 때문에 생략
dict = {
"black": "0",
"brown": "1",
"red": "2",
"orange":	"3",
"yellow":	"4",
"green":	"5",
"blue":	"6",
"violet":	"7",
"grey":	"8",
"white":	"9"	
}

# 색깔 리스트 입력
for i in range(3):
  color_list.append(input())

# 3번째 곱 출력
num = 10**int(dict[color_list[2]])

# (1번째값 + 2번째값) * 3번째 곱
ohm = int(dict[color_list[0]]+dict[color_list[1]]) * num
print(ohm)