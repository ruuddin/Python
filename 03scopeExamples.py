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

# 'global' - bind to variable in global scope
def outer():
    test = 1  # outer scope

    def inner():
        global test
        test = 2  # global scope
        print 'inner:', test
    inner()
    print 'outer:', test

test = 0  # global scope
outer()
print 'global:', test