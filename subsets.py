from itertools import chain, combinations

sum_a = list()
sum_b = list()
sum_total = list()
x, y = 0, 0

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def sum_set (a, b):
    for i in a:
        sum_a.append(sum(i))
    for j in b:
        sum_b.append(sum(j))

a = list (powerset([1,2,3,4,5,6]))
b = list (powerset([9,10,11,12,13,14]))
sum_set(a, b)

for i in sum_a:
    for j in sum_b:
        if i == j:
            x, y  = sum_a.index(i), sum_b.index(j)
            print (a[x], b[y])