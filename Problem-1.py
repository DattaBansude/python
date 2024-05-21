from pulp import *
# Creation of the model that will contain the data and solve the Lp
lp = LpProblem("Linear Programming Problem",LpMaximize)
#Define Variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)
# The Problem's Objective Function
lp += 4 * x + y
#Constraints
lp += x + y <= 50
lp += 3 * x + y <= 90
#Solve the Lp
status = lp.solve()
# Print the status of the solution  
print("status:", status) # 1:Optimal, 2:Not Solved, 3:Infeasible, 4:Unbounded, 5:Undef 
# Print each of the variables with it's resolved optimum value
for var in lp.variables():
    print(var, "=", value(var))
# Print the optimised value of the objective function
print("Maximum value of Z =", value(lp.objective))
