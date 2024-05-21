from scipy.optimize import linprog
objfn=[-2, 1, -2]
lhs= [[2, 2, 0], [1, 2, -1], [0, 1, 2]]
rhs= [10, 20, 5]
opt = linprog(c=objfn, A_ub=lhs, b_ub=rhs, method="simplex")
print(opt)