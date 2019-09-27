import math

ab = float(input())
bc = float(input())

h = math.hypot(ab,bc)
h = h / 2.0
adj = bc / 2.0
print (str(int(round(math.degrees(math.acos(adj/h))))) + "°")
