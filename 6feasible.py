minRev = 4500
# import gurobi library
from gurobipy import *

# resources data
resources, capacity, extraCost = multidict({
    "mahogany": [400, 20],
    "labor": [450, 30]
})

# products data
products, price = multidict({
    "chairs": 45,
    "tables": 80
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

# Create decision variables for extra capacity of resources
extra = f.addVars(resources, name="extra")

# Add constraints
res = f.addConstrs(((sum(bom[r, p] * make[p] for p in products) - extra[r] <= capacity[r]) for r in resources), name="r")

# Board constraint of minimum revenue
minProfitConstr = f.addConstr((sum(price[p] * make[p] for p in products)) >= minRev, name="B")

# The objective is to maximize total revenue
f.setObjective(make.prod(price) - extra.prod(extraCost), GRB.MAXIMIZE)

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

# Check if model infeasible or unbounded
if f.Status == GRB.Status.INF_OR_UNBD:
    print('LP problem is either infeasible or unbounded.')
    print('Checking if LP problem is infeasible...')
    print('set objective function to zero value and re-run engine')
    f.setObjective(0, GRB.MAXIMIZE)
    f.optimize()

# CHeck if model with zero objective is feasible
if f.status == GRB.Status.INFEASIBLE:
    print('LP problem is proven to be infeasible.')