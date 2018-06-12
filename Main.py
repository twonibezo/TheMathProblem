x = list(range(-30,31))
y = list(range(-30,31))
z = list(range(-30,31))
print ('The solves of the equations is here: ')
for i in x:
    for u in y:
        for c in z:
            if (x[i]**3+y[u]**3+z[c]**3) == 8:
                w = x[i], y[u], z[c]
                if x[i] != y[u] and y[u] != z[c] and x[i] != z[c]:
                    if x[i] + y[u] + z[c] == 8:
                        print(w)


