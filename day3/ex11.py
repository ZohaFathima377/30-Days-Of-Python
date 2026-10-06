#11
import math
print('y = x ^ 2 + 6x + 9')
a = 1
b= 6
c = 9
x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
print('The roots of the equation are:',x1,' ',x2)