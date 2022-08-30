from decorators import crossfun

@crossfun
def logic(name,activity):
    print(name,' is performing ',activity) # main concern - original logic

logic('Hari','Coding')