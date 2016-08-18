def f1():
    test = 1 #local scope
    print "f1",test

test = 0 #global scope
f1()
print 'global:', test

# Example: Function inside a function
#-- local and outer scope variables
def outer():
    test = 1
    def inner():
        test = 2
        print 'inner:', test
    
    inner()
    print 'outer:', test #if line 12 is commented, this will print value of line 20

test = 0 #global scope
outer()
print 'global:', test

# 'nonlocal' Example: how to use variable from outer scope in inner scope
def outer():
    test = 1
    def inner():
        nonlocal test #user scope from line 26
        test = 2 #changes outer scope value of test to 2
        print 'inner:', test
    
    inner()
    print 'outer:', test #outer scope

test = 0 #global scope
outer()
print 'global:', test

