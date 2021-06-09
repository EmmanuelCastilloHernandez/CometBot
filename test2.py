import sympy as sp
l = sp.Symbol('l')
f = l**2 - l + 3/16
l = sp.solve(f)
print(l)
for x in l:
  print(x)