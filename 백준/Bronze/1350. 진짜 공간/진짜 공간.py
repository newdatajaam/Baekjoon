# 1350번 진짜 공간

file_num = int(input())

disk_space = list(map(int,input().split()))

disk_size = int(input())

disk_num = 0

for file in disk_space:
  if file == 0:
    disk_num += 0
  elif file // disk_size == 0:
    disk_num += 1
  elif file // disk_size >= 1 and file % disk_size == 0:
    disk_num += file // disk_size
  else:
    disk_num += (file // disk_size + 1)
    

print(disk_size * disk_num)