# Proof by induction

Mathematical induction uses an interesting strategy to prove statements. An analogy I like is toppling dominos:
- If a domino falls, it'll topple over its neighbour (inductive hypothesis)
- Show that a particular (base case) domino falls

The general algorithm is implemented in this script. It can prove formulas of arithmetic sums e.g. the sum of the first `n` natural numbers. Python was used because of the excellent `SymPy` module which is used to expand and simplify mathematical expressions.


## Dependencies

- Python 2.7.1
- SymPy

# License
MIT