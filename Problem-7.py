from scipy.optimize import linprog
objfn=[-100000, -40000, -18000]
lhs= [[2000, 600, 300], [0, 1, 0], [-1, -1, 1], [-9, 1, 1]]
rhs= [18200, 10, 0, 0]
opt = linprog(c=objfn, A_ub=lhs, b_ub=rhs, method="simplex")
print(opt)
