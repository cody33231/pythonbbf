# --coding:utf-8 --

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """ 
I'll do a list:     
\t* Cat food 
\t* Fishies  
\t* Catnip\n\t* Grass
""" # \t 横向制表符 \n 换行符

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "abcedfg %r" % """fd""f""djfdk'kf'd"""

#2.''' 不能替代""",因为'''是注释
#4.