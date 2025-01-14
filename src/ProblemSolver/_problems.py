"""
Each function here passes the input given in the Project Euler problemset to the
function which solves the respective problem.
"""

import sys
sys.path.insert(1, "../ProblemSolverTools")
import src.ProblemSolverTools as tools

def solve_problem1(self):
    return tools.MultiplesOf3and5.sum_of_multiples(1000)

def solve_problem2(self):
    pass

def solve_problem3(self):
    pass

def solve_problem4(self):
    pass

def solve_problem11(self):
    pass

def solve_problem12(self):
    pass

def solve_problem13(self):
    pass

def solve_problem14(self):
    return tools.LongestCollatzSeq.longest_collatz_end(1000000)