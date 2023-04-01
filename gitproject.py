from random import randint
x = []
for i in range(10):
    x.append(randint(1,10))
print(x)
print(sum(x)/len(x))