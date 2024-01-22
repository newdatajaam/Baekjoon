stu_num = int(input())
class_list = []

# 모든 학생의 반 정보를 class_list에 담기
for _ in range(1,stu_num+1):
  studnets = list(map(int, input().split()))
  class_list.append(studnets)

cnt = []
for ban in class_list:
  i_stu_num = []
  for i in range(5):   
    for j in range(stu_num):
      if ban[i] == class_list[j][i]:
        i_stu_num.append(j)
      else:
        pass
  cnt.append(len(list(set(i_stu_num)))-1)

print(cnt.index(max(cnt))+1)