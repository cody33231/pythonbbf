# --coding:utf-8 --

my_name = 'Zad A. Shaw'
my_age =  35 # not a lie
my_height = 74 #inches
my_weight = 180  #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %r." % my_name
print "He's %r inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's not %r eyes end %r hair." % (my_eyes, my_hair)
print "His teeth are usually %r depending on the offee." % my_teeth

# this line is tricky, try to get it exactly right 

print "If I add %r, %r, and %r I get %r." % (my_age,my_height,my_weight,my_age + my_height +my_weight)



'''
1.修改所有的变量名字，把它们前面的``my_``去掉。确认将每一个地方的都改掉，不只是你使用``=``赋值过的地方。
2.试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。
3.在网上搜索所有的 Python 格式化字符。
4.试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。???'''