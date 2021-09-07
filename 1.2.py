# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from math import factorial

n1 = int(factorial(4) / (factorial(1) * factorial(4 - 1)))
nt1 = int(factorial(51) / (factorial(3) * factorial(51 - 3)))
n2 = int(factorial(4) / (factorial(2) * factorial(4 - 2)))
nt2 = int(factorial(50) / (factorial(2) * factorial(50 - 2)))
n3 = int(factorial(4) / (factorial(3) * factorial(4 - 3)))
nt3 = int(factorial(49) / (factorial(1) * factorial(49 - 1)))
n4 = int(factorial(4) / (factorial(4) * factorial(4 - 4)))

A = n1*nt1 + n2*nt2 + n3*nt3 + n4
A