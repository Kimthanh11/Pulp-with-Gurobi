# import gurobi library
from gurobipy import *

# resources data
resources, capacity = multidict({
    "mahogany": 400,
    "labor": 450
})

# products data
products, price, upBound = multidict({
    "chairs": [45, 200],
    "tables": [80, 150],
})

# Bill of materials: resources required by each product
bom = {
    ('mahogany', 'chairs'): 5,
    ('mahogany', 'tables'): 20,
    ('labor', 'chairs'): 10,
    ('labor', 'tables'): 15,
}

# Declare and initialize model
f = Model("Furniture")

# Create decision variables for the products to make
make = f.addVars(products, ub = upBound, name="make")

# Add constraints
res = f.addConstrs(((sum(bom[r, p] * make[p] for p in products) >= capacity[r]) for r in resources), name="r")

# The objective is to maximize total revenue
f.setObjective(make.prod(price), GRB.MAXIMIZE)

# save model for inspection
f.write('furniture.lp')


# Run optimization engine
f.optimize()


# display optimal values of decision variables
if f.status == GRB.Status.OPTIMAL:
    print("Optimal solution found.")
    print("total profits", f.objVal)
    for v in f.getVars():
        print(v.VarName, v.x)