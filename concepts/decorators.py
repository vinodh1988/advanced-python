def crossfun(fun):
    def inner(*args,**kwargs):
        print("The cross cutting logic - Proprocessing")
        fun(*args,**kwargs)
        print("The cross cutting logic - PostProcessing")
    return inner