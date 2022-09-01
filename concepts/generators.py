# a function usually returns one value to the caller when

# some times there might   be a need for a 
# function to communicate back to caller zero or more times asynchronously.
import random

def communicator(callback):
    listf=['apple','oranges','banana','figs','Dates','Papaya','Gauva','Cherry','Pomegranate','Tomato']

    print('the communciator function started working')
    while True:
        a=int(random.random()*10)
        if(a==5 or a==7 ):
            print('since we got ',a, ' we are terminating')
            break
        callback(listf[a])



# the above call needs to receive communication zero or more times from the communicator
# function 
# to achieve this functional programming languages uses a concept called callbacks

def receiver(data):
    print("Received -> ",data )

#communicator(receiver)


# Generators  function 

def fungen():
    listf=['apple','oranges','banana','figs','Dates','Papaya','Gauva','Cherry','Pomegranate','Tomato']

    print('the communciator function started working')
    while True:
        print("Will do if only you say yes-->")
        a=int(random.random()*10)
        if a==5 or a==7:
            print("We are not going to yield any values any more as we got, ",a)
            break
        yield listf[a]
    
    
def caller():
    gen=fungen()
    while(True):
        print("user logic is getting execute ->")
        result=gen.__next__()
        print('received ->',result)
        con=input('enter x if you want to exit any other character to continue')
        if(con=='x'):
            break

  
caller()
        