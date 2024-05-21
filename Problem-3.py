from pulp import *
# Creation of the model that will contain the data and solve the Lp
lp = LpProblem("Linear Programming Problem",LpMinimize)
#Define Variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)
# The Problem's Objective Function
lp += -50 * x + 20 * y
#Constraints
lp += 2 * x - y >= -5
lp += 3 * x + y >= 3
lp += 2 * x - 3 * y <= 12
#Solve the Lp
status = lp.solve()
# Print the status of the solution
print("status:", status) # 1:Optimal, 2:Not Solved, 3:Infeasible, 4:Unbounded, 5:Undef 
# Print each of the variables with it's resolved optimum value
for var in lp.variables():
    print(var, "=", value(var))
# Print the optimised value of the objective function
print("Minimum value of Z =", value(lp.objective))
