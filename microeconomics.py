import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

class Good:
    def __init__(self, name: str, price: float = None, amount: int = None):
        self.name = name
        self.price = price
        self.amount = amount

    def __repr__(self) -> str:
        return f"<Good: '{self.name}'>"

class LinearFunc:

    @staticmethod
    def equilibrium_point(func1, func2) -> tuple:
        eq = (func2.constant - func1.constant) / (func1.coefficient - func2.coefficient)
        return (func1(eq), eq)

    def __init__(self, coefficient: float = 1, constant: float = 0) -> None:
        self.coefficient = coefficient
        self.constant = constant
    
    def __repr__(self) -> str:
        return f"Q = {self.coefficient} * p + ({self.constant})"

    def __call__(self, p) -> float:
        return p * self.coefficient + self.constant

    def root(self) -> float:
        return -self.constant / self.coefficient

    def inverse(self, q) -> float:
        return (q - self.constant) / self.coefficient

def equilibrium_point(func1, func2) -> tuple:
    # If more types of functions are added, change the following
    return LinearFunc.equilibrium_point(func1, func2)

def budget_constraint_points(budget: float, good1: Good, good2: Good) -> np.ndarray:
    if not good1.price or not good2.price:
        print("Warning! Price of 0 for goods when graphing budget constraint!")
        return

    good1_max = int(budget / good1.price) + 1
    points = np.ndarray((good1_max, 2), dtype=np.float32)

    # q1: Quantity of good 1
    for q1 in range(good1_max):
        # Flipped to make axes on graph match
        points[q1] = (((budget - q1 * good1.price) / good2.price), q1)

    return points

def budget_constraint_graph(budget: float, good1: Good, good2: Good) -> None:
    _, ax = plt.subplots()

    if not isinstance(budget, list) and not isinstance(budget, tuple):
        points = budget_constraint_points(budget, good1, good2)

        ax.plot(points[:, 0], points[:, 1], label=f"Budget: ${budget:.2f}")
    else:
        for i, b in enumerate(budget):
            points = budget_constraint_points(b, good1, good2)
            ax.plot(points[:, 0], points[:, 1], label=f"Budget: ${budget[i]:.2f}")

    ax.legend(loc="upper right")
    ax.set_title(f"Budget Constraints of {good1.name} and {good2.name}")
    ax.set_xlabel(f"Quantity of {good2.name}")
    ax.set_ylabel(f"Quantity of {good1.name}")

def supply_demand_graph(supply_func: LinearFunc, demand_func: LinearFunc) -> None:
    _, ax = plt.subplots()

    eq_x, eq_y = equilibrium_point(supply_func, demand_func)

    demand_max = demand_func(0)

    demand_points = ((0, demand_func.root()), (demand_max, 0))
    supply_points = (supply_func(0), 0), (demand_max, supply_func.inverse(demand_max))

    ax.plot(*zip(*demand_points), 'r', label="Demand")
    ax.plot(*zip(*supply_points), 'b', label="Supply")
    
    # Plot Equilibrium point
    ax.plot(eq_x, eq_y, 'k', marker="o", markersize=5)
    ax.annotate(f'({eq_x}, {eq_y})', (eq_x, eq_y), xytext=(-15, 15), textcoords="offset points")

    # Plot Dotted equilibrium lines
    ax.plot((0, eq_x), (eq_y, eq_y), ':k') # Dotted line from price axis
    ax.plot((eq_x, eq_x), (0, eq_y), ':k') # Dotted line from Quantity Axis

    ax.legend(loc="upper right")
    ax.set_title("Supply and Demand Graph")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Price")