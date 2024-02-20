num = input()
one_cnt =  list(filter(None, num.split('1')))
zero_cnt =  list(filter(None, num.split('0')))

if len(one_cnt) >= len(zero_cnt):
  print(len(zero_cnt))
else:
  print(len(one_cnt))