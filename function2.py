# These examples define abs(n), which is a nice example here, but it is
# also a builtin function, so you do not need to define it to use it.

def abs1(n):
    if (n < 0):
        n = -n
    return n

# again, with same-line indenting

def abs2(n):
    if (n < 0): n = -n # only indent this way for very short lines (if at all)
    return n

# again, with multiple return statements

def abs3(n):
    if (n < 0):
        return -n
    return n

# aside: you can do this with boolean arithmetic, but don't!

def abs4(n):
    return (n < 0)*(-n) + (n>=0)*(n) # this is awful!

# now show that they all work properly:

print("abs1(5) =", abs1(5), "and abs1(-5) =", abs1(-5))
print("abs2(5) =", abs2(5), "and abs2(-5) =", abs2(-5))
print("abs3(5) =", abs3(5), "and abs3(-5) =", abs3(-5))
print("abs4(5) =", abs4(5), "and abs4(-5) =", abs4(-5))
