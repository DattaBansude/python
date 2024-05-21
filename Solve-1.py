from pulp import *
# Creation of the model that will contain the data and solve the Lp
lp = LpProblem("Linear Programming Problem",LpMinimize)
#Define Variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)
# The Problem's Objective Function
lp += 0.2 * x + 0.8 * y
#Constraints
lp += x + y >= 700
lp += 0.21 * x - 0.30 * y <= 0
lp += 0.03 * x - 0.01 * y >= 0
#Solve the Lp
status = lp.solve()
# Print the status of the solution
print("status:", status) # 1:Optimal, 2:Not Solved, 3:Infeasible, 4:Unbounded, 5:Undef 
# Print each of the variables with it's resolved optimum value
for var in lp.variables():
    print(var, "=", value(var))
# Print the optimised value of the objective function
print("Minimum value of Z =", value(lp.objective))
