# Optimization with PuLP and Gurobi – Furniture Factory Cases

This repository includes a collection of optimization problems solved using **Gurobi** with Python. These models simulate realistic business decision-making scenarios based on a furniture factory use case.

---

### 📚 Based On

These examples are inspired by and follow the tutorial playlist:  
🎥 [Gurobi Linear Programming Tutorials – YouTube](https://www.youtube.com/playlist?list=PLHiHZENG6W8BeAfJfZ3myo5dsSQjEV5pJ)

---

## 📁 Files and Descriptions

| File Name              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `1furnitureFactory.py` | Basic furniture production model maximizing revenue with wood and labor constraints. |
| `2parameterized.py`    | A more flexible model using dictionaries for resources, products, and BOM.         |
| `3shadowPrice.py`      | Adds a new product and prints shadow prices (dual values) for each constraint.   |
| `4multipleOptimal.py`  | Models multiple optimal solutions and shows reduced costs and shadow prices.     |
| `5unbounded.py`        | Demonstrates an unbounded problem when constraints are set improperly.           |
| `6feasible.py`         | Adds flexibility by purchasing extra resources if needed to reach profit targets.|
| `furniture.lp`         | LP file generated from the models for inspection in LP format.                   |
