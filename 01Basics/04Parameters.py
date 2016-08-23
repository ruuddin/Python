#Example 1
print "Ex1:"
x = 10
def param_test(y):
    y = 13
param_test(x)
print "\tVal of x: ", x

# Example 2
print "Ex2:"
x = [1, 2, 3]
def mutable_test(x):
    x[1] = 42 #changing only one element works! No reference change

mutable_test(x)
print "\tMutable test:",x

# Example 3: 
print "Ex3:"
x = [1, 2, 3]
def mutable_test(x):
    x[1] = 42
    x = 'Print something' # this does not change the global ValueError

mutable_test(x)
print "\t",x

#Ex4: Keyword arguments

print "Ex4:"
def func(a, b, c):
    print "\tKeyword arguments example:" ,a, b, c

func(c=10, b = 100, a = 1) #assigning arguments based on keywords from function definition

#Ex5: Default arguments
print "Ex5:"
def f5(a, b=10, c=30): #Rule - default arguments must always be after non-default argument
    print "\tDefault args: ", a, b, c

f5(10, 20) #Rule - positional args always appear 1st, Keyword arguments always appear last

#Ex6: Variable arguments
print "Ex6:"
def f6(*n):
    print "\t",n
    if n: # checks for emptiness
        min = n[0]
        for v in n:
            if v < min:
                min = v
        print "\tVariable args - Min value :",min

f6(1, 2, 4, -1, -2, 100)
f6(1, 2, -4, -10, 2, 100, 500, -3)
vals = (1, 3, -7, 9)
f6(vals) # equivalent to: func((1, 3, -7, 9))
f6(*vals) # equivalent to: func(1, 3, -7, 9). Unpacks the tuple and calls the function with 4 args

#Ex7: Variable 'positional' arguments
print "Ex7:"
def f7(**n): #double ** compared to single * in Ex6 (variable arguments). n must be a dictionary
    print "\t",n

f7(a=1, b=2)
f7(**{'a':1, 'b': 42}) #unpacks the dictionary
f7(**dict(a=1, b=42))

#Ex8: Mutable defaults
print "Ex8:"
def f8(a=[], b={}): # If a, b are changed, this change will stick around in subsequent function calls.
    print "\t",a
    print "\t",b
    print "\t",'#' * 12
    a.append(len(a))  # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one

f8()
f8()
f8()