# 1408번 24

h1, m1, s1 = map(int,input().split(":"))
h2, m2, s2 = map(int,input().split(":"))

time = h2*3600+m2*60+s2 - (h1*3600+m1*60+s1)
if time < 0:
  time += 24*60*60

h3 = time//3600
m3 = (time%3600)//60
s3 = (time%3600)%60

if h3 < 10:
  h3 = '0' + str(h3)
else:
  str(h3)
if m3 < 10:
  m3 = '0' + str(m3)
else:
  str(m3)
if s3 < 10:
  s3 = '0' + str(s3)
else:
  str(s3)

print(f"{h3}:{m3}:{s3}")