# --coding=utf-8--
def cheese_and_crackers(cheese_count,boxes_of_crackers): #定义函数cheese_and_crackers,参数为 cheese_count和boxes_of_crackers
    print "You have %d cheese!" % cheese_count #输出参数cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers #输出参数boxes_of_crackers
    print "Man that's enough for a prarty!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) #输出函数cheese_and_crackers参数为 20, 30

print "OR,we can use variables from our script:"
amount_of_cheese = 10 # 设置amount_of_cheese的变量值为10;
amount_of_crackers = 50 # 设置amount_of_crackers的变量值为50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #输出函数  cheese_and_crackers，参数使用变量 amount_of_cheese和amount_of_crackers

print "We can enen do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #输出函数 cheese_and_crackers，参数值使用加法 赋值

print "And we can combine the two,variables and math:"

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #输出函数 cheese_and_crackers，参数值使用变量加 整数
