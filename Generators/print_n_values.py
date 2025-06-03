def n_values_gen(n):
    for i in range(1,n+1):
        yield i
val=int(input("Enter a value :"))
g=n_values_gen(val)
for x in g:
    print(x)

