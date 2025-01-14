import math
print("**----Quadratic equation solver----**")
print('Quadratic equation standard format: ax\u00b2 + bx + c = 0')
a = float(input("Enter the value for 'a' : "))
b = float(input("Enter the value for 'b' : "))
c = float(input("Enter the value for 'c' : "))
determinant = (b**2) - (4 * a * c)
eqn_pos = ((-1 * b) + math.sqrt(determinant)) / (2 * a)
eqn_neg = ((-1 * b) - math.sqrt(determinant)) / (2 * a)
print("\nx can have the values {} or {}".format(round(eqn_neg, 2), round(eqn_pos, 2)))

