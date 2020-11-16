from pymoo.algorithms.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.problems.multi import CTP3
from pymoo.visualization.scatter import Scatter

problem = CTP3()

algorithm = NSGA2()

res = minimize(problem,
               algorithm,
               seed=1,
               verbose=True)

plot = Scatter()
plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
plot.add(res.F, color="red")
plot.show()
