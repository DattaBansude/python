from pulp import* 
# Data for Linear Optimization Problem
M = 2 # Supply Points
N = 3 # Demand Points
a = range(1, M+1)
a1 = range(M)
b = range(1, N+1)
b1 = range(N)
# Index List for decision variable x
xindx = [(a[i],b[j]) for j in b1 for i in a1]
# Creation of the model that will contain the data and solve the Lp
model = LpProblem("Transportation LP Problem", LpMinimize)
# Creation of the Decision variables
x = LpVariable.dicts("X", xindx, 0, None)
# The Problem's Objective Function
model += 160*x[1,1] + 100*x[1,2] + 150*x[1,3] \
 + 100*x[2,1] + 120*x[2,2] + 100*x[2,3], "Transportation Cost"
# Supply Constraints
model += x[1,1] + x[1,2] + x[1,3] <=8, "Supply Pt 1"
model += x[2,1] + x[2,2] + x[2,3] <=6, "Supply Pt 2"
# Demand Contraints
model += x[1,1] + x[2,1] >= 5, "Demand Pt 1"
model += x[1,2] + x[2,2] >= 5, "Demand Pt 2"
model += x[1,3] + x[2,3] >= 4, "Demand Pt 3"
# Solve the Optimization Problem
model.solve()
# Print the status of the solution
print("Status:",LpStatus[model.status]) # 1:Optimal, 2:Not Solved, 3:Infeasible, 4:Unbounded, 5:Undef 
# Print each of the variables with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)
# Print the optimised value of the objective function
print("Minimum Transportation Cost = ", value (model.objective))