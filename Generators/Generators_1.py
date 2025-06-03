#Gnerators are a special type of function used to generate a sequence of values using
#special keyword called 'yield'

def mygen():
    yield "A"
    yield "B"
    yield "C"
g=mygen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) throws error stopIteration Error
for x in g:
    print(x)
