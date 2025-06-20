# import gurobi library
from gurobipy import *

# resources data
resources, capacity = multidict({
    "mahogany": 400,
    "labor": 450
})

# products data
products, price = multidict({
    "chairs": 45,
    "tables": 80,
    "desk": 110,
})

# Bill of materials: resources required by each product
bom = {
    ('mahogany', 'chairs'): 5,
    ('mahogany', 'tables'): 20,
    ('mahogany', 'desk'): 15,
    ('labor', 'chairs'): 10,
    ('labor', 'tables'): 15,
    ('labor', 'desk'): 25
}

# Declare and initialize model
f = Model("Furniture")

# Create decision variables for the products to make
make = f.addVars(products, name="make")

# Add constraints
res = f.addConstrs(((sum(bom[r, p] * make[p] for p in products) <= capacity[r]) for r in resources), name="r")

# The objective is to maximize total revenue
f.setObjective(make.prod(price), GRB.MAXIMIZE)

# save model for inspection
f.write('furniture.lp')


# Run optimization engine
f.optimize()

# Display optimal values of decision variables
for v in f.getVars():
    if (abs(v.x) > 1e-6):
        print(v.VarName, v.x)

# Display optimal total revenue
print("Optimal total revenue:", f.objVal)

# display shadow prices
for r in resources:
    if (abs(res[r].Pi) > 1e-6):
        print(f"Shadow price for {r}: {res[r].Pi}")
    