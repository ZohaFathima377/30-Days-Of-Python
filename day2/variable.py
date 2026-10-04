#Day 2: 30 Days of Python Programming
#Day 2 Exercise Level-1
first_name='Zoha'
last_name='Fathima'
full_name='Zoha Fathima'
country='India'
city='Bengaluru'
age=19
year=2026
is_married=False
is_true=True
is_light_on=True
college,course,sem='MCU','BCA',3

#Day 2 Exercise Level-2
#1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(college))
print(type(course))
print(type(sem))

#2
print(len(first_name))

#3
print('First Name:',len(first_name),'Last Name:',len(last_name))

#4
num_one=5
num_two=4

#5
total=num_one + num_two
print(total)

#6
diff=num_one - num_two
print(diff)

#7
product=num_one * num_two
print(product)

#8
division=num_one / num_two
print(division)

#9
remainder=num_two % num_one
print(remainder)

#10
exp=num_one ** num_two
print(exp)

#11
floor_division=num_one // num_two
print(floor_division)

#12
#radius = 30m 
# 1. Calculate area   2. Calculate circumference   3. Take radius as user input and calculate area
area=3.142*30*30
print('Area:',area)

circumference=2*3.142*30
print('Circumference:',circumference)

radius=float(input('Enter Radius:'))
_area=3.142*radius*radius
print('Area:',_area)

#13
firstname=input('Enter first name:')
lastname=input('Enter last name:')
country=input('Enter country:')
age=input('Enter age:')

print(firstname,lastname,country,age)