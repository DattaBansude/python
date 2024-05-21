
# Print the status of the solution
print("status:", status) # 1:Optimal, 2:Not Solved, 3:Infeasible, 4:Unbounded, 5:Undef 
# Print each of the variables with it's resolved optimum value
for var in lp.variables():
    print(var, "=", value(var))