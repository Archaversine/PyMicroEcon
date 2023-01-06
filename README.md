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

If inside a jupyter notebook, use `%matplotlib inline` without `plt.show()`.