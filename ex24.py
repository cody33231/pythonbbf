# --coding=utf-8--

print "Let's practice everything."
print "You\'d neet to know \'bout escapes with \\ that do \n newlines and \t tabs."

#\转义将字符不转义，\n换行，\t空格
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is non.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be filve: %s " % five

def secret_formula(started): #定义函数secret_formula,参数为 started
    jelly_beans = started * 500  #变量jelly_beans值为参数 started* 500
    jars = jelly_beans / 1000   #变量jars值为 jelly_beans / 1000
    crates = jars / 100 #变量crates 值为 jars / 100
    return jelly_beans, jars, crates #secret_formula 函数返回值为 jelly_beans,jars,crates


start_point = 1000 #变量 start_point值为1000
beans, jars, crates = secret_formula(start_point)  #这行代码可以不用？？？？必须定义这3个变量后才能出 34line的值

print "With a starting point of: %d " % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
#cc = secret_formula(start_point)

#print beans, jars, crates
