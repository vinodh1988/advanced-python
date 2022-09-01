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

communicator(receiver)
