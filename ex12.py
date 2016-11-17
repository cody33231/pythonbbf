# --coding:utf-8--
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How mach do you weight?")


print "So, you'r %r old, %r tall and %r heavy." % (age, height, weight)

'''
1.在命令行界面下运行你的程序，然后在命令行输入 pydoc raw_input 看它说了些什么。如果你用的是 Window，那就试一下 python -m pydoc raw_input 。
自动生成文档，这些文档可以基于文本呈现的、也可以生成WEB 页面的，还可以在服务器上以浏览器的方式呈现！
在本地机器上，按照给定的端口启动HTTP
D:\>python -m pydoc -p 1234 #比如说: 端口为1234
pydoc server ready at http://localhost:1234/
pydoc server stopped
2.输入 q 退出 pydoc。
3.上网找一下 pydoc 命令是用来做什么的。自动生成文档
4.使用 pydoc 再看一下 open, file, os, 和 sys 的含义。看不懂没关系，只要通读一下，记下你觉得有意思的点就行了。'''
