def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, areg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, areg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "some nonsence with no arguments"


print_two("alpha", "omega")
print_two_again("omega", "alpha")
print_one("wisky tango foxtrot")
print_none()



    