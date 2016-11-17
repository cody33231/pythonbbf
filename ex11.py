# --coding:utf-8 --

print "How old are you", #每行 print 后面加了个逗号(comma) , 了吧？这样的话 print 就不会输出新行符而结束这一行跑到下一行去了。
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old,%r tall and %r heavy." % (age, height,weight)