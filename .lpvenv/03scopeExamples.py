def f1():
    test = 1 #local scope
    print "f1",test

test = 0 #global scope
f1()
print 'global:', test

# Example: Function inside a function
#-- local and outer scope variables
def f2_outer():
    test = 1
    def f2_inner():
        test = 2
        print 'inner:', test
    
    f2_inner()
    print 'outer:', test #if line 12 is commented, this will print value of line 20

test = 0 #global scope
f2_outer()
print 'global:', test

# 'nonlocal' Example: how to use variable from outer scope in inner scope
def f3_outer():
    test2 = 1
    def f3_inner():
        nonlocal test2
        test2 = 2 #changes outer scope value of test to 2
        print 'inner:', test2
    
    f3_inner()
    print 'outer:', test2 #outer scope

test2 = 0 #global scope
f3_outer()
print 'global:', test2

# 'global' - bind to variable in global scope
def f4_outer():
    test3 = 1  # outer scope

    def f4_inner():
        global test3
        test1 = 2  # global scope
        print 'inner:', test3
    f4_inner()
    print 'outer:', test3

test3 = 0  # global scope
f4_outer()
print 'global:', test3