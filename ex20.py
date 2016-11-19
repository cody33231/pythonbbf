# --coding=utf-8--
from sys import argv

script, input_file = argv #设置需要两个参数 script,input_file

def print_all(f): #定义函数print_all，参数是f
    print f.read() #打印 f使用read 文件的方法

def rewind(f): #定义函数rewind，参数是f
    f.seek(0) #使用f 的方法是seek()   ps:seek方法用于移动文件读取指针到指定位置。
def print_a_line(line_count,f): #定义函数print_a_line,参数是line_count和f
    print line_count,f.readline() #打印 line_count参数和对readline参数使用f方法

current_file = open(input_file) #current_file变量定义为 open方法打开input_file参数的过程

print "First Let's print the whole file:\n"

print_all(current_file) #执行函数print_all使用current_file变量

print "Now Let's rewind, Kind of likea tape."

rewind(current_file)#执行函数rewind使用current_file变量

print "Let's print three lines:"

current_line = 1 #给变量current_line赋值为1
print_a_line(current_line,current_file) #执行函数print_a_line，参数使用current_line变量和current_file参数

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
