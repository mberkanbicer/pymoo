import numpy as np

from pymoo.model.problem import Problem, ZeroToOneProblem
from pymoo.optimize import minimize
from pymoo.vendor.vendor_scipy import LBFGSB


class MySphere(Problem):

    def __init__(self, n_var=3):
        super().__init__(n_var=n_var, n_obj=1, n_constr=0, xl=-100, xu=5, type_var=np.double)

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = np.sum(np.square(x + 10), axis=1)


# for the local optimizer this is now a perfectly normalized problem
problem = ZeroToOneProblem(MySphere())

algorithm = LBFGSB()

res = minimize(problem,
               algorithm,
               seed=1,
               verbose=False)

# map the solution back to the original space
res.X = problem.denormalize(res.X)

print(f"{algorithm.__class__.__name__}: Best solution found: X = {res.X} | F = {res.F} | CV = {res.F}")
