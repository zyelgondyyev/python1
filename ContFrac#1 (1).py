#Programmer: Zhandos Yelgondyyev

#Code starts here:

def nonrecursive_cf(a):
    
    n = len(a)
    x = a[n-1]
    for i in range (n-2, -1, -1):
        x = a[i] + 1/x
    return x

def cf(a):                                              # this is the function for nonrecursive 
    x = a[0]
    
    if len(a) == 1:                                     # to avoid endless loop
        x = a[0]
        
    else:                                               # recursive func.
        x = x + 1/ cf(a[1:])
        
    return x

# The following code is for nonrecursive:

a = [0,1,1,2]
print ("%12.10f" % (nonrecursive_cf(a)))
print ("%12.10f" % (cf(a)))
print ()

b = [3, 7, 15, 1, 292, 1, 1, 1, 2] 
print ("%12.10f" % (nonrecursive_cf(b)))
print ("%12.10f" % (cf(b)))
print ()

c = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1]
print ("%12.10f" % (nonrecursive_cf(c)))
print ("%12.10f" % (cf(c)))
print ()

d = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] 
print ("%12.10f" % (nonrecursive_cf(d)))
print ("%12.10f" % (cf(d)))
print ()


    
# You must write a recursive version of the above function. Put your work here:


listinput = input("Please type the numbers from a, b, c, d respectively:  ")            # inputing the value of list

lists = []



for x in listinput.split():                             # spliting values of input
    y = int(x)
    lists.append(y)                                     # storing splitted numbers in the list
    
        
print ("%12.10f" % (cf(lists)))
        



# And ends here.



