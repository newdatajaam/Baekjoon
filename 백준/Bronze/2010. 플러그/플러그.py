multi_plug = int(input())
plug_hole = []
total_hole = 0

for i in range(multi_plug):
  plug_hole.append(int(input()))

for plugs in plug_hole:
  total_hole += plugs

print((total_hole)-(len(plug_hole)-1))