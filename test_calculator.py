from calculator import Calculator

calc = Calculator()

# assert fails the pipeline if the condition is false
assert calc.add(2, 3) == 5, "2 + 3 should be 5"
assert calc.subtract(10, 4) == 6, "10 - 4 should be 6"

print("ALL TESTS PASSED!")