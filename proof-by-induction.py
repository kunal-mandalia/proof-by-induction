from sympy import *
x, y, z, k, n = symbols('x y z k n')
init_printing(use_unicode=True)

# Sum of all integers
INPUT_FORMULA = 'n*(n+1)/2'
INPUT_BASE_CASE = 1
INPUT_NEXT_STEP = 'n+1'

# # Sum of all even numbers
# INPUT_FORMULA = 'n*(n+1)'
# INPUT_BASE_CASE = 2
# INPUT_NEXT_STEP = '2*(n+1)'

# Prove base case f(1) = 1
BASE_CASE = (sympify(INPUT_FORMULA)).subs(n, 1)
print 'Base case met?', BASE_CASE,INPUT_BASE_CASE, BASE_CASE == INPUT_BASE_CASE

# Prove if formula holds for k, it holds for k+1
INDUCTION_1 = INPUT_FORMULA.replace('n', '(k+1)')
EXPAND_INDUCTION_1 = expand(INDUCTION_1)
print INDUCTION_1, EXPAND_INDUCTION_1

INDUCTION_2 = INPUT_FORMULA.replace('n', 'k') + '+' + INPUT_NEXT_STEP.replace('n', 'k')
EXPAND_INDUCTION_2 = expand(INDUCTION_2)
print INDUCTION_2, EXPAND_INDUCTION_2

print 'Proved?', EXPAND_INDUCTION_1 == EXPAND_INDUCTION_2
