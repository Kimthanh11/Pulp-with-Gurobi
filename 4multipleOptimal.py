# import gurobi library
from gurobipy import *

# resources data
resources, capacity, cost = multidict({
    "mahogany": [400, 1],
    "labor": [450, 2]
})

# products data
products, price = multidict({
    "chairs": 50,
    "tables": 75
})

# Bill of materials: resources required by each product
bom = {
    ('mahogany', 'chairs'): 5,
    ('mahogany', 'tables'): 20,
    ('labor', 'chairs'): 10,
    ('labor', 'tables'): 15
}

# Declare and initialize model
f = Model("Furniture")

# Create decision variables for the products to make
make = f.addVars(products, name="make")

# Create decsion variables for the waste of resources
waste = f.addVars(resources, name="waste")

# Add constraints
res = f.addConstrs(((sum(bom[r, p] * make[p] for p in products) + waste[r] == capacity[r]) for r in resources), name="r")

# The objective is to maximize total revenue
f.setObjective(make.prod(price) - waste.prod(cost), GRB.MAXIMIZE)

# save model for inspection
f.write('furniture.lp')

# Run optimization engine
f.optimize()

# Display optimal values of decision variables
for v in f.getVars():
    if (abs(v.x) > 1e-6):
        print(v.VarName, v.x)

# Display optimal total revenue
print("total revenue", f.objVal)

# display shadow prices
for r in resources:
    print(res[r].ConstrName, res[r].Pi)

# display reduced costs
for v in f.getVars():
    print(v.VarName, abs(v.RC))