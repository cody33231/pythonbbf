# --coding:utf-8 --
x = "There are %d types of people." % 10  #变量X定义为字符串和十进制数字
binary = "binary"
do_not ="don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e #将 w 和 e拼接起来