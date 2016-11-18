# --coding=utf-8--
from sys import argv #导入argv

script,filename = argv #设置
txt = open(filename) #打开文件设置为txt

print "Here's you file %r:" % filename #打印
print txt.read()
txt.close()

print "Type the filename again."
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()

txt.close()