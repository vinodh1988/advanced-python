from decorators import crossfun

@crossfun
def logic(name,activity):
    print(name,' is performing ',activity) # main concern - original logic

@crossfun
def sample():
    print("Cool Sample function")

logic('Hari','Coding')
sample()