from src import Rope, pturn, ppass, npass, ploop

R = Rope()
w = R.w
s = R.s

t, c1, c2 = pturn(w) # TODO: replace with w.minus(30)
p1 = ppass(w, t) # TODO: replace with w.minus(10)
l, p2 = ploop(w, s)
p3 = npass(w, t)

R.equalize()
R.print(t=t, c1=c1, c2=c2, p1=p1, l=l, p2=p2, p3=p3)