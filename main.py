from ktl import *

R1 = Rope()
R2 = Rope()
w1 = R1.w
s1 = R1.s
w2 = R2.w
s2 = R2.s

t, c1, c2 = nturn(w1)
p1 = npass(w2, t)
l, p2 = ploop(w2, s1)
p3 = ppass(w2, t)

R1.equalize()
# Test locations order
reference1 = [p2, c1, c2]
locations1 = [loc for loc in R1.locations if loc in reference1]
assert locations1 == reference1

R2.equalize()
# Test locations order
reference2 = [p1, l.start, l.end, p3]
locations2 = [loc for loc in R2.locations if loc in reference2]
assert locations2 == reference2

# Test stability of print
R1.print(t=t, c1=c1, c2=c2, p2=p2)
R2.print(p1=p1, l=l, p3=p3)