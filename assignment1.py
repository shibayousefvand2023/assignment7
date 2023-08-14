# name = ('Wellocme to my jadval_zarb!')
# print(name)
name = ('How many row do you want?')
n = int(input('Enter Hear _>'))
f = int(input('Enter Hear _>'))
print('How many row do you want?')
for i in range(n):
    for m in range(i):
        print(f"{m+1} * {i} = {(m+1)* (i)}" , end='.')
        if m ==f:
            break
        print()





