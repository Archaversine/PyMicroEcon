# PyMicroEcon

Python library to graph and solve microeconomics problems 

## Usage

### Graphing Budget Constraints

To make a budget constraints graph, three things are needed: the budget, and two different goods (with prices).

To make some goods, use the following:
This will create a good "Pizza" that costs $2.00, and a good "Gum" that costs $0.50.

```py
import microeconomics as micro
import matplotlib.pyplot as plt # Used for showing graph later

pizza = micro.Good("Pizza", price = 2)
gum = micro.Good("Gum", price = 0.50)
```

For the example, we'll also make a budget of $10:

```py
budget = 10
```

Finally to create the actual graph, simply plug in the values to the following function:

```py
micro.budget_constraint_graph(budget, pizza, gum)
plt.show() # Show the graph
```

![Budget Constraint](https://github.com/Archaversine/PyMicroEcon/blob/main/images/budget_constraints_1.png)

If inside a jupyter notebook, use `%matplotlib inline` without `plt.show()`.

The budget constraint graph also supports multiple curves. For example, to show the graph
for both of the budgets $10.00 and $12.00 with the same goods, use the following:

```py
import microeconomics as micro
import matplotlib.pyplot as plt

pizza = micro.Good("Pizza", 2)
gum = micro.Good("Gum", 0.5)
budgets = 10, 12

micro.budget_constraint_graph(budgets, pizza, gum)
plt.show()
```

![Budget Constraint](https://github.com/Archaversine/PyMicroEcon/blob/main/images/budget_constraints_2.png)