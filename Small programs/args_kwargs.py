#===================*ARGS=========================
def summation(*n):
    sum=0
    for x in n:
        sum = sum+x
    print("The sum is :",sum)
summation(10,20,20)
summation(10,20)
summation(40,50,20,10)

#==================**KWARGS=======================

def info(**kwargs):
    print(kwargs)
info(name = "Wahida",age = 27)
