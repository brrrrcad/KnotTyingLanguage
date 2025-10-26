from src import Rope, pturn

R = Rope()
w = R.w
s = R.s

t, c1, c2 = pturn(w) # TODO: replace with w.minus(30)
p1 = ppass(w, t) # TODO: replace with w.minus(10)
l, p2 = ploop(w, s)
p3 = npass(w, t)