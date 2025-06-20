# import gurobi libraries
from gurobipy import *

# Create Furniture Factory Model
f = Model("Furniture")

#  Define Variables
x1 = f.addVar(name="chairs")
x2 = f.addVar(name="tables")

# Set Objective Function
f.setObjective(45 * x1 + 80 * x2, GRB.MAXIMIZE)

# Add mahogany constraint
f.addConstr(5 * x1 + 20 * x2 <= 400, "mahogany")

# Add labor constraint
f.addConstr(10 * x1 + 15 * x2 <= 450, "labor")

# Run optimization engine
f.optimize()

# Display optimal production plan
for v in f.getVars():
    print(v.VarName, v.x)

print("Optimal total revenue:", f.objVal)