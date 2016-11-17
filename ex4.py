# --coding: utf-8 --

cars = 100
space_in_a_car = 4 #如果这里使用整数4.0，那么变量“carpool_capacity = cars_driven（30） * space_in_a_car（4.0）的值就是120.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven =drivers
carpool_capacity = cars_driven * space_in_a_car #执行时提示“car_pool_capacity”变量没有被定义，修改变量
average_passengers_per_car = passengers /cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."