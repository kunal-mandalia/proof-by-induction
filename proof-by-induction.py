from sympy import *
x, y, z, k, n = symbols('x y z k n')
init_printing(use_unicode=True)

def verify_base_case(formula, valid_from_n, base_case):
    computed_base_case = (sympify(formula)).subs(n, valid_from_n)
    base_case_satisfied = computed_base_case == base_case
    return base_case_satisfied

def expand_induction_hypothesis_k_plus_1(formula, next_expression):
    # inductive hypothesis
    inductive_step = formula.replace('n', 'k') + '+' + next_expression.replace('n', 'k')
    return expand(inductive_step)

def expand_formula_k_plus_1(formula):
    return expand(formula.replace('n', '(k+1)'))

def prove_arithmetic_series_formula(formula, valid_from_n, base_case, next_expression):
    # verify base case
    base_case_satisfied = verify_base_case(formula, valid_from_n, base_case)

    # Inductive step
    inductive_hypothesis = expand_induction_hypothesis_k_plus_1(formula, next_expression)
    formula_next_term = expand_formula_k_plus_1(formula)

    # If the inductive hypothesis matches the formula for the next term
    # then we have proved the formula
    return {
        'base_case_satisfied': base_case_satisfied,
        'inductive_hypothesis': inductive_hypothesis,
        'formula_next_term': formula_next_term,
        'proved': inductive_hypothesis == formula_next_term
    }

# Sum of all even numbers
INPUT_FORMULA = 'n*(n+1)'
INPUT_VALID_FROM_N = 1
INPUT_BASE_CASE = 2
INPUT_NEXT_STEP = '2*(n+1)'

print prove_arithmetic_series_formula(
    INPUT_FORMULA,
    INPUT_VALID_FROM_N,
    INPUT_BASE_CASE,
    INPUT_NEXT_STEP
    )
