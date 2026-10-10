# Input nums

a = int(input('Enter first num:'))
b = int(input('Enter second num:'))

# Sum func

def sloj(a, b):
    return a + b

# Substraction func

def vichit(a, b):
    return a - b

# Multiply func

def umnoj(a, b):
    return a * b

# Division func

def delit(a, b):
    if b!=0:
        return a // b
    else:
        print('Error, division by 0')

# Output

s = sloj(a, b)
v = vichit(a, b)
u = umnoj(a, b)
d = delit(a, b)

print(s)
print(v)
print(u)
print(d)
