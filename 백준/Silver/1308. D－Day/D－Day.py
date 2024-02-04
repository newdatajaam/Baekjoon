from datetime import date
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

today = date(y1, m1, d1)
end_date = date(y2, m2, d2)
day_long = end_date - today
d_day = day_long.days # 애초에 윤년도 계산해주는 듯함

if (y1+1000) < y2:  # 천년 이상 차이
  print('gg')
elif y1+1000 == y2: # 딱 천년 차이
  if m1 > m2: # 월 차이
    print(f"D-{d_day}")
  elif m1 == m2: # 월이 같으면 일수 확인
    if d1 > d2 :
      print(f"D-{d_day}")
    else:
      print("gg")
  else:
    print('gg')
else:
  print(f"D-{d_day}")