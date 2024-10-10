#write a program that calculates volume of a sphere
import math
radius = int(input('Enter radius of the sphere: '))
height = int(input('Enter height of the sphere: '))
pie =math.pi
volume = pie * radius **2 * height
print(volume)