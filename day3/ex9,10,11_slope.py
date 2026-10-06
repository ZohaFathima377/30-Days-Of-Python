#8
print('Slope, x-intercept and y-intercept of y=2x-2')
m = 2
c = -2
x_intercept = -c/m
y_intercept = c
print('Slope:',m)
print('x-intercept:',x_intercept)
print('y-intercept:',y_intercept)

#9
import math
print('Finding the slope and the Euclidean Distance between the points (2,2) and (6,10) ')
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
ed = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('Slope:',slope)
print('Euclidean Distance:',ed)

#10
print(m == slope)
print(m > slope)
print(m < slope)
print(m >= slope)
print(m <= slope)
print(m != slope)