from scipy.optimize import linprog
objfn=[-20, -12, -40, -25]
lhs= [[1, 1, 1, 1], [3, 2, 1, 0], [0, 1, 2, 3]]
rhs= [50, 100, 90]
opt = linprog(c=objfn, A_ub=lhs, b_ub=rhs, method="revised simplex")
print(opt)