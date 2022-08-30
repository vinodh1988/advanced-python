def outer(p1):
    print("p1 is ",p1)
    def inner(p2):
        nonlocal p1
        print("p2 is ",p2)
        print("inside inner p1 is ",p1)
        p1=p1+10
    inner(100)
    return inner

# inner function can refer to variables of outer function
# but outer function cannot refer to variable of inner funciton
# inner function is meant to be called only with in the outer funciton
# you cannot directly call the inner funciton from outside of the outer funciton
# but inner function can be returned

outcome=outer(50)
#p1 is 50
#p2 is 100
#p1 is 50
# p1 <- 60 [not output]
outcome(500)
# p2 is 500
# p1 is 60
# p1 <- 70
outcome(1000)
# p2 is 1000
# p1 is 70
# p1 <- 80

