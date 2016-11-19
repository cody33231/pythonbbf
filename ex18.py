# --coding=utf-8--
#this one is like your scripts with argv

def print_two(*args):
<<<<<<< HEAD
    arg1, arg2=args
=======
    arg1,arg2 = args
>>>>>>> 9a63fb703e2ec24fde39901e986f5e6836fb4a28
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok,that* args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("CC","DD")
print_one("Peter")
print_none()
